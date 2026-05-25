# ============================================================
# explainer.py
# This file talks to the Groq API (which runs Llama 3,
# a free open-source AI model made by Meta).
# It sends the patient's result details and gets back
# a warm, plain-language explanation.
# ============================================================
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from groq import Groq

client = Groq()

# This line creates a connection to Groq.
# It automatically reads your GROQ_API_KEY from the environment.


def generate_explanation(
    condition_name: str,
    condition_data: dict,
    result_type: str,
    risk_number: str,
    patient_name: str,
    language: str,
    extra_context: str = "",
) -> str:
    """
    Sends the patient result info to Llama 3 via Groq
    and returns a plain-language patient explanation.
    """

    # This is the instruction we give to the AI.
    # Think of it like writing a very detailed job description
    # for the AI before it writes the explanation.
    prompt = f"""You are a compassionate, experienced genetic counselor 
at BillionToOne — a leading genomics diagnostics company based in California.

Your job right now is to write a warm, clear, plain-language explanation 
of a patient's genetic test result. This explanation will be handed 
directly to the patient or read to them over the phone.

Here are the details of this patient's result:

PATIENT FIRST NAME: {patient_name}
CONDITION TESTED FOR: {condition_name}
GENE OR CHROMOSOME INVOLVED: {condition_data['gene']}
TEST PRODUCT USED: {condition_data['product']}
RESULT TYPE: {result_type}
RISK NUMBER OR PROBABILITY: {risk_number}
INHERITANCE PATTERN: {condition_data['inheritance']}
ANALOGY TO USE: {condition_data['analogy']}
COUNSELING NOTE (background for context): {condition_data['counseling_note']}
EXTRA CONTEXT FROM COUNSELOR: {extra_context if extra_context else 'None provided.'}
OUTPUT LANGUAGE: {language}

Now write the patient explanation. Follow this exact structure:

1. GREETING
   Start with "{patient_name}," and a warm one-sentence opening.

2. WHAT YOUR RESULT MEANS
   2-3 sentences. Use extremely simple words — no medical jargon at all.
   Write as if explaining to a 6th grader. Be direct but calm.

3. A HELPFUL WAY TO THINK ABOUT IT
   Use the analogy provided above. Adapt it naturally into 2-3 sentences.
   Do not quote it word-for-word — make it feel conversational.

4. WHAT THIS MEANS FOR YOU
   2-3 sentences. Be specific to this patient's result type.
   If it is low risk, reassure clearly. If carrier, explain they are healthy.
   If high risk or positive, be calm and focus on available options and support.

5. YOUR NEXT STEPS
   Write exactly 3 bullet points. Each one is a clear, specific action.
   Start each with a verb (e.g. "Schedule...", "Ask your doctor...", "Contact...").

6. CLOSING
   One warm, reassuring sentence. End with the patient's name.

STRICT RULES:
- Total length: 250 to 320 words. Not more, not less.
- No medical jargon, no Latin terms, no abbreviations without explanation.
- Tone: warm, calm, like a knowledgeable trusted friend. Never clinical or alarming.
- Do NOT include any legal disclaimers, liability language, or "consult a doctor" 
  boilerplate — the counselor handles that separately.
- If {language} is not English, write the ENTIRE explanation in {language}.
  Every single word, including section headers, must be in {language}.
- Do not add any extra sections, headers, or notes beyond the 6 sections above."""

    # Send the prompt to Llama 3 running on Groq servers
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Llama 3.3, 70 billion parameters
        max_tokens=1000,                    # Maximum length of the response
        temperature=0.7,                   # 0 = very predictable, 1 = more creative
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a compassionate genetic counselor. "
                    "You always follow the exact format and length instructions given. "
                    "You never add extra content beyond what is asked."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    # Extract and return just the text from the response
    return response.choices[0].message.content
