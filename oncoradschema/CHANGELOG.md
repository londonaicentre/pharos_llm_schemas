# Changelog

## [0.5.0] - 2026-08-05 [EJ/JZ]

Arising from the PharosAI imaging schema review and the prompt-output discrepancy review.

### General structure changes

- **`DiseaseSpecificScore` → `SpecialtySpecificScore`.** May not have confirmed disease. Rename is a precondition for admitting ACR density.
- **`disease_specific_scores` lifted from `CancerStatus` to `OncoRadModel.specialty_specific_scores`.** Nesting forced cancer-status block open on patients with no cancer
- **`is_malignancy_identified` split into `is_malignancy_identified_on_scan` + `is_malignancy_suspected_on_scan`.** One boolean was being asked two questions (did this scan find cancer / did it find something not yet excluded)
- **`NonCancerFinding.is_cancer_lesion_related` → `is_cancer_related`.** Description broadened from findings caused by a lesion to caused by the cancer or its treatment, therefore including consequences such as radiotherapy skin thickening.

### Enum members added

- **`ScoringSystem.RCR`**: UK RCR 1–5, the NHS default scoring system, usually in place of BI-RADS. Highest-priority review item.
- **`ScoringSystem.ACR_BREAST_DENSITY`**: density is a property of background tissue, assigned on entirely normal breasts. Reuses the scores list.
- **`LesionMorphology.NON_MASS_ENHANCEMENT`**: a 28mm NME counted in the malignant footprint was landing in `non_cancer_findings.other`. Enum extended to non mass-shaped findings.
- **`ScanModality.TOMOSYNTHESIS`**: Now added. Previously collapsed to `MAMMOGRAPHY`/`OTHER`, making PharosAI ImagingType 005 unrecoverable.
- **`ScanRegion.AXILLA`**: axillary studies were extracting as `upper_limb`. Docstring records that the field answers what the scanner covered, not the requesting specialty: a standalone axillary study is `axilla` alone. Note - contrary to Pharos review expectation of `["breast"]` for reports 11/13. Breast should be raised from context, LLM inference has to be objective to content. 
  - `ScanRegion` states which anatomy the scanner covered — an observable fact of the study. The specialty context is also now carried per lesion by `associated_primary_cancer`.
- **`AnatomicalSite.LYMPH_NODE_INTERNAL_MAMMARY`**: previously missing nodal station.

### Fields added

- **`anatomical_subsite`** on `CancerLesion` and `NonCancerFinding`: no quadrant granularity existed and subsites were being smuggled into `anatomical_site_desc`.
- **`LesionSize.lesion_depth_mm`**: a mm measurement, so it belongs with the numerics. Kept organ-neutral.
- **`CancerLesion.is_index_lesion`**: index lesion was inferred downstream from `is_recist_target` or largest diameter, which may not match the report's own designation.
- **`ScanMetadata.image_quality_desc`** : quality had no home, referenced only indirectly via `RECIST NOT_EVALUABLE`. Free text only to avoid excessive schema extension.
- **`CancerLesion.associated_primary_cancer`**: `AnatomicalSite` records where a lesion is, never what it arose from. This inputs free text to carry varied disease (including those with no anatomical primary) without distortion.
- **`CancerLesion.characterisation_desc`** — `morphology`/`margin`/`shape`/`internal_features`/`uptake` collapse a descriptive sentence into five enums. Free text field scoped to appearance only.

### `ScanRationale`

- Split by **point in the care pathway**
- `DIAGNOSIS_OR_SCREENING` → `ROUTINE_SCREENING` + `DIAGNOSTIC_PRE_TREATMENT`;
- `POST_DIAGNOSIS_FOLLOW_UP` → `FOLLOW_UP`;
- `TREATMENT_PLANNING`, `INTERVENTIONAL`, `NOT_DETERMINABLE` retained.
- Screening/diagnostic collapse was unrecoverable: high-risk surveillance in a never-diagnosed patient was extracting as post-diagnosis follow-up.
- Have rejected proposed `ON_TREATMENT`/`POST_TREATMENT` split as one surveillance mammogram can be follow-up, on-treatment and post-treatment simultaneously, so a single-valued enum forces an arbitrary pick. Also frequently determinable only from clinical history.

## [0.1.0] - 2026-05-26

Initial schema design. Two-sibling finding hierarchy (`CancerLesion` / `NonCancerFinding`) as flat top-level lists; paired `<field>` + `<field>_desc` pattern throughout; top-level gate booleans; patient-level facts (RECIST response, disease scores) lifted off per-lesion records onto `CancerStatus`; `Topography` replaced by `AnatomicalSite` (radiology coordinates rather than patient-centric primary site);`LesionMargin` / `LesionShape` aligned to the BI-RADS lexicon; enum values normalised to snake_case.
