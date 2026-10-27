# Dataset-trained crop model — measured evaluation

- Source dataset: https://github.com/KRUTHIKTR/Crop-Recommendation-System-Using-Machine-Learning/blob/main/Datasets/crop_data1.csv
- Observations parsed: 2200; crops: 22
- Features: N, P, K, temperature, relative humidity, pH, rainfall
- Method: standardized nearest-class-centroid classifier; each class split by row order (every fourth row test; remaining training)
- Training rows: 1650
- Held-out rows: 550
- Correct held-out predictions: 476
- **Measured internal holdout accuracy: 86.55%**
- This is NOT an external field validation or a microbiome-based crop rotation model.
- Source data is described as assembled/augmented, not necessarily independently measured farm samples.
- Potential bias: class-ordered records and deterministic split; potential repeated/augmented samples across partitions.
- For scientific claims: acquire genuine independent crop/microbiome data, assess provenance, run grouped or external validation and evaluate crop-rotation outcomes.
- The browser predictor loads `crop_model.json` and uses its fitted centroids; it does not need a backend.
