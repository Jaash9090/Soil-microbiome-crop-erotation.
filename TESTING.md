# SoilSense AI — Prototype Testing Evidence

Date: 27 October 2026

## Scope
Client-side HTML/CSS/JavaScript academic prototype with 171 illustrative crop profiles. These tests exercise JavaScript using a simulated DOM; they are **not** a real mobile-browser test or agronomic validation.

## Test observations
| Case | Inputs / action | Observed result | Status |
|---|---|---|---|
| Default sample | pH 6.8, N 50, P 45, K 55, moisture 55%, temperature 26 C, organic matter 2.5%, rainfall 650 mm | Recommendation function evaluated 171 crop profiles and rendered 20 ranked entries; button callback displayed completion message | Pass (simulated DOM) |
| Dry soil | Moisture 18%, rainfall 250 mm | Ranking generated; top illustrative match Chickpea | Pass (simulated DOM) |
| Acidic soil | pH 5.1 | Ranking generated | Pass (simulated DOM) |
| Invalid pH | pH 20 | Input validation showed an error and blocked analysis | Pass (simulated DOM) |
| Crop search | Search for Tomato | Filter rendered one matching crop | Pass (simulated DOM) |

## Limitations
- The suitability scores are *illustrative relative scores*, not accuracy percentages.
- Nutrient fields are relative indices; crop profiles are simplified and many additional crops use category-level defaults.
- Real soil microbiome data, trained ML model, backend/database and field validation are not integrated.
- End-to-end verification in actual mobile browsers and scientific dataset validation remain pending.
- The initial result list shows the top 20 ranked matches for mobile performance; crop search/filter can retrieve other matches.

## Links
- [Source repository](https://github.com/Jaash9090/Soil-microbiome-crop-erotation.)
- [Live academic prototype](https://jaash9090.github.io/Soil-microbiome-crop-erotation./)
