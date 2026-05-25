# 🧬 Unity / Northstar — Patient Result Plain-Language Explainer

A demo tool built for **BillionToOne's** genetic counseling workflow.

Genetic counselors enter a patient's Unity or Northstar test result,
and the tool instantly generates a warm, plain-language explanation —
personalized for the patient, in their language  ready to print or email.

---

## The Problem This Solves

BillionToOne's Unity and Northstar reports are written for clinicians.
A pregnant patient who sees terms like *"heterozygous carrier"*,
*"autosomal recessive"*, or *"residual risk 1:4,200"* often panics
or misunderstands their result entirely.

Genetic counselors currently spend significant time on post-result calls
explaining the same concepts repeatedly. This tool handles that first-pass
explanation automatically — freeing up counselor time while improving
patient understanding.

---

## What It Does

1. Counselor selects the **condition**, **result type**, and **risk number**
2. Selects the **patient's preferred language** (10 languages supported)
3. Clicks **Generate** — the tool produces a warm, plain-language explanation
   in ~3-5 seconds using **Llama 3.3** (open-source, Meta) via **Groq**
4. Counselor downloads a **printable PDF card** to share with the patient

---

## Conditions Supported

Matched to BillionToOne's actual product lines:

| Condition | Gene | Product |
|---|---|---|
| Sickle Cell Disease | HBB | Unity Complete |
| Cystic Fibrosis | CFTR | Unity Complete |
| Spinal Muscular Atrophy | SMN1 | Unity Complete |
| Trisomy 21 / Down Syndrome | Chromosome 21 | Unity Complete |
| Trisomy 18 / Edwards Syndrome | Chromosome 18 | Unity Complete |
| Hereditary Breast & Ovarian Cancer | BRCA1/2 | Northstar Select |
| Li-Fraumeni Syndrome | TP53 | Northstar Select |
| Lung Cancer Mutation | EGFR | Northstar Select |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web interface |
| Groq API | AI inference (free, fast) |
| Llama 3.3 70B | Open-source LLM by Meta |
| fpdf2 | PDF generation |

---

## Setup Instructions

### Step 1 — Get a free Groq API key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up with your Google or GitHub account (free)
3. Click **API Keys** → **Create API Key**
4. Copy your key (it starts with `gsk_...`)

### Step 2 — Download this project
```bash
git clone https://github.com/negiayushi/unity-explainer.git
cd unity-explainer
```

### Step 3 — Install the required libraries
```bash
pip install -r requirements.txt
```

### Step 4 — Set your API key

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=gsk_your_key_here
```

**Mac / Linux (Terminal):**
```bash
export GROQ_API_KEY=gsk_your_key_here
```

### Step 5 — Run the app
```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`

---

## Project Structure

```
unity-explainer/
├── app.py           ← Main web interface (Streamlit)
├── conditions.py    ← Database of conditions, genes, and analogies
├── explainer.py     ← Calls Groq API to generate the explanation
├── report.py        ← Generates the printable PDF card
├── requirements.txt ← List of Python libraries needed
├── .gitignore       ← Prevents secrets from being uploaded
└── README.md        ← This file
```

---

## Example Output

**Input:** Maria | Sickle Cell Disease | Carrier detected | 1 in 4 | English

**Output (in English):**

>  GREETING
Maria, I'm so glad we could talk about your test results today, and I want to start by saying that everything
looks very positive for you.
>
> WHAT YOUR RESULT MEANS
Your test results show that you are at low risk for Sickle Cell Disease, which is great news. This means that
we didn't find any changes in your genes that would suggest you have the disease. You can feel reassured
by this result, and we can talk more about what it means for you and your family
...

---

## Why Open-Source AI?

This demo uses **Llama 3.3** (Meta) via Groq — not a proprietary model.
This means:
- No ongoing licensing fees for BillionToOne
- Patient explanation text is not stored by a third party
- The model can be run fully locally for maximum privacy (see Ollama)

---

## Disclaimer

This tool is a demonstration prototype. It is not approved for clinical use.
All explanations should be reviewed by a licensed genetic counselor before
being shared with patients.

---

*Built as a demo for BillionToOne — showing how AI can improve patient 
communication in genomics diagnostics workflows.*
