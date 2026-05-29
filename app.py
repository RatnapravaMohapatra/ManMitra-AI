import streamlit as st
from google import genai

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="ManMitra AI",
    page_icon="🧠",
    layout="centered"
)

# ==========================
# API CONFIG
# ==========================

try:
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"]
    )
except Exception:
    st.error(
        "API Key not found. Please add GOOGLE_API_KEY in Streamlit Secrets."
    )
    st.stop()

# ==========================
# HEADER
# ==========================

st.title("🧠 ManMitra AI")
st.subheader("Your AI Wellness Companion powered by Gemma 4")

st.info(
    "⚠️ This application provides wellness insights and self-reflection support. "
    "It is not a medical diagnosis tool or a replacement for professional care."
)

# ==========================
# DESCRIPTION
# ==========================

with st.expander("About ManMitra AI"):
    st.write("""
    ManMitra AI helps users reflect on their emotions through journaling.

    Features:
    - Emotional Summary
    - Stress Level Detection
    - Main Concern Identification
    - Positive Sign Recognition
    - Wellness Suggestions
    - Reflection Questions

    Powered by Google's Gemma 4 model.
    """)

# ==========================
# USER INPUT
# ==========================

journal = st.text_area(
    "📝 How are you feeling today?",
    height=250,
    placeholder="""
Example:

I have been feeling stressed about finding a job.
I studied machine learning today for two hours.
I am worried about my future but I feel motivated to keep learning.
"""
)

# ==========================
# ANALYSIS BUTTON
# ==========================

if st.button("🔍 Analyze My Journal"):

    if not journal.strip():
        st.warning("Please write something before analysis.")
        st.stop()

    prompt = f"""
You are ManMitra AI.

Analyze the following journal entry.

Provide your response in markdown format.

## Emotional Summary

Briefly summarize the emotional state.

## Stress Level

Choose one:
- Low
- Medium
- High

Explain why.

## Main Concerns

List major concerns if any.

## Positive Signs

Identify positive behaviors, strengths, or encouraging patterns.

## Wellness Suggestions

Provide practical and supportive suggestions.

## Reflection Question

Ask one thoughtful question to encourage self-reflection.

Important Rules:
- Be empathetic.
- Be supportive.
- Do not diagnose mental health conditions.
- Do not provide medical advice.
- Use simple and encouraging language.

Journal Entry:
{journal}
"""

    try:

        with st.spinner("🧠 Gemma 4 is analyzing your journal..."):

            response = client.models.generate_content(
                model="gemma-4-26b-a4b-it",
                contents=prompt
            )

        st.success("Analysis Complete")

        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error: {e}")

# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
    "Built with ❤️ using Streamlit and Gemma 4"
)