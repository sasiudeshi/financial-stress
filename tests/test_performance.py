"""Basic performance check: /predict should respond quickly and consistently."""
import time


def test_20_consecutive_predict_requests_each_under_one_second(client, valid_payload):
    # Warm up first so lazy-loading the model/scaler/SHAP explainer on the
    # very first call doesn't get counted against the per-request budget.
    client.post("/predict", json=valid_payload)

    durations = []
    for _ in range(20):
        start = time.perf_counter()
        response = client.post("/predict", json=valid_payload)
        elapsed = time.perf_counter() - start

        assert response.status_code == 200
        durations.append(elapsed)
        assert elapsed < 1.0, f"request took {elapsed:.3f}s, expected < 1.0s"

    print(f"\n20 requests: min={min(durations):.4f}s max={max(durations):.4f}s "
          f"avg={sum(durations) / len(durations):.4f}s")
