# ============================================================
# conditions.py
# All genetic conditions that BillionToOne tests for,
# matched to their actual Unity and Northstar products.
# ============================================================

CONDITIONS = {
    "Sickle Cell Disease (HBB)": {
        "gene": "HBB",
        "product": "Unity Complete",
        "analogy": (
            "Think of red blood cells like round delivery trucks carrying oxygen. "
            "In sickle cell disease, those trucks are bent into crescent shapes — "
            "they get stuck in small blood vessels and can't deliver oxygen properly."
        ),
        "inheritance": "Autosomal recessive",
        "counseling_note": (
            "Both parents must carry one copy for a child to be affected. "
            "A carrier is completely healthy but can pass the gene to children."
        ),
    },
    "Cystic Fibrosis (CFTR)": {
        "gene": "CFTR",
        "product": "Unity Complete",
        "analogy": (
            "The CFTR gene controls a tiny 'gate' that manages salt and water in cells. "
            "When the gate doesn't work, thick sticky mucus builds up — mostly in the "
            "lungs and digestive system — making it hard to breathe and digest food."
        ),
        "inheritance": "Autosomal recessive",
        "counseling_note": (
            "Being a carrier means you have one working copy and are completely healthy. "
            "Only children who inherit two non-working copies are affected."
        ),
    },
    "Spinal Muscular Atrophy (SMN1)": {
        "gene": "SMN1",
        "product": "Unity Complete",
        "analogy": (
            "SMN1 makes a protein that keeps motor neurons — the nerve cells that tell "
            "your muscles to move — alive and healthy. Without enough of this protein, "
            "those nerve cells gradually weaken, affecting movement and strength."
        ),
        "inheritance": "Autosomal recessive",
        "counseling_note": (
            "SMA is rare but serious. Early detection allows early treatment planning — "
            "and treatments have improved significantly in recent years."
        ),
    },
    "Trisomy 21 / Down Syndrome": {
        "gene": "Chromosome 21",
        "product": "Unity Complete",
        "analogy": (
            "Usually people have two copies of each chromosome — like two volumes of "
            "a book. In Down syndrome, there is an extra copy of chromosome 21, "
            "like having a third volume. This extra copy changes how the body and "
            "brain develop."
        ),
        "inheritance": "Chromosomal (not inherited in most cases)",
        "counseling_note": (
            "This is a screening result, not a final diagnosis. "
            "Confirmatory diagnostic testing (like amniocentesis) is available "
            "if you want to know for certain."
        ),
    },
    "Trisomy 18 / Edwards Syndrome": {
        "gene": "Chromosome 18",
        "product": "Unity Complete",
        "analogy": (
            "Similar to Down syndrome, Trisomy 18 means there is an extra copy of "
            "chromosome 18. This extra genetic material significantly affects how "
            "the body develops during pregnancy."
        ),
        "inheritance": "Chromosomal (not inherited in most cases)",
        "counseling_note": (
            "This is a screening result. Your provider will discuss confirmatory "
            "testing and next steps with you. Genetic counseling is strongly recommended."
        ),
    },
    "BRCA1 / BRCA2 — Hereditary Breast & Ovarian Cancer": {
        "gene": "BRCA1 / BRCA2",
        "product": "Northstar Select",
        "analogy": (
            "BRCA1 and BRCA2 are like the body's repair crew for damaged DNA. "
            "Every day your cells get small amounts of damage — normally the crew "
            "fixes it fast. A change in BRCA means the repair crew is less efficient, "
            "so damage can build up over time, raising cancer risk."
        ),
        "inheritance": "Autosomal dominant",
        "counseling_note": (
            "Having a BRCA variant raises risk but does NOT mean cancer is certain. "
            "Many people with BRCA variants never develop cancer. "
            "Screening and prevention options are available."
        ),
    },
    "TP53 — Li-Fraumeni Syndrome": {
        "gene": "TP53",
        "product": "Northstar Select",
        "analogy": (
            "TP53 is called the 'guardian of the genome.' It acts like a quality "
            "control inspector on a factory floor — stopping damaged products from "
            "leaving the line. When TP53 is altered, that inspector is less effective, "
            "and damaged cells are more likely to grow unchecked."
        ),
        "inheritance": "Autosomal dominant",
        "counseling_note": (
            "TP53 variants are significant and a referral to a cancer genetics "
            "specialist is strongly recommended. Enhanced surveillance can catch "
            "problems early when they are most treatable."
        ),
    },
    "EGFR — Lung Cancer Mutation": {
        "gene": "EGFR",
        "product": "Northstar Select",
        "analogy": (
            "EGFR is like an on/off switch on the surface of cells that tells them "
            "when to grow. In some lung cancers, this switch gets stuck in the 'on' "
            "position, causing uncontrolled growth. Knowing about this specific "
            "mutation helps doctors choose targeted therapies."
        ),
        "inheritance": "Somatic (acquired, not inherited)",
        "counseling_note": (
            "An EGFR mutation in a tumor is not inherited and cannot be passed to "
            "children. It is important for treatment selection — targeted therapies "
            "exist specifically for EGFR-positive tumors."
        ),
    },
}

RESULT_TYPES = [
    "Low risk — no variant detected",
    "Carrier detected (one copy — patient is healthy)",
    "High risk — variant detected (two copies affected)",
    "Positive — variant detected in tumor",
    "Inconclusive — further testing recommended",
    "Test failed — redraw required",
]

LANGUAGES = [
    "English",
    "Spanish",
    "French",
    "Mandarin Chinese",
    "Hindi",
    "Arabic",
    "Portuguese",
    "Tagalog",
    "Vietnamese",
    "Korean",
]
