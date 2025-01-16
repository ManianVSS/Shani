// JavaScript implementation of CHISQ.INV.RT
export function chisqInvRt(p, df) {
  if (p <= 0 || p > 1) {
    throw new Error("Probability p must be in the range (0, 1].");
  }
  if (df <= 0) {
    throw new Error("Degrees of freedom df must be positive.");
  }

  // Chi-squared CDF
  function chisqCDF(x, k) {
    if (x < 0) return 0;
    return gammaLowerIncomplete(k / 2, x / 2) / gamma(k / 2);
  }

  // Incomplete gamma function (lower)
  function gammaLowerIncomplete(s, x) {
    let sum = 0;
    let term = 1 / s;

    for (let n = 0; n < 100; n++) {
      sum += term;
      term *= x / (s + n + 1);
      if (term < 1e-10) break;
    }
    return Math.pow(x, s) * Math.exp(-x) * sum;
  }

  // Gamma function
  function gamma(z) {
    const g = 7;
    const p = [
      0.99999999999980993, 676.5203681218851, -1259.1392167224028,
      771.32342877765313, -176.61502916214059, 12.507343278686905,
      -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
    ];

    if (z < 0.5) {
      return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
    }

    z -= 1;
    let x = p[0];
    for (let i = 1; i < g + 2; i++) {
      x += p[i] / (z + i);
    }

    const t = z + g + 0.5;
    return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
  }

  // Newton-Raphson method to find the inverse
  let x = df; // Initial guess
  for (let i = 0; i < 100; i++) {
    const error = chisqCDF(x, df) - (1 - p);
    const derivative = (chisqCDF(x + 1e-5, df) - chisqCDF(x, df)) / 1e-5;
    const newX = x - error / derivative;

    if (Math.abs(newX - x) < 1e-10) return newX;
    x = newX;
  }

  throw new Error("Failed to converge.");
}

// Example usage
const p = 0.09999999999999998; // Right-tailed probability
const df = 6; // Degrees of freedom
// console.log(chisqInvRt(p, df));
