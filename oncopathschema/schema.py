from enum import Enum

from pydantic import BaseModel, Field

# ENUMS


class Laterality(str, Enum):
    """Side of the body the specimen was taken from."""

    LEFT = "left"
    RIGHT = "right"
    BILATERAL = "bilateral"
    NOT_APPLICABLE = "not_applicable"


class AnatomicalSite(str, Enum):
    """Where the specimen was taken from.
    Use anatomical_site_name_desc and anatomical_subsite for detail."""

    OTHER = "other"
    UNKNOWN = "unknown"

    # Thoracic
    LUNG = "lung"
    PLEURA = "pleura"
    MEDIASTINUM = "mediastinum"
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
    COLON = "colon"
    RECTUM = "rectum"
    ANUS = "anus"

    # Peritoneal / retroperitoneal
    PERITONEUM = "peritoneum"
    OMENTUM = "omentum"
    RETROPERITONEUM = "retroperitoneum"

    # GU / pelvic
    BLADDER = "bladder"
    URETER = "ureter"
    RENAL_PELVIS = "renal_pelvis"
    URETHRA = "urethra"
    PROSTATE = "prostate"
    TESTIS = "testis"
    OVARY = "ovary"
    UTERUS = "uterus"
    CERVIX = "cervix"
    VULVA_VAGINA = "vulva_vagina"

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
    NASAL_CAVITY_SINUS = "nasal_cavity_sinus"
    THYROID = "thyroid"

    # Skin
    SKIN = "skin"

    # Bone / marrow / soft tissue (region carried by anatomical_subsite)
    BONE = "bone"
    BONE_MARROW = "bone_marrow"
    SOFT_TISSUE = "soft_tissue"

    # Lymph nodes (by nodal station)
    LYMPH_NODE_CERVICAL = "lymph_node_cervical"
    LYMPH_NODE_SUPRACLAVICULAR = "lymph_node_supraclavicular"
    LYMPH_NODE_AXILLARY = "lymph_node_axillary"
    LYMPH_NODE_INTERNAL_MAMMARY = "lymph_node_internal_mammary"
    LYMPH_NODE_MEDIASTINAL = "lymph_node_mediastinal"
    LYMPH_NODE_HILAR = "lymph_node_hilar"
    LYMPH_NODE_MESENTERIC = "lymph_node_mesenteric"  # includes mesocolic
    LYMPH_NODE_ABDOMINAL = "lymph_node_abdominal"
    LYMPH_NODE_RETROPERITONEAL = "lymph_node_retroperitoneal"
    LYMPH_NODE_PELVIC = "lymph_node_pelvic"
    LYMPH_NODE_INGUINAL = "lymph_node_inguinal"
    LYMPH_NODE_OTHER = (
        "lymph_node_other"  # station not listed; use anatomical_site_name_desc
    )


class MorphologyType(str, Enum):
    """Histological classification of the tumour."""

    UNKNOWN_MORPHOLOGY = (
        "unknown_morphology"  # explicitly stated that morphology unknown or uncertain
    )
    OTHER = "other"  # where unable to fit into any categories below

    # Carcinomas
    ADENOCARCINOMA = "adenocarcinoma"
    SQUAMOUS_CELL_CARCINOMA = "squamous_cell_carcinoma"
    UROTHELIAL_CARCINOMA = "urothelial_carcinoma"
    RENAL_CELL_CARCINOMA = "renal_cell_carcinoma"
    HEPATOCELLULAR_CARCINOMA = "hepatocellular_carcinoma"
    SMALL_CELL_CARCINOMA = "small_cell_carcinoma"
    BASAL_CELL_CARCINOMA = "basal_cell_carcinoma"
    CARCINOMA_OTHER = "carcinoma_other"
    CLEAR_CELL_CARCINOMA = "clear_cell_carcinoma"
    PAPILLARY_CARCINOMA = "papillary_carcinoma"
    CHROMOPHOBE_CARCINOMA = "chromophobe_carcinoma"
    ACINAR_CARCINOMA = "acinar_carcinoma"
    LARGE_CELL_CARCINOMA = "large_cell_carcinoma"
    MUCINOUS_CARCINOMA = "mucinous_carcinoma"
    SIGNET_RING_CELL_CARCINOMA = "signet_ring_cell_carcinoma"

    # Other Breast
    INVASIVE_CARCINOMA_NST = "invasive_carcinoma_nst"  # ductal/no special type
    INVASIVE_LOBULAR_CARCINOMA = "invasive_lobular_carcinoma"
    DCIS = "ductal_carcinoma_in_situ"
    LCIS = "lobular_carcinoma_in_situ"
    TUBULAR_CARCINOMA = "tubular_carcinoma"
    CRIBRIFORM_CARCINOMA = "cribriform_carcinoma"
    MEDULLARY_LIKE_CARCINOMA = "medullary_like_carcinoma"
    METAPLASTIC_CARCINOMA = "metaplastic_carcinoma"
    INVASIVE_MICROPAPILLARY_CARCINOMA = "invasive_micropapillary_carcinoma"
    INVASIVE_PAPILLARY_CARCINOMA = "invasive_papillary_carcinoma"
    INVASIVE_PLEOMORPHIC_LOBULAR_CARCINOMA = "invasive_pleomorphic_lobular_carcinoma"
    PHYLLODES = "phyllodes_tumour"
    ADENOID_CYSTIC_CARCINOMA = "adenoid_cystic_carcinoma"
    APOCRINE_CARCINOMA = "apocrine_carcinoma"

    # Mesothelioma
    MESOTHELIOMA = "mesothelioma"

    # Melanocytic
    MELANOMA = "melanoma"

    # Neuroendocrine
    NEUROENDOCRINE_TUMOUR = "neuroendocrine_tumour"
    NEUROENDOCRINE_CARCINOMA = "neuroendocrine_carcinoma"
    LARGE_CELL_NEUROENDOCRINE_CARCINOMA = "large_cell_neuroendocrine_carcinoma"

    # Sarcoma
    SARCOMA = "sarcoma"
    GIST = "gastrointestinal_stromal_tumour"
    LEIOMYOSARCOMA = "leiomyosarcoma"
    LIPOSARCOMA = "liposarcoma"

    # Lymphoma
    HODGKIN_LYMPHOMA = "hodgkin_lymphoma"
    DIFFUSE_LARGE_B_CELL_LYMPHOMA = "diffuse_large_b_cell_lymphoma"
    FOLLICULAR_LYMPHOMA = "follicular_lymphoma"
    MARGINAL_ZONE_LYMPHOMA = "marginal_zone_lymphoma"
    MANTLE_CELL_LYMPHOMA = "mantle_cell_lymphoma"
    T_CELL_LYMPHOMA = "t_cell_lymphoma"
    NON_HODGKIN_LYMPHOMA_OTHER = "non_hodgkin_lymphoma_other"

    # Other haematological
    LEUKAEMIA = "leukaemia"
    MULTIPLE_MYELOMA = "multiple_myeloma"
    MYELODYSPLASTIC = "myelodysplastic"

    # CNS
    GLIOMA = "glioma"
    ASTROCYTOMA = "astrocytoma"
    MENINGIOMA = "meningioma"

    # Germ cell
    GERM_CELL_TUMOUR = "germ_cell_tumour"


class InvasionStatus(str, Enum):
    """Whether the tumour finding is invasive or in-situ. A report describing both an
    invasive and an in-situ component is recorded as two separate findings;
    None where the finding is not a tumour."""

    INVASIVE = "invasive"
    IN_SITU_ONLY = "in_situ_only"  # e.g. pure DCIS, non-invasive papillary carcinoma
    NOT_ASSESSABLE = "not_assessable"  # e.g. cytology, superficial biopsy
    NOT_STATED = "not_stated"


class TumourNature(str, Enum):
    """Origin of the tumour at this specimen site.
    None where the finding is not a tumour."""

    PRIMARY = "primary"  # report states or concludes the tumour arose at this site
    METASTASIS = "metastasis"  # secondary deposit
    LOCAL_RECURRENCE = "local_recurrence"  # recurrence at or adjacent to a treated site
    NOT_STATED_UNCLEAR = "not_stated_unclear"


class Differentiation(str, Enum):
    """Degree of differentiation where reported in words rather than as a graded score.
    None where not stated."""

    WELL = "well"
    MODERATE = "moderate"
    POOR = "poor"
    UNDIFFERENTIATED = "undifferentiated"


class FeatureType(str, Enum):
    """Histological features explicitly stated for a finding, whether the finding is
    cancerous or not. Features the report does not mention are omitted."""

    OTHER = "other"

    # Prognostic / behavioural features
    LYMPHOVASCULAR_INVASION = "lymphovascular_invasion"  # small vessel invasion
    MACROVASCULAR_INVASION = "macrovascular_invasion"  # large-calibre vessel invasion
    PERINEURAL_INVASION = "perineural_invasion"
    NECROSIS = "necrosis"
    EXTRANODAL_EXTENSION = "extranodal_extension"  # extracapsular spread in a node
    TREATMENT_EFFECT = "treatment_effect"  # chemo/radiotherapy change, tumour bed
    MICROINVASION = (
        "microinvasion"  # invasive focus <1mm, usually in otherwise pure DCIS
    )
    INFLAMMATORY_INFILTRATE = (
        "inflammatory_infiltrate"  # inflammatory cell infiltrate present
    )

    # Non-cancerous histological findings
    DYSPLASIA = "dysplasia"
    ATYPIA = "atypia"
    METAPLASIA = "metaplasia"
    INFLAMMATION = "inflammation"
    FIBROSIS = "fibrosis"
    BENIGN_NEOPLASM = "benign_neoplasm"

    # Architectural patterns
    COMEDO_NECROSIS = "comedo_necrosis"
    CRIBRIFORM_ARCHITECTURE = "cribriform_architecture"
    SOLID_ARCHITECTURE = "solid_architecture"
    MICROPAPILLARY_ARCHITECTURE = "micropapillary_architecture"
    PAPILLARY_ARCHITECTURE = "papillary_architecture"


class FeatureStatus(str, Enum):
    """Whether the report explicitly states a feature to be
    present, absent, or possible."""

    PRESENT = "present"
    ABSENT = "absent"  # explicitly stated not identified / not seen
    POSSIBLE = "possible"  # described as possible, probable, suspicious or equivocal
    NOT_ASSESSABLE = "not_assessable"  # explicitly stated as not sampled/assessed


class MarginStatus(str, Enum):
    CLEAR = "clear"  # tumour does not reach the margin
    INVOLVED = "involved"  # tumour present at the margin
    CLOSE = "close"  # explicitly described as close but not involved
    NOT_ASSESSABLE = "not_assessable"
    NOT_STATED = "not_stated"


class FindingStatus(str, Enum):
    """What the finding is, and the certainty with which the report asserts it."""

    CANCEROUS = "cancerous"  # report asserts or positively assumes malignancy
    UNCERTAIN = "uncertain"
    # diagnosis and/or malignant potential is unresolved: possible, probable, query,
    NOT_CANCEROUS = "not_cancerous"
    # explicitly normal, confirmed negative finding, named benign/reactive finding


class TreatmentResponseStatus(str, Enum):
    """Response of the specimen to prior neoadjuvant therapy, where assessed.
    None where no prior therapy, or none assessed."""

    COMPLETE = "complete"  # no residual tumour (e.g. ypT0 ypN0)
    PARTIAL = "partial"
    STABLE = "stable"
    PROGRESSION = "progression"


class ScoreName(str, Enum):
    """Named staging, grading or prognostic scoring systems used in histopathology."""

    OTHER = "other"

    # Staging
    TNM_PATHOLOGICAL = "tnm_pathological"  # pT/pN/pM, including ypTNM
    TNM_CLINICAL = "tnm_clinical"  # cT/cN/cM where restated in the report
    AJCC_STAGE_GROUP = "ajcc_stage_group"  # I-IV group stage
    DUKES = "dukes"
    FIGO = "figo"
    ANN_ARBOR = "ann_arbor"  # lymphoma staging

    # Grading
    PATHOLOGICAL_GRADE = "pathological_grade"  # generic G1-G3/G4
    NOTTINGHAM = "nottingham"  # Nottingham/Bloom-Richardson breast grade
    GLEASON = "gleason"
    ISUP_GRADE_GROUP = "isup_grade_group"  # prostate grade group 1-5
    WHO_ISUP_NUCLEAR_GRADE = "who_isup_nuclear_grade"  # renal cell carcinoma
    IN_SITU_GRADE = "in_situ_grade"  # DCIS/LCIS low/intermediate/high

    # Depth / extent
    BRESLOW = "breslow"

    # Biopsy reporting categories
    BREAST_B_CATEGORY = "breast_b_category"  # B1-B5c
    CYTOLOGY_C_CATEGORY = "cytology_c_category"  # C1-C5

    # Prognostic / response indices
    NOTTINGHAM_PROGNOSTIC_INDEX = "nottingham_prognostic_index"
    LEIBOVICH = "leibovich"
    RESIDUAL_CANCER_BURDEN = "residual_cancer_burden"  # RCB 0/I/II/III
    TUMOUR_REGRESSION_GRADE = "tumour_regression_grade"


class BiomarkerType(str, Enum):
    """Gene or protein or other biomarker with therapeutic or prognostic significance."""

    OTHER = "other"

    # General
    BRAF = "braf"
    NTRK = "ntrk"
    RET = "ret"
    ERBB2_HER2 = "erbb2_her2"
    TP53 = "tp53"

    # DNA repair / mismatch repair
    BRCA1 = "brca1"
    BRCA2 = "brca2"
    MLH1 = "mlh1"
    MSH2 = "msh2"
    MSH6 = "msh6"
    PMS2 = "pms2"

    # Lung
    EGFR = "egfr"
    ALK = "alk"
    ROS1 = "ros1"
    MET = "met"
    KRAS = "kras"

    # Colorectal
    NRAS = "nras"

    # Breast
    PIK3CA = "pik3ca"
    ESR1_ER = "esr1_er"
    PGR_PR = "pgr_pr"
    KI67 = "ki_67"
    AR = "ar"  # androgen receptor

    # GIST / melanoma
    KIT = "kit"
    PDGFRA = "pdgfra"

    # Bladder / cholangiocarcinoma
    FGFR = "fgfr"

    # Glioma / cholangiocarcinoma
    IDH = "idh"

    # Other solid tumour
    PDL1 = "pdl1"

    # Neuro-oncology
    MGMT = "mgmt"

    # Haematological
    BCL2 = "bcl2"
    MYC = "myc"

    # Lineage markers that determine site of origin
    TTF1 = "ttf1"
    GATA3 = "gata3"
    PSA = "psa"

    # Aggregate genomic measures
    MSI = "msi"  # microsatellite instability
    MMR = "mmr"  # mismatch repair protein status
    TMB = "tmb"  # tumour mutational burden


class BiomarkerStatus(str, Enum):
    """Crude result of a biomarker test."""

    ALTERED = "altered"  # any alteration or positive expression
    NEGATIVE = "negative"  # explicit recording of negativity or normality
    EQUIVOCAL = "equivocal"
    # where explicitly stated borderline/indeterminate
    NOT_ASSESSABLE = "not_assessable"  # e.g. insufficient tumour cells / failed stain


class BiomarkerMethod(str, Enum):
    """None where not stated."""

    OTHER = "other"
    IMMUNOHISTOCHEMISTRY = "immunohistochemistry"
    FISH_ISH = "fish_ish"
    PCR = "pcr"
    SEQUENCING = "sequencing"


# BLOCKS


class PathologyScore(BaseModel):
    """A named staging, grading, or prognostic score reported for this finding."""

    score_name: ScoreName = Field(
        description="Named scoring system. Use OTHER if not in enum."
    )
    score_name_desc: str | None = Field(
        None, description="Name of the scoring system as described in the report"
    )
    score_value: str = Field(
        description="Direct extract of the value assigned (e.g. 'pT3a', '3 + 4 = 7', 'C1', 'B5b', '7/8', 'Intermediate (5)')"
    )


class Biomarker(BaseModel):
    """A single biomarker result, whether immunohistochemical or molecular, in the cells
    relevant to the finding (not background results mentioned separately by the report)"""

    biomarker: BiomarkerType = Field(
        description="Gene or protein biomarker. Use OTHER if not in enum."
    )
    biomarker_name_desc: str | None = Field(
        None, description="Name of the biomarker as described in the report"
    )
    biomarker_status: BiomarkerStatus = Field(
        description="Crude status of the marker in this finding's own cells, not in any other (e.g. background/reactive/non-neoplastic) cells"
    )
    method: BiomarkerMethod | None = Field(
        None, description="Test method used, if stated"
    )
    result_value: str | None = Field(
        None,
        description="Direct extract of the result as reported, including any alteration, expression level, score, percentage, assay or clone (e.g. 'Allred score = 7', 'score = 1+ (Negative)', '100% of tumour cells, Dako pharmDx 22C3')",
    )


class Feature(BaseModel):
    """A histological feature explicitly stated for a finding, and what the report
    said about it."""

    feature: FeatureType = Field(
        description="Histological feature. Use OTHER if not in enum."
    )
    feature_name_desc: str | None = Field(
        None, description="Name of the feature as described in the report"
    )
    feature_status: FeatureStatus = Field(
        description="Whether the report stated this feature to be present, absent, or possible"
    )


class Margin(BaseModel):
    """Status of surgical margin of a specimen as reported."""

    margin_status: MarginStatus = Field(
        description="Status of this margin. Record a margin only where the report characterises it."
    )
    distance_mm: float | None = Field(
        None, ge=0, description="Distance from tumour to this margin in mm, if stated"
    )
    margin_desc: str = Field(
        description="Direct extract naming and describing this margin (e.g. 'Circumferential: positive', 'Distal resection margin: clear, 15mm')"
    )


class SpecimenFinding(BaseModel):
    """A single noteworthy pathological observation described within a specimen"""

    is_lymph_node: bool = Field(
        description="True if this finding is a lymph node group (with or without tumour deposit) or tumour invading a lymph node; false for a finding elsewhere"
    )
    finding_status: FindingStatus = Field(
        description="What this finding is, and the certainty with which it is asserted"
    )
    finding_summary: str = Field(
        description="Short summary of this finding in your own words"
    )
    features: list[Feature] = Field(
        default_factory=list,
        description="Histological features explicitly stated for this finding, each with its reported status; empty if none stated",
    )

    # describing any tumour present; None throughout for a benign or normal finding
    morphology: MorphologyType | None = Field(
        None,
        description="Histological classification of the tumour. Use OTHER if not in enum. None where the finding is not a tumour.",
    )
    invasion_status: InvasionStatus | None = Field(
        None,
        description="Whether the tumour is invasive or in-situ only. Record an invasive and an in-situ component as two separate findings.",
    )
    tumour_nature: TumourNature | None = Field(
        None,
        description="Whether the tumour is primary at this site, a metastasis, or a recurrence, or if not stated or unclear.",
    )
    tumour_source: AnatomicalSite | None = Field(
        None,
        description="For a metastasis, the primary site the report states it originates from. Use OTHER if not in enum.",
    )
    tumour_source_desc: str | None = Field(
        None,
        description="Name of the primary site as described in the report (e.g. 'colorectal', 'upper GI')",
    )
    differentiation: Differentiation | None = Field(
        None,
        description="Degree of differentiation where described in words",
    )
    dimensions_desc: str | None = Field(
        None,
        description="Direct extract of the TUMOUR's own reported size only (e.g. '40x30x35mm', '2mm focus in a 14mm core'). Not the size of the specimen, container or cores received, and not a distance of spread. Count or ratio of nodes belong on Specimen.nodes_examined/nodes_positive.",
    )

    # results specific to this finding
    biomarkers: list[Biomarker] = Field(
        default_factory=list,
        description="Biomarker results reported for this finding; empty if none",
    )
    scores: list[PathologyScore] = Field(
        default_factory=list,
        description="Staging, grading and prognostic scores reported for this finding; empty if none",
    )


class Specimen(BaseModel):
    """A single specimen received and reported within the accession. Findings are
    nested under the specimen they belong to, so no cross-referencing labels are
    needed elsewhere in the schema."""

    anatomical_site: AnatomicalSite = Field(
        description="Anatomical site the specimen was taken from. Use OTHER if not in enum."
    )
    anatomical_site_name_desc: str = Field(
        description="Direct extract naming the specimen and its anatomical site (e.g. 'Recto-sigmoid resection', 'Urinary bladder, right lateral wall, tumour, TURBT')"
    )
    anatomical_subsite: str | None = Field(
        None,
        description="Location detail within the site (e.g. 'right lateral wall', 'left midzone', 'axillary')",
    )
    laterality: Laterality | None = Field(
        None, description="Laterality of the specimen"
    )
    procedure_desc: str | None = Field(
        None,
        description="Direct extract naming how the specimen was obtained (e.g. 'radical nephrectomy', 'TURBT', '4mm punch biopsy', 'slide review')",
    )
    is_sentinel: bool = Field(
        False,
        description="True if any node in this specimen was taken as a sentinel node (e.g. 'sentinel node x3')",
    )
    is_multifocal: bool = Field(
        False,
        description="True if two or more discrete tumour foci are described in the same quadrant/region of this specimen",
    )
    is_multicentric: bool = Field(
        False,
        description="True if two or more discrete tumour foci are described in different quadrants/regions of this specimen",
    )
    treatment_response: TreatmentResponseStatus | None = Field(
        None,
        description="Response of this specimen to prior neoadjuvant therapy, where the report assesses it",
    )
    nodes_examined: int | None = Field(
        None,
        ge=0,
        description="Total number of lymph nodes examined in this specimen, if stated",
    )
    nodes_positive: int | None = Field(
        None,
        ge=0,
        description="Total number of lymph nodes involved in this specimen, if stated",
    )
    findings: list[SpecimenFinding] = Field(
        default_factory=list,
        description="Noteworthy pathological observations described in this specimen, whatever their status; empty only if the report says nothing reportable about it",
    )
    margins: list[Margin] = Field(
        default_factory=list,
        description="Surgical margin statuses reported for this specimen; empty if none reported",
    )


# FINAL MODEL


class OncoPathModel(BaseModel):
    is_pathology_report: bool = Field(
        description="True only if the document is a histopathology or cytopathology report"
    )
    is_neoplastic_disease_identified: bool = Field(
        description="True if this report's findings assert, or raise unresolved suspicion of, malignant or in-situ neoplastic disease in any specimen. False for a benign or normal specimen."
    )
    clinical_indication: str | None = Field(
        None,
        description="Concise summary of the clinical details or indication given for the specimen",
    )
    specimens: list[Specimen] = Field(
        default_factory=list,
        description="Specimens described in this report; empty if not a pathology report",
    )
    report_summary: str | None = Field(
        None,
        description="Short free-text overall summary of the report; None if not a pathology report",
    )
