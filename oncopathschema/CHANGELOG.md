# Changelog

## [0.5.0] - 2026-09-14 [EJ/JZ]

Arising from the PharosAI pathology schema review (JB, 2026-09-02).

### General structure changes

- **`CancerSpecimenFinding` -> `SpecimenFinding`.** No longer restricted to confirmed/suspected cancer to avoid excluding borderline and explicitly negative cases. `Specimen.findings` now holds all noteworthy observations.
- **`FindingStatus` gains `NOT_CANCEROUS`** (was `CANCEROUS` / `UNCERTAIN` only). Covers named benign/reactive findings, explicitly normal results, and confirmed-negative results (negative sentinel node, complete pathological response) which were previously unrecordable.
- **`GeneralSpecimenFeature` merged into `FeatureType`.** Single feature vocabulary removes arbitrary and potentially incorrect splits.
- **`features` becomes `list[Feature]`** (`feature` + `FeatureStatus`: PRESENT / ABSENT / POSSIBLE / NOT_ASSESSABLE). A feature is recorded only if the report explicitly addresses it to allow capture of explicit absence.
- **`FeatureType` gains** `COMEDO_NECROSIS`, `CRIBRIFORM_ARCHITECTURE`, `SOLID_ARCHITECTURE`, `MICROPAPILLARY_ARCHITECTURE`, `PAPILLARY_ARCHITECTURE`.
- **`is_oncology_related` removed, `is_malignancy_identified_on_specimen` -> `is_neoplastic_disease_identified`.** `is_oncology_related` depended on clinical details that might not be present resulting in false negatives. The remaining flag now scoped to enabling flagging of borderline cases, also avoiding false negatives.
- **Enum members removed**: `InvasionStatus.INVASIVE_AND_IN_SITU` (findings are treated as atomic units, so invasive and an in-situ component can be separated); `BiomarkerStatus.HYPOTHETICAL` (pending tests are no longer extracted to prevent noise); `FeatureType.NORMAL_UNREMARKABLE` (an unremarkable specimen does not get reported); and `FindingFeature.MULTIFOCAL` / `MULTICENTRIC` now changed to specimen level flags `Specimen.is_multifocal` / `is_multicentric`).
- **`FeatureType` gains `MACROVASCULAR_INVASION`**, to separate large-calibre vessel invasion (e.g. renal vein, extramural/EMVI) in addition to `LYMPHOVASCULAR_INVASION`.
- **`NOT_STATED` removed where the field is optional** (`TreatmentResponseStatus`, `Differentiation`, `BiomarkerMethod`) - use `None` instead.

### Fields added

- **`Specimen.is_sentinel: bool`**: true if any node in the specimen was taken as a sentinel (e.g. "sentinel node x3").
- **`Specimen.is_multifocal` / `is_multicentric: bool`**: two or more discrete tumour foci in the same, or different, quadrant/region of the specimen as a specimen-wide signal
- **`Specimen.treatment_response: TreatmentResponseStatus | None`**: response to prior therapy (`COMPLETE` / `PARTIAL` / `STABLE` / `PROGRESSION`), at specimen level.
- **`Feature.feature_name_desc: str | None`**: name of the feature as described in the report, for use when `feature = OTHER`. Brings `Feature` in line with `Biomarker`/`PathologyScore`/`AnatomicalSite`, which already carry a `*_name_desc` free-text companion
- **`SpecimenFinding.tumour_source: AnatomicalSite | None`**: the primary site the report states or concludes it originates from, useful for metastases
- **`SpecimenFinding.tumour_source_desc: str | None`**: name of the primary site as described in the report

### Domain rules / prompt changes

- A finding now recorded for any noteworthy observation - cancer, benign, or a confirmed-negative result (an entirely unremarkable specimen can remain null).
- Biomarkers are extracted only once confirmed (pending/awaited test no longer recorded).
- Biomarker status is pinned to this finding's own cell population, to avoid false positives from background populations. 
- Margins: state margin identity and distance_mm only where explicitly stated, do not infer.
- PII is excluded, not tokenised. Identifiers are omitted or rephrased around so the clinical meaning survives; no placeholder token is emitted, including inside direct extracts.

### Pharos feedback deferred or rejected

- Primary constraint is schema being at limit of complexity.
- Rejected a dedicated `BORDERLINE_MALIGNANT_POTENTIAL` status and an IHC/ISH pending-result split: both asked the model to infer, or draw a distinction in an edge case. Folded into `UNCERTAIN` / `NOT_CANCEROUS`, and into "only extract confirmed results", respectively.
- Full neoadjuvant block not added, `ScoreName` carries `RESIDUAL_CANCER_BURDEN` / `TUMOUR_REGRESSION_GRADE`.
- Numeric size fields, structured TNM, structured margin identity (a `margin_name` enum) - kept as free text per MESA conventions for fields that require disambiguation, but subsequently easy to parse (precision / recall trade off); resolved instead by a prompt rule against inferring status/distance not in the text.
- Biomarker germline/somatic origin not added as considered to be an edge case, not worth additional schema surface.
