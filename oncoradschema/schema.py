from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


# ENUMS


class ScanModality(str, Enum):
    CT = "ct"
    MRI = "mri"
    PET = "pet"  # standalone PET (no co-registered CT/MRI)
    PET_CT = "pet_ct"
    PET_MRI = "pet_mri"
    SPECT = "spect"
    SPECT_CT = "spect_ct"
    SCINTIGRAPHY = "scintigraphy"  # planar nuclear medicine (e.g. whole-body bone scan)
    ULTRASOUND = "ultrasound"
    XRAY = "xray"
    FLUOROSCOPY = "fluoroscopy"
    MAMMOGRAPHY = "mammography"
    OTHER = "other"


class ScanContrast(str, Enum):
    WITHOUT_CONTRAST = "without_contrast"  # no contrast required or none given (e.g. non-contrast CT or scintigraphy)
    WITH_CONTRAST = "with_contrast"  # single phase
    DUAL_PHASE = "dual_phase"
    TRIPLE_PHASE = "triple_phase"


class ScanRegion(str, Enum):
    HEAD = "head"
    NECK = "neck"
    CHEST = "chest"
    ABDOMEN = "abdomen"
    PELVIS = "pelvis"
    SPINE = "spine"
    UPPER_LIMB = "upper_limb"
    LOWER_LIMB = "lower_limb"
    WHOLE_BODY = "whole_body"
    HEART = "heart"
    BREAST = "breast"
    VESSEL = "vessel"
    OTHER = "other"


class Laterality(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    BILATERAL = "bilateral"
    NOT_APPLICABLE = "not_applicable"


class ComparativeChange(str, Enum):
    """Explicit mention of change vs previous scan based on radiologist determination"""

    NEW = "new"
    PROGRESSIVE = "progressive"
    STABLE = "stable"
    IMPROVING = "improving"
    RESOLVED = "resolved"
    MIXED = "mixed"
    INDETERMINATE = "indeterminate"  # explicit statement that change cannot be assessed


class FormalRECISTResponse(str, Enum):
    """Formal RECIST 1.1 response. Only for explicit/measured RECIST."""

    COMPLETE_RESPONSE = "complete_response"  # disappearance of all target lesions
    PARTIAL_RESPONSE = "partial_response"  # ≥30% decrease in sum of diameters
    STABLE_DISEASE = "stable_disease"  # neither PR nor PD criteria met
    PROGRESSIVE_DISEASE = "progressive_disease"  # ≥20% increase or new lesions
    NOT_EVALUABLE = "not_evaluable"  # cannot assess — missing, artefact, wrong modality
    NOT_APPLICABLE = "not_applicable"  # not a target lesion / not a follow-up scan


class ScanRationale(str, Enum):
    DIAGNOSIS_OR_SCREENING = "diagnosis_or_screening"  # screening, initial workup, staging of known/suspected cancer
    TREATMENT_PLANNING = "treatment_planning"  # imaging to plan a treatment (e.g. pre-operative/surgical planning, radiotherapy planning)
    POST_DIAGNOSIS_FOLLOW_UP = "post_diagnosis_follow_up"  # any post-diagnosis scan: response assessment, surveillance, routine follow-up
    INTERVENTIONAL = "interventional"  # image-guided procedure / biopsy
    NOT_DETERMINABLE = "not_determinable"  # rationale not determinable from report


class ScoringSystem(str, Enum):
    OTHER = "other"
    TNM = "tnm"
    AJCC_STAGE = "ajcc_stage"
    BI_RADS = "bi_rads"
    PI_RADS = "pi_rads"
    FIGO = "figo"
    BOSNIAK = "bosniak"
    LI_RADS = "li_rads"
    LUNG_RADS = "lung_rads"
    TI_RADS = "ti_rads"
    O_RADS = "o_rads"
    DEAUVILLE = "deauville"
    GLEASON = "gleason"


class LesionStatus(str, Enum):
    CANCEROUS = (
        "cancerous"  # report asserts or positively assumes the lesion as cancerous
    )
    UNCERTAIN = "uncertain"  # described as possible, probable, query, indeterminate cancer lesion


class LesionNature(str, Enum):
    PRIMARY = "primary"  # confirmed primary tumour at this site
    METASTASIS = "metastasis"  # confirmed or strongly implied secondary
    NOT_STATED_UNCLEAR = "not_stated_unclear"  # not stated in report and unclear


class LesionMargin(str, Enum):
    """Edge transitions using BI-RADS lexicon"""

    CIRCUMSCRIBED_WELLDEFINED = "circumscribed_welldefined"
    MICROLOBULATED = "microlobulated"  # small undulations along margin
    OBSCURED = "obscured"  # margin hidden by superimposed tissue
    INDISTINCT_ILLDEFINED = "indistinct_illdefined"
    SPICULATED = "spiculated"  # radiating lines from mass


class LesionShape(str, Enum):
    """Silhouette descriptors using BI-RADS lexicon"""

    OVAL = "oval"  # elliptical
    ROUND = "round"  # spherical
    IRREGULAR = "irregular"  # non-uniform, no defining pattern
    LOBULATED = "lobulated"  # multiple smooth bulges, polycyclic


class LesionMorphology(str, Enum):
    """Tissue composition of a soft-tissue / parenchymal lesion.
    For bone lesions use internal_features (lytic / sclerotic) instead."""

    SOLID = "solid"
    CYSTIC = "cystic"
    MIXED_SOLID_CYSTIC = "mixed_solid_cystic"
    GROUND_GLASS_NODULE = "ground_glass_nodule"  # Fleischner description
    PART_SOLID_GROUND_GLASS = (
        "part_solid_ground_glass"  # Fleischner description (solid + ground-glass)
    )


class LesionInternalFeature(str, Enum):
    """
    Internal features of the lesion. Multi-valued.
    """

    NECROTIC = "necrotic"
    CALCIFIED = "calcified"
    HAEMORRHAGIC = "haemorrhagic"
    MUCINOUS = "mucinous"
    FAT_CONTAINING = "fat_containing"
    SCLEROTIC = "sclerotic"  # bone lesion composition
    LYTIC = "lytic"  # bone lesion composition


class LesionUptake(str, Enum):
    """Functional tracer uptake (PET / scintigraphy). None on purely anatomic imaging.
    Captures avidity only; does not imply malignancy (avid lesions may be benign)."""

    AVID = "avid"  # increased / abnormal tracer uptake
    NON_AVID = "non_avid"  # no significant tracer uptake
    EQUIVOCAL = "equivocal"  # low-grade / subtle / indeterminate uptake


class AnatomicalSite(str, Enum):
    OTHER = "other"
    UNKNOWN = "unknown"

    # Thoracic
    LUNG = "lung"
    PLEURA = "pleura"
    MEDIASTINUM = "mediastinum"
    HEART = "heart"
    CHEST_WALL = "chest_wall"

    # Abdominal solid organs
    LIVER = "liver"
    PANCREAS = "pancreas"
    SPLEEN = "spleen"
    GALLBLADDER = "gallbladder"
    BILE_DUCT = "bile_duct"
    KIDNEY = "kidney"
    ADRENAL = "adrenal"

    # GI tract
    OESOPHAGUS = "oesophagus"
    STOMACH = "stomach"
    SMALL_INTESTINE = "small_intestine"
    APPENDIX = "appendix"
    COLON = "colon"
    RECTUM = "rectum"
    ANUS = "anus"

    # Peritoneal / retroperitoneal
    PERITONEUM = "peritoneum"
    OMENTUM = "omentum"
    MESENTERY = "mesentery"
    RETROPERITONEUM = "retroperitoneum"

    # GU / pelvic
    BLADDER = "bladder"
    URETER = "ureter"
    PROSTATE = "prostate"
    TESTIS = "testis"
    OVARY = "ovary"
    UTERUS = "uterus"
    CERVIX = "cervix"

    # Breast
    BREAST = "breast"

    # CNS
    BRAIN = "brain"
    MENINGES = "meninges"
    SPINAL_CORD = "spinal_cord"

    # Head & neck
    ORAL_CAVITY = "oral_cavity"
    PHARYNX = "pharynx"
    LARYNX = "larynx"
    SALIVARY_GLAND = "salivary_gland"
    NASAL_CAVITY = "nasal_cavity"
    PARANASAL_SINUS = "paranasal_sinus"
    THYROID = "thyroid"

    # Bone (axial / appendicular)
    BONE_SKULL = "bone_skull"
    BONE_SPINE = "bone_spine"
    BONE_RIBS_STERNUM = "bone_ribs_sternum"
    BONE_PELVIS = "bone_pelvis"
    BONE_UPPER_LIMB = "bone_upper_limb"
    BONE_LOWER_LIMB = "bone_lower_limb"
    BONE_MARROW = "bone_marrow"

    # Soft tissue (by body region)
    SOFT_TISSUE_HEAD_NECK = "soft_tissue_head_neck"
    SOFT_TISSUE_THORAX = "soft_tissue_thorax"
    SOFT_TISSUE_ABDOMEN = "soft_tissue_abdomen"
    SOFT_TISSUE_PELVIS = "soft_tissue_pelvis"
    SOFT_TISSUE_UPPER_LIMB = "soft_tissue_upper_limb"
    SOFT_TISSUE_LOWER_LIMB = "soft_tissue_lower_limb"

    # Lymph nodes (by nodal station)
    LYMPH_NODE_CERVICAL = "lymph_node_cervical"
    LYMPH_NODE_SUPRACLAVICULAR = "lymph_node_supraclavicular"
    LYMPH_NODE_AXILLARY = "lymph_node_axillary"
    LYMPH_NODE_INTERNAL_MAMMARY = "lymph_node_internal_mammary"
    LYMPH_NODE_MEDIASTINAL = "lymph_node_mediastinal"
    LYMPH_NODE_HILAR = "lymph_node_hilar"
    LYMPH_NODE_ABDOMINAL = "lymph_node_abdominal"
    LYMPH_NODE_MESENTERIC = "lymph_node_mesenteric"
    LYMPH_NODE_PORTA_HEPATIS = "lymph_node_porta_hepatis"
    LYMPH_NODE_RETROPERITONEAL = "lymph_node_retroperitoneal"
    LYMPH_NODE_PELVIC = "lymph_node_pelvic"
    LYMPH_NODE_INGUINAL = "lymph_node_inguinal"

    # Vessels (commonly named in oncology radiology reports)
    VESSEL_AORTA = "vessel_aorta"
    VESSEL_IVC = "vessel_ivc"
    VESSEL_SVC = "vessel_svc"
    VESSEL_PORTAL_VEIN = "vessel_portal_vein"
    VESSEL_HEPATIC_VEIN = "vessel_hepatic_vein"
    VESSEL_HEPATIC_ARTERY = "vessel_hepatic_artery"
    VESSEL_SMA = "vessel_sma"
    VESSEL_SMV = "vessel_smv"
    VESSEL_SPLENIC_VEIN = "vessel_splenic_vein"
    VESSEL_RENAL_VEIN = "vessel_renal_vein"
    VESSEL_RENAL_ARTERY = "vessel_renal_artery"
    VESSEL_PULMONARY_ARTERY = "vessel_pulmonary_artery"
    VESSEL_CAROTID = "vessel_carotid"
    VESSEL_ILIAC = "vessel_iliac"
    VESSEL_OTHER = "vessel_other"


class NonCancerFindingType(str, Enum):
    """
    Mechanism-based taxonomy for clinically-impactful non-cancer findings.
    Paired with AnatomicalSite
    """

    OTHER = "other"
    THROMBUS = "thrombus"  # any in-situ clot or embolism (DVT, portal/IVC, PE, mural)
    ANEURYSM = "aneurysm"  # aneurysmal dilatation of a vessel
    DISSECTION = "dissection"  # intimal/wall dissection of a vessel
    STENOSIS_OCCLUSION = "stenosis_occlusion"  # non-embolic narrowing/occlusion
    ASCITES = "ascites"
    EFFUSION = "effusion"  # other serous fluid collection, e.g. pleural, pericardial, joint etc
    ACTIVE_HAEMORRHAGE = "active_haemorrhage"  # active bleeding
    HAEMATOMA = "haematoma"  # any blood collection
    ABSCESS_PUS_COLLECTION = "abscess_pus_collection"  # organised infected collection
    CYST_BENIGN_COLLECTION = (
        "cyst_benign_collection"  # simple cyst, seroma, lymphocoele
    )
    PNEUMOTHORAX_PNEUMOPERITONEUM = "pneumothorax_pneumoperitoneum"
    INFLAMMATION_INFECTION = "inflammation_infection"  # e.g. signs of pneumonia, colitis, cystitis, cholecystitis etc
    OBSTRUCTION_DILATATION = "obstruction_dilatation"  # bowel obstruction, hydronephrosis, biliary dilatation
    CALCULUS = "calculus"  # stones in any duct/cavity
    FIBROSIS_SCARRING = "fibrosis_scarring"  # e.g. ILD, radiation, chronic scar
    STEATOSIS_FATTY_CHANGE = "steatosis_fatty_change"  # hepatic/pancreatic fatty change
    ATROPHY = "atrophy"
    VOLUME_LOSS_COLLAPSE = "volume_loss_collapse"  # e.g. lung collapse
    FRACTURE = "fracture"  # any cortical break
    PERFORATION_RUPTURE = "perforation_rupture"  # bowel perforation, organ rupture
    HERNIATION = "herniation"  # any hernia, disc herniation
    DEGENERATIVE_CHANGE = "degenerative_change"


# BLOCKS


class ScanMetadata(BaseModel):
    modality: ScanModality = Field(description="Scan modality used")
    contrast: Optional[ScanContrast] = Field(
        None, description="Contrast usage for the scan"
    )
    regions: Optional[List[ScanRegion]] = Field(
        None, description="Anatomical regions captured by the scan"
    )


class DiseaseSpecificScore(BaseModel):
    scoring_system: ScoringSystem = Field(
        description="Structured scoring system. Use OTHER if not in enum."
    )
    scoring_system_name_desc: Optional[str] = Field(
        None, description="Name of scoring system as described in clinical text"
    )
    score_or_stage: str = Field(
        description="Score or stage assigned (e.g. 'T3bN1M0', 'PI-RADS 4', 'Category III', 'C')"
    )
    laterality: Optional[Laterality] = Field(
        None,
        description="Laterality the score applies to, if relevant",
    )
    score_desc: Optional[str] = Field(
        None, description="Direct extract of descriptive text for the score"
    )


class CancerStatus(BaseModel):
    overall_status: Optional[ComparativeChange] = Field(
        None,
        description="Radiologist's gestalt progression/response vs prior scan",
    )
    recist_response: Optional[FormalRECISTResponse] = Field(
        None,
        description=(
            "Formal whole scan RECIST 1.1 response. Populate ONLY when the report gives an "
            "explicit/measured RECIST response (a measured target-lesion sum or % change)."
        ),
    )
    progression_desc: Optional[str] = Field(
        None, description="Direct extract of descriptive text for overall progression"
    )
    disease_specific_scores: Optional[List[DiseaseSpecificScore]] = Field(
        None,
        description="Structured scoring/staging systems reported (e.g. TNM, BI-RADS, PI-RADS, Bosniak)",
    )


class LesionSize(BaseModel):
    longest_diameter_mm: Optional[float] = Field(
        None,
        ge=0,
        description="Longest reported diameter in mm (RECIST-relevant; non-nodal lesions)",
    )
    short_axis_mm: Optional[float] = Field(
        None,
        ge=0,
        description="Short-axis diameter in mm (lymph nodes, or any reported short-axis measurement)",
    )
    x_mm: Optional[float] = Field(None, ge=0, description="First reported axis in mm")
    y_mm: Optional[float] = Field(None, ge=0, description="Second reported axis in mm")
    z_mm: Optional[float] = Field(None, ge=0, description="Third reported axis in mm")
    volume_ml: Optional[float] = Field(
        None, ge=0, description="Volume in mL or cc if explicitly reported"
    )


class CancerLesion(BaseModel):
    """A single non-benign lesion (or a miliary presentation) at a given anatomical site.
    Only malignant or uncertain-malignancy lesions belong here. Unlikely lesions are excluded."""

    anatomical_site: AnatomicalSite = Field(description="Anatomical site of the lesion")
    anatomical_site_desc: Optional[str] = Field(
        None,
        description="Direct extract of descriptive text for the lesion's anatomical site",
    )
    lesion_status: LesionStatus = Field(
        description="Whether the report asserts the lesion as cancerous or uncertain"
    )
    change: Optional[ComparativeChange] = Field(
        None,
        description=(
            "General interval change of this lesion compared to prior scan."
        ),
    )
    laterality: Optional[Laterality] = Field(
        None, description="Laterality of the lesion"
    )
    size: Optional[LesionSize] = Field(None, description="Reported lesion dimensions")
    is_recist_target: bool = Field(
        False, description="True if designated a RECIST target lesion"
    )
    is_infiltrative: bool = Field(
        False,
        description="True if the lesion is described as actively invading or infiltrating adjacent tissue",
    )
    is_vascular_involvement: bool = Field(
        False,
        description="True if the lesion is described as invading a vessel or forming tumour thrombus",
    )
    is_miliary: bool = Field(
        False,
        description=(
            "True if the lesion is described as miliary (innumerable tiny nodules across an anatomy). "
        ),
    )
    nature: LesionNature = Field(
        description="Whether the lesion is a primary, metastasis, or not stated"
    )
    morphology: Optional[LesionMorphology] = Field(
        None,
        description="Tissue composition (anatomic imaging)",
    )
    internal_features: List[LesionInternalFeature] = Field(
        default_factory=list,
        description=(
            "Internal features described for the lesion. "
            "Multi-valued: include all features mentioned, empty if not characterised."
        ),
    )
    margin: Optional[LesionMargin] = Field(
        None,
        description="Edge appearance",
    )
    shape: Optional[LesionShape] = Field(
        None,
        description="Contour shape",
    )
    uptake: Optional[LesionUptake] = Field(
        None,
        description="Functional tracer uptake",
    )


class NonCancerFinding(BaseModel):
    finding: NonCancerFindingType = Field(
        description="Mechanism-based finding type. Use OTHER for findings not in the enum."
    )
    finding_desc: str = Field(
        description="Direct extract of descriptive text for the finding"
    )
    anatomical_site: AnatomicalSite = Field(
        description="Anatomical site of the finding"
    )
    anatomical_site_desc: Optional[str] = Field(
        None,
        description="Direct extract of descriptive text for the finding's anatomical site",
    )
    is_cancer_lesion_related: bool = Field(
        False,
        description="True if the finding is explicitly described as being related to a cancer lesion in the report (e.g. malignant biliary obstruction, tumour-related lobar collapse, pathological fracture, malignant effusion)",
    )


# FINAL MODEL


class OncoRadModel(BaseModel):
    is_radiology_report: bool = Field(
        description="True only if the document is a radiology report"
    )
    is_oncology_related: bool = Field(
        description="True only if the report concerns a patient being investigated for cancer"
    )
    is_malignancy_identified: bool = Field(
        description=(
            "True only if this scan identifies any malignant or uncertain-malignancy lesion"
        ),
    )
    scan_metadata: Optional[ScanMetadata] = Field(
        None,
        description="Scan-level metadata; None if not a radiology report",
    )
    scan_rationale: Optional[ScanRationale] = Field(
        None,
        description="Rationale for the scan (diagnosis/screening, post-diagnosis follow-up, interventional)",
    )
    cancer_status: Optional[CancerStatus] = Field(
        None,
        description="Patient-level cancer status summary; None if not oncology related",
    )
    cancer_lesions: Optional[List[CancerLesion]] = Field(
        None,
        description="Malignant or uncertain-malignancy lesions described in the report; exclude clearly benign findings",
    )
    non_cancer_findings: Optional[List[NonCancerFinding]] = Field(
        None, description="Other non-cancer findings described in the report"
    )
    report_summary: Optional[str] = Field(
        None,
        description="Short free-text overall summary of the report; None if not a radiology report",
    )
