"use strict";

/* Field validation rules mirror the backend's Pydantic model
   (src/app/api.py: FinancialProfileRequest) so users get instant feedback
   before the request ever reaches the API. The API remains the final
   authority -- any 422 it returns is still surfaced field-by-field. */
const MONEY_MAX = 10000000;
const COUNT_MAX = 100000;

const FIELD_RULES = {
  age: { type: "int", min: 18, max: 100 },
  employment_status: { type: "enum", values: ["Employed", "Self-employed", "Student", "Unemployed"] },
  dependents: { type: "int", min: 0, max: 20 },
  monthly_income: { type: "float", strictPositive: true, max: MONEY_MAX },
  monthly_expenditure: { type: "float", strictPositive: true, max: MONEY_MAX },
  essential_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  non_essential_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  housing_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  utility_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  food_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  healthcare_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  education_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  transportation_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  shopping_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  entertainment_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  subscription_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  other_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  debt_repayment: { type: "float", min: 0, max: MONEY_MAX },
  num_financial_commitments: { type: "int", min: 0, max: COUNT_MAX },
  savings: { type: "float", min: -MONEY_MAX, max: MONEY_MAX },
  planned_expenditure: { type: "float", min: 0, max: MONEY_MAX },
  transaction_frequency: { type: "int", min: 1, max: COUNT_MAX },
  spending_volatility: { type: "float", min: 0, max: MONEY_MAX },
  impulse_purchase_frequency: { type: "int", min: 0, max: COUNT_MAX },
  online_purchase_frequency: { type: "int", min: 0, max: COUNT_MAX },
  unplanned_expenditure_frequency: { type: "int", min: 0, max: COUNT_MAX },
  budget_exceed_frequency_last3mo: { type: "int", min: 0, max: 3 },
  can_save_regularly: { type: "enum", values: ["Yes", "Sometimes", "No"] },
  balance_check_frequency_per_week: { type: "int", min: 0, max: COUNT_MAX },
  spending_change_during_difficulty: { type: "int", min: 1, max: 5 },
};

const WEATHER_COPY = {
  Low: { word: "Clear", sub: "Your finances currently look steady." },
  Moderate: { word: "Changeable", sub: "Some ups and downs worth keeping an eye on." },
  High: { word: "Stormy", sub: "Things look turbulent right now — worth addressing gently, not alarmingly." },
};

const form = document.getElementById("stress-form");
const formView = document.getElementById("form-view");
const resultsView = document.getElementById("results-view");
const submitBar = document.getElementById("submit-bar");
const submitBtn = document.getElementById("submit-btn");
const submitBtnLabel = document.getElementById("submit-btn-label");
const submitStatus = document.getElementById("submit-status");
const submitError = document.getElementById("submit-error");
const startOverBtn = document.getElementById("start-over");

function fieldEl(name) {
  return document.getElementById(name);
}
function errorEl(name) {
  return document.getElementById(name + "-error");
}

/* ------------------------------------------------------------------------
   Motion utilities. prefersReducedMotion() is re-checked at the point each
   animated feature is triggered (not just once at load), and every
   JS-driven animation below (choreography, count-up, tilt, scroll-reveal)
   branches on it explicitly -- the CSS @media guard in style.css handles
   the *styles*, this handles the *behavior* driving those styles.
   ------------------------------------------------------------------------ */

function prefersReducedMotion() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function easeOutCubic(t) {
  return 1 - Math.pow(1 - t, 3);
}

/** Animate a numeric value over `duration` ms with an eased curve,
 * calling onUpdate(currentValue) every frame. */
function animateValue(fromValue, toValue, duration, onUpdate, onComplete) {
  const start = performance.now();
  function frame(now) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    onUpdate(fromValue + (toValue - fromValue) * easeOutCubic(t));
    if (t < 1) {
      requestAnimationFrame(frame);
    } else if (onComplete) {
      onComplete();
    }
  }
  requestAnimationFrame(frame);
}

function setFieldError(name, message) {
  const input = fieldEl(name);
  const err = errorEl(name);
  if (!input || !err) return;
  if (message) {
    input.setAttribute("aria-invalid", "true");
    input.setAttribute("aria-describedby", name + "-error");
    err.textContent = message;
  } else {
    input.removeAttribute("aria-invalid");
    err.textContent = "";
  }
}

function validateField(name) {
  const rules = FIELD_RULES[name];
  const input = fieldEl(name);
  if (!rules || !input) return { valid: true };

  const raw = input.value;

  if (rules.type === "enum") {
    if (!raw) return { valid: false, message: "Please choose an option." };
    if (!rules.values.includes(raw)) return { valid: false, message: "Please choose a valid option." };
    return { valid: true, value: raw };
  }

  if (raw === "") return { valid: false, message: "This field is required." };

  const num = Number(raw);
  if (Number.isNaN(num)) return { valid: false, message: "Please enter a number." };

  if (rules.type === "int" && !Number.isInteger(num)) {
    return { valid: false, message: "Please enter a whole number." };
  }
  if (rules.strictPositive && num <= 0) {
    return { valid: false, message: "Must be greater than 0." };
  }
  if (rules.min !== undefined && num < rules.min) {
    return { valid: false, message: `Must be ${rules.min} or greater.` };
  }
  if (rules.max !== undefined && num > rules.max) {
    return { valid: false, message: `Must be ${rules.max} or less.` };
  }

  return { valid: true, value: num };
}

function validateAll() {
  let firstInvalid = null;
  const payload = {};

  for (const name of Object.keys(FIELD_RULES)) {
    const result = validateField(name);
    if (result.valid) {
      setFieldError(name, "");
      payload[name] = result.value;
    } else {
      setFieldError(name, result.message);
      if (!firstInvalid) firstInvalid = fieldEl(name);
    }
  }

  return { ok: !firstInvalid, payload, firstInvalid };
}

// Validate on blur for immediate feedback; clear the error as soon as the
// field becomes valid again while typing.
for (const name of Object.keys(FIELD_RULES)) {
  const input = fieldEl(name);
  if (!input) continue;
  input.addEventListener("blur", () => {
    const result = validateField(name);
    setFieldError(name, result.valid ? "" : result.message);
  });
  input.addEventListener("input", () => {
    if (input.getAttribute("aria-invalid") === "true") {
      const result = validateField(name);
      if (result.valid) setFieldError(name, "");
    }
  });
}

function mapServerErrorsToFields(detail) {
  if (!Array.isArray(detail)) return false;
  let mapped = false;
  for (const err of detail) {
    const loc = err.loc || [];
    const fieldName = loc[loc.length - 1];
    if (fieldName && FIELD_RULES[fieldName]) {
      setFieldError(fieldName, err.msg || "Invalid value.");
      mapped = true;
    }
  }
  return mapped;
}

/* ------------------------------------------------------------------------
   Form section scroll-in (IntersectionObserver)
   ------------------------------------------------------------------------ */

function setupScrollReveal() {
  const revealEls = document.querySelectorAll(".reveal");
  if (prefersReducedMotion() || !("IntersectionObserver" in window)) {
    revealEls.forEach((el) => el.classList.add("reveal--visible"));
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal--visible");
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );
  revealEls.forEach((el) => observer.observe(el));
}

/* ------------------------------------------------------------------------
   Card tilt micro-interaction (form sections + results card)
   ------------------------------------------------------------------------ */

function attachTilt(el, maxDeg) {
  let rafId = null;
  let pending = null;

  function apply() {
    rafId = null;
    if (!pending) return;
    el.style.transform = `perspective(800px) rotateX(${pending.rotX}deg) rotateY(${pending.rotY}deg)`;
  }

  el.addEventListener("mousemove", (event) => {
    const rect = el.getBoundingClientRect();
    const px = (event.clientX - rect.left) / rect.width - 0.5;
    const py = (event.clientY - rect.top) / rect.height - 0.5;
    pending = { rotX: -py * maxDeg, rotY: px * maxDeg };
    if (rafId === null) rafId = requestAnimationFrame(apply);
  });

  el.addEventListener("mouseleave", () => {
    pending = null;
    el.style.transform = "";
  });
}

function setupCardTilt() {
  if (prefersReducedMotion()) return;
  document.querySelectorAll(".section, .results-card").forEach((el) => attachTilt(el, 3.5));
}

/* ------------------------------------------------------------------------
   Weather visual: Three.js 3D scene, with a static-SVG fallback.

   The 3D scene is only ever initialized when the results view actually
   renders (called from showResults, never on page load), so it can never
   delay the form becoming usable. Three.js itself is loaded from a CDN via
   a dynamic import() rather than a classic <script src> tag: modern
   Three.js only ships as an ES module, so a plain script tag wouldn't
   expose a usable global -- dynamic import() is the zero-build equivalent
   and, as a bonus, is naturally lazy (nothing is fetched until called).
   ------------------------------------------------------------------------ */

const THREE_CDN_URL = "https://unpkg.com/three@0.169.0/build/three.module.min.js";
const THREE_LOAD_TIMEOUT_MS = 4000;

let threeModulePromise = null;
function loadThree() {
  if (!threeModulePromise) {
    threeModulePromise = import(THREE_CDN_URL);
  }
  return threeModulePromise;
}

function withTimeout(promise, ms) {
  return Promise.race([
    promise,
    new Promise((_, reject) => setTimeout(() => reject(new Error("Three.js load timed out")), ms)),
  ]);
}

function isWebGLAvailable() {
  try {
    const canvas = document.createElement("canvas");
    return !!(window.WebGLRenderingContext && (canvas.getContext("webgl2") || canvas.getContext("webgl")));
  } catch (e) {
    return false;
  }
}

function getComputedColor(varName) {
  const value = getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
  return value || "#888888";
}

let threeState = null;

function disposeThreeScene() {
  if (!threeState) return;
  if (threeState.animationId !== null) cancelAnimationFrame(threeState.animationId);
  threeState.scene.traverse((obj) => {
    if (obj.geometry) obj.geometry.dispose();
    if (obj.material) {
      if (Array.isArray(obj.material)) obj.material.forEach((m) => m.dispose());
      else obj.material.dispose();
    }
  });
  threeState.renderer.dispose();
  if (typeof threeState.renderer.forceContextLoss === "function") {
    threeState.renderer.forceContextLoss();
  }
  const canvas = threeState.renderer.domElement;
  if (canvas && canvas.parentNode) canvas.parentNode.removeChild(canvas);
  threeState = null;
}

function makeCloud(THREE, colorHex, baseX, baseY, baseZ, scale, opacity) {
  const group = new THREE.Group();
  const material = new THREE.MeshLambertMaterial({
    color: colorHex,
    // Always transparent (even at ~full opacity): the sun's glow sprite
    // is depth-tested off (see makeSunGlow) and relies on Three.js's
    // back-to-front distance sort of the transparent queue to end up
    // correctly painted UNDER any cloud in front of it. An opaque cloud
    // would render in the separate opaque pass instead, which happens
    // before the transparent pass regardless of z, and would incorrectly
    // let the glow paint over it.
    transparent: true,
    opacity: opacity === undefined ? 0.99 : opacity,
  });
  // A cloud built from a few overlapping soft spheres, then flattened --
  // smooth-shaded and blobby rather than a literal cartoon cloud outline.
  const puffs = [
    { x: 0, y: 0, r: 0.62 },
    { x: 0.55, y: 0.08, r: 0.5 },
    { x: -0.5, y: 0.05, r: 0.48 },
    { x: 0.15, y: 0.3, r: 0.42 },
  ];
  for (const puff of puffs) {
    const geometry = new THREE.SphereGeometry(puff.r, 16, 16);
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(puff.x, puff.y, 0);
    group.add(mesh);
  }
  group.scale.set(scale, scale * 0.72, scale * 0.85);
  group.position.set(baseX, baseY, baseZ);
  group.userData.baseX = baseX;
  group.userData.baseY = baseY;
  group.userData.baseZ = baseZ;
  return group;
}

/** A small tapered vertical streak (soft-edged, transparent at both ends)
 * used as the rain sprite texture -- reads as a falling streak rather
 * than a dot, closer to what the original SVG's <line> rain communicated. */
function createRainStreakTexture() {
  const canvas = document.createElement("canvas");
  canvas.width = 24;
  canvas.height = 96;
  const ctx = canvas.getContext("2d");
  const gradient = ctx.createLinearGradient(0, 0, 0, 96);
  gradient.addColorStop(0, "rgba(255,255,255,0)");
  gradient.addColorStop(0.2, "rgba(255,255,255,1)");
  gradient.addColorStop(0.8, "rgba(255,255,255,1)");
  gradient.addColorStop(1, "rgba(255,255,255,0)");
  ctx.fillStyle = gradient;
  ctx.beginPath();
  ctx.moveTo(9, 8);
  ctx.lineTo(15, 8);
  ctx.lineTo(15, 88);
  ctx.lineTo(9, 88);
  ctx.closePath();
  ctx.fill();
  return canvas;
}

function buildRain(THREE, colorHex) {
  const count = 55;
  const positions = new Float32Array(count * 3);
  const velocities = new Float32Array(count);
  for (let i = 0; i < count; i++) {
    positions[i * 3 + 0] = (Math.random() - 0.5) * 3.4;
    // Biased toward the lower half of the frame -- rain falling beneath
    // the clouds, not overlapping the cloud/sphere cluster itself.
    positions[i * 3 + 1] = Math.random() * 3 - 2.4;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 1.4 + 3.2; // clearly in front, near the clouds
    velocities[i] = 0.05 + Math.random() * 0.03;
  }
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  const texture = new THREE.CanvasTexture(createRainStreakTexture());
  // Mipmapping a small, high-contrast procedural texture like this blurs
  // the tapered streak into a soft grey blob at a distance -- disable it
  // and use plain linear filtering so the streak shape stays crisp.
  texture.generateMipmaps = false;
  texture.minFilter = THREE.LinearFilter;
  texture.magFilter = THREE.LinearFilter;
  const material = new THREE.PointsMaterial({
    map: texture,
    color: colorHex,
    size: 0.32,
    transparent: true,
    opacity: 0.85,
    sizeAttenuation: true,
    depthWrite: false,
  });
  const points = new THREE.Points(geometry, material);
  points.userData.velocities = velocities;
  return points;
}

function animateRain(points) {
  const positions = points.geometry.attributes.position.array;
  const velocities = points.userData.velocities;
  for (let i = 0; i < velocities.length; i++) {
    positions[i * 3 + 1] -= velocities[i];
    if (positions[i * 3 + 1] < -2.4) positions[i * 3 + 1] = 0.6;
  }
  points.geometry.attributes.position.needsUpdate = true;
}

/** Soft radial falloff used for the sun's outer glow -- an additive-blended
 * sprite behind/around the sphere so it reads as radiating light rather
 * than a flat painted disc. */
function createGlowTexture() {
  const canvas = document.createElement("canvas");
  canvas.width = 128;
  canvas.height = 128;
  const ctx = canvas.getContext("2d");
  const gradient = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
  gradient.addColorStop(0, "rgba(255,255,255,1)");
  gradient.addColorStop(0.35, "rgba(255,255,255,0.5)");
  gradient.addColorStop(1, "rgba(255,255,255,0)");
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, 128, 128);
  return canvas;
}

function makeSunGlow(THREE, colorHex, diameter) {
  const texture = new THREE.CanvasTexture(createGlowTexture());
  const material = new THREE.SpriteMaterial({
    map: texture,
    color: colorHex,
    transparent: true,
    opacity: 0.5,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    // Depth-testing this sprite against the sphere was unreliable even
    // with a large, confirmed world-space offset behind it (see git log
    // for the debugging trail) -- some quirk of this billboard/software
    // WebGL combination, not a straightforward near-plane precision
    // issue. The glow is a decorative halo, not a physically occluded
    // object, so disabling depth test outright is an acceptable trade:
    // opaque clouds drawn after it in the paint order still visually
    // cover it (see cloudGroup added after glow, below).
    depthTest: false,
  });
  const sprite = new THREE.Sprite(material);
  sprite.scale.set(diameter, diameter, 1);
  return sprite;
}

function buildWeatherScene(THREE, container, level) {
  const size = Math.max(Math.min(container.clientWidth || 220, 220), 120);

  const scene = new THREE.Scene();
  // near/far kept tight around the scene's actual depth range (roughly
  // 4-12 units from the camera) -- a much wider range like the classic
  // 0.1/100 default wastes almost all depth-buffer precision on space
  // nothing ever occupies, which was causing z-fighting between objects
  // that are clearly separated in world units (e.g. the glow sprite
  // behind the sun) but land in the same imprecise depth bucket.
  const camera = new THREE.PerspectiveCamera(35, 1, 1, 20);
  camera.position.set(0, 0, 9);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(size, size, false); // updateStyle=false: CSS (not Three.js) controls the rendered box size
  renderer.domElement.setAttribute("aria-hidden", "true");
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  container.appendChild(renderer.domElement);

  // Lower ambient + a moderate key light from upper-front + a dim fill
  // light from the opposite side: gives the sphere a real, visible
  // gradient (bright side -> soft falloff -> never-quite-black far side)
  // instead of the flat, evenly-lit look a strong ambient light produces.
  // (No renderer tone mapping: ACES desaturated the warm gold toward tan/
  // beige. Keeping intensities modest and letting the default clamp
  // handle the highlight preserves the actual accent hue better.)
  scene.add(new THREE.AmbientLight(0xffffff, 0.42));
  const keyLight = new THREE.DirectionalLight(0xffffff, 0.55);
  keyLight.position.set(3, 4, 6);
  scene.add(keyLight);
  const fillLight = new THREE.DirectionalLight(0xffffff, 0.18);
  fillLight.position.set(-4, -2, -3);
  scene.add(fillLight);

  // Sun: emissive MeshStandardMaterial (reads as a light source, not a
  // painted ball) plus an additive glow sprite for a soft radiating halo.
  const accentColor = new THREE.Color(getComputedColor("--color-accent"));
  const emissiveColor = accentColor.clone().lerp(new THREE.Color(0xffffff), 0.2);
  const sunRadius = 1.7;
  const sun = new THREE.Mesh(
    new THREE.SphereGeometry(sunRadius, 32, 32),
    new THREE.MeshStandardMaterial({
      color: accentColor,
      emissive: emissiveColor,
      emissiveIntensity: 0.55,
      roughness: 0.85,
      metalness: 0.05,
    })
  );
  scene.add(sun);

  const glow = makeSunGlow(THREE, "#" + emissiveColor.getHexString(), sunRadius * 3.4);
  // Offset behind the sphere's center (not exactly on it): a sprite at
  // precisely the same depth as the sphere z-fights against the sphere's
  // own silhouette (grazing-angle surface points sit at nearly the same
  // depth as the sprite there), which was killing the glow everywhere
  // except dead center. Sitting behind fixes that while still correctly
  // getting occluded by the sphere itself and by any cloud in front of it.
  glow.position.copy(sun.position);
  glow.position.z -= 0.5;
  scene.add(glow);

  const cloudGroup = new THREE.Group();
  scene.add(cloudGroup);

  const rain = buildRain(THREE, getComputedColor("--color-high-text"));
  rain.visible = false;
  scene.add(rain);

  // Clouds sit roughly halfway between the sun and the camera (not just
  // in front of it), scaled down to compensate for perspective growth at
  // that distance -- unambiguous depth separation instead of appearing
  // fused to the sphere's surface.
  const cloudZ = 4.2;
  if (level === "Moderate") {
    cloudGroup.add(makeCloud(THREE, getComputedColor("--color-moderate-fill"), 1.05, 0.6, cloudZ, 0.55));
    cloudGroup.add(makeCloud(THREE, getComputedColor("--color-moderate-bg"), -1.15, -0.45, cloudZ - 0.4, 0.5, 0.92));
  } else if (level === "High") {
    cloudGroup.add(makeCloud(THREE, getComputedColor("--color-high-fill"), 0, 0.55, cloudZ, 0.62));
    cloudGroup.add(makeCloud(THREE, getComputedColor("--color-high-text"), -1.5, -0.3, cloudZ - 0.5, 0.52, 0.94));
    cloudGroup.add(makeCloud(THREE, getComputedColor("--color-high-fill"), 1.45, -0.6, cloudZ + 0.3, 0.5, 0.96));
    rain.visible = true;
  }
  // Low ("Clear"): sphere alone, no clouds.

  let t = 0;
  let firstFrame = true;
  function animate() {
    t += 0.012;
    sun.rotation.y += 0.003;
    sun.position.y = Math.sin(t * 0.6) * 0.12;
    glow.position.copy(sun.position);
    glow.position.z -= 0.5;
    cloudGroup.children.forEach((cloud, i) => {
      cloud.position.x = cloud.userData.baseX + Math.sin(t * (0.3 + i * 0.07) + i) * 0.26;
      cloud.position.y = cloud.userData.baseY + Math.cos(t * (0.25 + i * 0.05) + i) * 0.14;
    });
    if (rain.visible) animateRain(rain);
    renderer.render(scene, camera);
    if (firstFrame) {
      firstFrame = false;
      // WebGL's first paint can lag a frame or two behind the JS call that
      // requested it (shader compilation, GPU submission -- more so under
      // software rendering). This flag lets anything that needs to know the
      // scene has genuinely painted at least once wait for a real signal
      // instead of guessing a timeout.
      container.dataset.weatherReady = "true";
    }
    threeState.animationId = requestAnimationFrame(animate);
  }

  threeState = { renderer, scene, camera, animationId: null };
  animate();
}

function renderStaticWeatherSVG(container, level) {
  const tplId =
    level === "Low" ? "weather-clear-tpl" : level === "Moderate" ? "weather-changeable-tpl" : "weather-stormy-tpl";
  const tpl = document.getElementById(tplId);
  if (tpl) container.appendChild(tpl.content.cloneNode(true));
  container.dataset.weatherReady = "true";
}

async function renderWeatherVisual(level) {
  const container = document.getElementById("results-visual");
  disposeThreeScene();
  container.innerHTML = "";
  delete container.dataset.weatherReady;

  const can3D = !prefersReducedMotion() && isWebGLAvailable();

  if (can3D) {
    try {
      const THREE = await withTimeout(loadThree(), THREE_LOAD_TIMEOUT_MS);
      buildWeatherScene(THREE, container, level);
      return;
    } catch (err) {
      // CDN unreachable, WebGL context creation failed, timed out, etc.
      // This is an enhancement layer -- fail silently into the SVG
      // fallback rather than surfacing an error anywhere.
      disposeThreeScene();
      container.innerHTML = "";
    }
  }

  renderStaticWeatherSVG(container, level);
}

/* ------------------------------------------------------------------------
   Results reveal choreography
   ------------------------------------------------------------------------ */

function setBarProgress(key, pct) {
  const fillEl = document.querySelector(`.confidence-bar__fill[data-fill="${key}"]`);
  const valueEl = document.querySelector(`.confidence-row__value[data-value="${key}"]`);
  if (fillEl) fillEl.style.width = pct + "%";
  if (valueEl) valueEl.textContent = pct.toFixed(1) + "%";
}

function runResultsChoreography(targets) {
  const visual = document.getElementById("results-visual");
  const headingGroup = document.getElementById("results-heading-group");
  const confidenceBlock = document.querySelector(".confidence");
  const cascadeItems = document.querySelectorAll(
    "#factor-list .cascade-item, #recommendation-list .cascade-item"
  );

  if (prefersReducedMotion()) {
    visual.classList.add("stage-visible");
    headingGroup.classList.add("stage-visible");
    confidenceBlock.classList.add("stage-visible");
    for (const key of ["Low", "Moderate", "High"]) setBarProgress(key, targets[key]);
    cascadeItems.forEach((el) => el.classList.add("stage-visible"));
    return;
  }

  // Reset (in case a previous result is still mid-sequence / being re-shown).
  visual.classList.remove("stage-visible");
  headingGroup.classList.remove("stage-visible");
  confidenceBlock.classList.remove("stage-visible");
  cascadeItems.forEach((el) => el.classList.remove("stage-visible"));
  for (const key of ["Low", "Moderate", "High"]) setBarProgress(key, 0);

  requestAnimationFrame(() => {
    setTimeout(() => visual.classList.add("stage-visible"), 0);
    setTimeout(() => headingGroup.classList.add("stage-visible"), 250);
    setTimeout(() => {
      confidenceBlock.classList.add("stage-visible");
      for (const key of ["Low", "Moderate", "High"]) {
        animateValue(0, targets[key], 800, (v) => setBarProgress(key, v));
      }
    }, 550);
    cascadeItems.forEach((el, i) => {
      setTimeout(() => el.classList.add("stage-visible"), 650 + i * 90);
    });
  });
}

function populateList(listId, items) {
  const list = document.getElementById(listId);
  list.innerHTML = "";
  for (const text of items || []) {
    const li = document.createElement("li");
    li.textContent = text;
    li.classList.add("cascade-item");
    list.appendChild(li);
  }
}

async function showResults(data) {
  const level = data.financial_stress_level;
  const copy = WEATHER_COPY[level] || { word: level, sub: "" };

  const heading = document.getElementById("results-heading");
  heading.textContent = copy.word;
  heading.setAttribute("data-level", level);

  document.getElementById("results-state-sublabel").textContent =
    `${copy.sub} (Classified as ${level} financial stress.)`;

  populateList("factor-list", data.contributing_factors);
  populateList("recommendation-list", data.recommendations);
  document.getElementById("results-disclaimer").textContent = data.disclaimer || "";

  formView.hidden = true;
  submitBar.hidden = true;
  resultsView.hidden = false;
  resultsView.scrollIntoView({ behavior: prefersReducedMotion() ? "auto" : "smooth", block: "start" });
  heading.focus?.();

  await renderWeatherVisual(level);

  const targets = {};
  for (const key of ["Low", "Moderate", "High"]) {
    targets[key] = Math.round((data.confidence[key] || 0) * 1000) / 10;
  }
  runResultsChoreography(targets);
}

startOverBtn.addEventListener("click", () => {
  disposeThreeScene();
  resultsView.hidden = true;
  formView.hidden = false;
  submitBar.hidden = false;
  formView.scrollIntoView({ behavior: prefersReducedMotion() ? "auto" : "smooth", block: "start" });
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  submitError.hidden = true;
  submitError.textContent = "";

  const { ok, payload, firstInvalid } = validateAll();
  if (!ok) {
    submitStatus.textContent = "Please fix the highlighted fields.";
    firstInvalid.focus();
    firstInvalid.scrollIntoView({ behavior: "smooth", block: "center" });
    return;
  }

  submitStatus.textContent = "";
  submitBtn.disabled = true;
  submitBtnLabel.textContent = "Checking…";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (response.status === 200) {
      const data = await response.json();
      await showResults(data);
    } else if (response.status === 422) {
      const body = await response.json();
      const mapped = mapServerErrorsToFields(body.detail);
      submitStatus.textContent = "Please fix the highlighted fields.";
      if (!mapped) {
        submitError.hidden = false;
        submitError.textContent = "Some of the submitted values weren't valid. Please review the form.";
      }
    } else {
      let detail = "Something went wrong while checking your financial weather. Please try again.";
      try {
        const body = await response.json();
        if (typeof body.detail === "string") detail = body.detail;
      } catch (_) {
        /* non-JSON error body, fall back to default message */
      }
      submitError.hidden = false;
      submitError.textContent = detail;
    }
  } catch (networkError) {
    submitError.hidden = false;
    submitError.textContent = "Couldn't reach the server. Please check your connection and try again.";
  } finally {
    submitBtn.disabled = false;
    submitBtnLabel.textContent = "Check my financial weather";
  }
});

setupScrollReveal();
setupCardTilt();
