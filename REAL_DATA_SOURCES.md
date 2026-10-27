# Verified public research data sources

## Integrated into website

- Peralta Lab / CropDiversity, `BDsoil_exptdesign.csv`, 36 field records, source: https://raw.githubusercontent.com/PeraltaLab/CropDiversity/master/data/BDsoil_exptdesign.csv
- Data fields include crop rotation, soil pH, soil texture, total carbon and total nitrogen.
- This is real experimental metadata, **not microbial sequencing counts** and not a crop-suitability label.

## Additional genuine microbiome data sources for further research

- USDA ARS, **Microbial community structure is affected by cropping sequences and poultry litter under long-term no-tillage**. Dataset DOI 10.15482/USDA.ADC/1503822, public CSV and data dictionary: https://catalog.data.gov/dataset/microbial-community-structure-is-affected-by-cropping-sequences-and-poultry-litter-under-l
- CA-SYS 16S rRNA study, OTU counts and metadata: https://pmc.ncbi.nlm.nih.gov/articles/PMC13320386/
- Crop rotation microbiome sequencing study: https://datadryad.org/dataset/doi:10.5061/dryad.tht76hf2x

## Not yet scientifically established

The existing crop classifier is trained on separate crop/soil data and **does not ingest microbial measurements**. Combining unrelated studies row-by-row would be scientifically invalid. A real microbiome-driven crop recommendation model requires matched samples with microbial profiles, soil conditions, and independent crop-outcome labels, then leakage-controlled evaluation.

## Browser testing

GitHub Pages deployment success only proves site publication. Actual Android/desktop user interaction and compatibility cannot be certified without a browser test. Use `AI_VALIDATION.md` checklist and record observations.
