# pages/1_Translate.py

import streamlit as st
import requests

st.set_page_config(
    page_title="Translate | AI Shakespeare",
    page_icon="📝",
    layout="centered"
)

# --- Configuration ---------------------------------------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b"

PROMPT_TMPL = (
    "You are a literary translator. Convert the following modern English "
    "statement into Shakespearean English in exactly two lines. "
    "Adopt a {mood} mood.\n\n"
    "Original: {user_text}\nShakespearean:"
)

# --- Streamlit UI ----------------------------------------------------------
st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:32px;'>"
    "🎭 Translate</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "Enter a sentence, pick a mood, and watch the Bard at work!</p>",
    unsafe_allow_html=True
)

user_text = st.text_area(
    "Enter a sentence to translate:",
    height=120,
    placeholder="e.g., The weather outside is sunny."
)

mood = st.selectbox("Choose a mood:", ["Happy", "Sad"])

if st.button("Translate"):
    if not user_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Summoning the Bard…"):
            payload = {
                "model": MODEL_NAME,
                "prompt": PROMPT_TMPL.format(
                    user_text=user_text.strip(),
                    mood=mood
                ),
                "stream": False
            }
            try:
                resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
                resp.raise_for_status()
                response_text = resp.json().get("response", "").strip()
                st.markdown(
                    f"<p style='font-size:18px; font-weight:bold;'>"
                    f"{response_text}</p>",
                    unsafe_allow_html=True
                )
            except requests.RequestException as e:
                st.error(f"Error contacting model: {e}")

st.markdown("---")
st.markdown(
    "<p style='font-style:italic; text-align:center; font-size:14px;'>"
    "“The fool doth think he is wise, but the wise man knows himself to be a fool.”<br>"
    "– William Shakespeare</p>",
    unsafe_allow_html=True
)