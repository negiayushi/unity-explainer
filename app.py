# ============================================================
# app.py
# This is the main file that runs the web application.
# Streamlit turns this Python file into a real website
# you can open in your browser.
# Run it with:  streamlit run app.py
# ============================================================

import streamlit as st
import os
import tempfile
from conditions import CONDITIONS, RESULT_TYPES, LANGUAGES
from explainer import generate_explanation
from report import generate_pdf


# ── Page configuration ────────────────────────────────────────
# This must be the very first Streamlit command in the file.
st.set_page_config(
    page_title="Unity Result Explainer | BillionToOne Demo",
    page_icon="🧬",
    layout="centered",
)


# ── Custom CSS styling ────────────────────────────────────────
# This makes the app look cleaner and more professional.
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0a6450 0%, #0d8a6e 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .main-header h1 { color: white; margin: 0; font-size: 1.6rem; }
    .main-header p  { color: #b2ede0; margin: 0.4rem 0 0; font-size: 0.95rem; }
    .result-box {
        background: #f7faf9;
        border-left: 4px solid #0a6450;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        white-space: pre-wrap;
        font-size: 1rem;
        line-height: 1.7;
        color: #1a1a1a;
    }
    .info-badge {
        background: #e8f5f1;
        color: #0a6450;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.2rem;
    }
    .stButton > button {
        background-color: #0a6450 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.5rem !important;
    }
    .stButton > button:hover {
        background-color: #085440 !important;
    }
</style>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🧬 Unity / Northstar — Patient Result Explainer</h1>
    <p>
        Enter a patient's genetic test result below. 
        The tool generates a warm, plain-language explanation 
        in the patient's language — ready to share in seconds.
    </p>
</div>
""", unsafe_allow_html=True)


# ── Check for API key before showing the form ─────────────────
if not os.environ.get("GROQ_API_KEY"):
    st.error(
        "⚠️ GROQ_API_KEY not found. "
        "Please set it in your terminal before running this app. "
        "See the README.md for instructions."
    )
    st.stop()  # Stop the app here if no key is set


# ── Input form ────────────────────────────────────────────────
st.markdown("### Patient details")
st.caption("Fill in the details from the patient's Unity or Northstar report.")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input(
        "Patient first name *",
        placeholder="e.g. Maria",
        help="Used to personalize the explanation with their name."
    )

    condition = st.selectbox(
        "Condition / gene tested *",
        list(CONDITIONS.keys()),
        help="Select the condition that was screened for."
    )

    result = st.selectbox(
        "Result type *",
        RESULT_TYPES,
        help="Select the result category shown on the report."
    )

with col2:
    risk = st.text_input(
        "Risk or probability from report *",
        placeholder="e.g. 1 in 4, or < 1 in 10,000, or N/A",
        help="Copy the exact number from the report."
    )

    language = st.selectbox(
        "Patient's preferred language *",
        LANGUAGES,
        help="The explanation will be fully written in this language."
    )

    extra = st.text_area(
        "Extra context for the AI (optional)",
        placeholder=(
            "e.g. Patient is 12 weeks pregnant and very anxious. "
            "Partner is also a confirmed carrier."
        ),
        height=118,
        help="Any additional context helps the AI tailor the explanation."
    )

st.markdown("")

# ── Condition info preview ────────────────────────────────────
if condition:
    cdata = CONDITIONS[condition]
    st.markdown(
        f'<span class="info-badge">🧪 Gene: {cdata["gene"]}</span>'
        f'<span class="info-badge">📋 Product: {cdata["product"]}</span>'
        f'<span class="info-badge">🔗 Inheritance: {cdata["inheritance"]}</span>',
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Generate button ───────────────────────────────────────────
generate_clicked = st.button(
    "✨ Generate patient explanation",
    use_container_width=True,
)

if generate_clicked:

    # Validate required fields
    missing = []
    if not patient_name.strip():
        missing.append("Patient first name")
    if not risk.strip():
        missing.append("Risk or probability")

    if missing:
        st.error(f"Please fill in: {', '.join(missing)}")

    else:
        condition_data = CONDITIONS[condition]

        # Show a spinner while the AI is generating
        with st.spinner(
            f"Generating plain-language explanation in {language}... "
            "This takes about 3-5 seconds."
        ):
            try:
                explanation = generate_explanation(
                    condition_name=condition,
                    condition_data=condition_data,
                    result_type=result,
                    risk_number=risk,
                    patient_name=patient_name.strip(),
                    language=language,
                    extra_context=extra.strip(),
                )
            except Exception as e:
                st.error(
                    f"Something went wrong calling the Groq API: {e}\n\n"
                    "Check that your GROQ_API_KEY is set correctly."
                )
                st.stop()

        # ── Show the result ───────────────────────────────────
        st.success("✅ Explanation ready!")

        st.markdown("### Plain-language explanation")
        st.markdown(
            f'<div class="result-box">{explanation}</div>',
            unsafe_allow_html=True,
        )

        # ── Counselor notes expander ──────────────────────────
        with st.expander("📋 Counselor background notes"):
            st.info(condition_data["counseling_note"])
            st.markdown(f"**Analogy used:** {condition_data['analogy']}")

        st.markdown("---")

        # ── Generate and download PDF ─────────────────────────
        st.markdown("### Download patient card")

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".pdf"
        ) as tmp:
            pdf_path = tmp.name

        generate_pdf(
            patient_name=patient_name.strip(),
            condition=condition,
            result=result,
            risk=risk,
            product=condition_data["product"],
            language=language,
            explanation=explanation,
            output_path=pdf_path,
        )

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()

        os.remove(pdf_path)

        safe_name = patient_name.strip().replace(" ", "_")
        safe_cond = condition[:20].replace(" ", "_").replace("/", "-")

        st.download_button(
            label="📄 Download printable PDF card",
            data=pdf_bytes,
            file_name=f"result_summary_{safe_name}_{safe_cond}.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

        st.caption(
            "The PDF is formatted for printing or emailing directly to the patient."
        )


# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "🧬 Demo built to show how AI can reduce genetic counselor call volume "
    "while improving patient understanding of Unity and Northstar results. "
    "Powered by Llama 3.3 (Meta) via Groq inference. "
    "Not for clinical use — demonstration purposes only."
)
