# SoilSense AI — Final Evaluation Submission Pack

Project ID: **26P_3CSE348**

Approved project title: **Soil Microbiome Recommendation Engine for Crop Rotation**

Team: Harsh Aryan, Murari Kumar, Palak Singh, Ashish Joshi

Guide: Confirm officially allotted name and email with faculty before submission.

## Page 1 — Project and Guide
- Project ID: 26P_3CSE348
- Title: Soil Microbiome Recommendation Engine for Crop Rotation
- Guide name/email: Verify against official allotment. Do not enter student email.
- Guide reviewed: Select Yes only if actually discussed.

## Page 2 — Mid-Term / Phase III

**Current Implementation / Prototype Status**

A client-side web prototype has been implemented using HTML, CSS, and JavaScript. It supports editable soil inputs, input validation, preset soil scenarios, 171 illustrative crop profiles, rule-based suitability scoring, crop search, category filters, and a responsive interface. The source code is hosted on GitHub and the prototype is deployed using GitHub Pages. Real soil microbiome data integration and trained machine learning models are not implemented.

**Design / Architecture & Validation**

The architecture consists of a web interface, numeric soil input validation, in-browser crop profile data, a rule-based suitability scoring function, and ranked recommendation rendering. The original crop library was expanded to 171 profiles, with many additional profiles based on category-level assumptions. JavaScript-level execution checks have been performed; complete mobile-browser and agronomic validation remain pending.

**Testing / Experimental Results So Far**

Five JavaScript-level simulated-DOM scenarios were exercised: default sample input, dry conditions, acidic conditions, invalid pH, and crop search. The default sample evaluated 171 profiles and displayed the top 20 ranked recommendations; invalid pH produced a validation error. These tests do not establish agricultural accuracy or verified live-browser compatibility. See TESTING.md.

**Major Challenges / Pending Work**

Complete mobile-browser testing, integrate a real soil microbiome dataset, develop and validate a data-driven recommendation model, establish scientifically meaningful crop profiles and units, and complete documentation and field-oriented evaluation.

## Page 3 — Phase III

**Implementation Completed**

A web-based academic prototype is implemented with input forms, validation, preset scenarios, 171 crop profiles, rule-based suitability scoring, ranked results, crop search, category filters, and GitHub Pages deployment. The microbiome analysis and machine learning components remain pending.

**Code / Hardware / System Integration Status**

HTML, CSS, and JavaScript components are integrated into a client-side application. No backend, database, external API, physical sensor, or trained ML model is connected. GitHub manages the source code and GitHub Pages hosts the static prototype.

**Testing, Validation & Performance Results**

Simulated-DOM JavaScript tests confirmed that the recommendation logic processed sample inputs and generated results for 171 profiles, with 20 initially displayed for performance. An invalid pH value of 20 triggered validation. Crop search filtered results for Tomato. No verified accuracy, latency, field-testing, or real mobile-browser benchmarks are available. See TESTING.md.

**Milestone Completion**

Partially completed (subject to the team's actual milestone plan and guide review).

**Pending Milestones**

Real microbiome dataset and ML integration, scientific calibration and evaluation, mobile browser end-to-end tests, final demonstration and documentation.

## Evidence links (one per line)

https://github.com/Jaash9090/Soil-microbiome-crop-erotation.

https://jaash9090.github.io/Soil-microbiome-crop-erotation./

https://github.com/Jaash9090/Soil-microbiome-crop-erotation./blob/main/TESTING.md

## Pages 4 and 5 — Declarations

Confirm only after checking that all information and evidence accurately reflect the team's actual progress and after discussing the submission with the project guide.

## Before submission

1. Verify official guide name and email.
2. Discuss progress and submission with guide.
3. Open the deployed website and test Analyze on the actual device; if broken, report this honestly.
4. Verify repository and evidence links are accessible to evaluators.
5. Submit only once per team for each evaluation stage.

**Scientific limitation:** This is an educational rule-based simulation, not a validated soil microbiome inference system. Suitability scores are not model accuracy percentages.
