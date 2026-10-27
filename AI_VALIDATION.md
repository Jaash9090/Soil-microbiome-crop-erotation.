# Data-driven AI and Validation Plan

## What is actually implemented
- `train_model.py`: a reproducible scikit-learn Random Forest classifier training and 25% stratified holdout evaluation pipeline for **real labelled crop data** supplied by the user.
- `requirements-ml.txt`: Python dependencies.
- `microbiome.html`: microbial abundance CSV analysis with Shannon, Gini-Simpson, richness and evenness.
- `index.html`: browser-based **rule-based** crop suitability simulation, not the trained model.

## How to run training
1. Obtain a legitimate dataset with observed crop labels and at least two columns named among `ph,n,p,k,moisture,temp,organic,rainfall`. Check dataset provenance, units, license, label meaning, and class counts.
2. `pip install -r requirements-ml.txt`
3. `python train_model.py --csv your_real_dataset.csv --target crop`
4. Inspect generated `model_report.json` for holdout accuracy, per-class precision/recall/F1 and confusion matrix.

**No real dataset is bundled, no model has yet been trained, and no measured accuracy is claimed.** The script will not run without a user-supplied real dataset.

## Important methodological limits
A crop label is not proof of agronomic suitability or crop-rotation benefit. Train/test splitting by row can overestimate performance when farms, locations, years, or repeated observations overlap. For credible scientific validation, source independently collected samples, check leakage, apply farm/time-based splits where appropriate, compare baseline models, and evaluate on external datasets. Microbiome features require real measurements with verified sample metadata; the diversity calculator alone is not a trained microbiome-based crop predictor.

## Browser test checklist (manual, real devices)
- Open homepage and verify it loads without console errors.
- Run the Analyze button with default inputs and confirm recommendations update.
- Change pH to 20 and confirm validation prevents recommendations.
- Search for Tomato and verify filtered results.
- Open microbiome.html; paste `taxon,abundance\nA,10\nB,10` and confirm richness=2, Shannon≈0.6931, Gini–Simpson=0.5, evenness=1.
- Upload a valid CSV and confirm results; try invalid/negative abundance and confirm error.
- Repeat on Android Chrome and desktop browser, record device, browser version, date, screenshots, and failures.

Do not mark the checklist completed without performing the browser tests.
