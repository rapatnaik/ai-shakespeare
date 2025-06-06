# pages/2_InsultCompliment.py

import streamlit as st
import requests

st.set_page_config(
    page_title="Insult / Compliment | AI Shakespeare",
    page_icon="🗡️❤️",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b"

st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:32px;'>"
    "🗡️/❤️ Shakespearean Insult & Compliment Generator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "Choose whether to create a witty insult or a flattering compliment in Bard-style. "
    "Then enter the name or noun to target.</p>",
    unsafe_allow_html=True
)

# Let user pick Insult or Compliment
choice = st.selectbox("Choose type:", ["Insult", "Compliment"])

# Let user enter a name or noun
target = st.text_input(
    "Enter who (or what) this should be aimed at:",
    placeholder="e.g., my rival, my friend, the cat, my boss…"
)

if st.button("Generate"):
    if not target.strip():
        st.warning("Please enter a name or noun to aim this at.")
    else:
        with st.spinner("Summoning the Bard’s wit…"):
            if choice == "Insult":
                prompt = (
                    f"You are the jester at the Elizabethan court. "
                    f"Create a witty Shakespearean insult aimed at '{target.strip()}'. "
                    f"Use archaic phrasing and rhyme in two lines.\n\n"
                    f"Insult:"
                )
            else:  # Compliment
                prompt = (
                    f"You are a courtly poet in the Elizabethan era. "
                    f"Compose a flattering Shakespearean compliment for '{target.strip()}'. "
                    f"Use archaic phrasing and rhyme in two lines.\n\n"
                    f"Compliment:"
                )

            payload = {
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }

            try:
                resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
                resp.raise_for_status()
                result = resp.json().get("response", "").strip()

                # Replace newlines with <br> before rendering
                html_result = result.replace("\n", "<br>")

                st.markdown(
                    f"<p style='font-size:18px; font-weight:bold;'>{html_result}</p>",
                    unsafe_allow_html=True
                )
            except requests.RequestException as e:
                st.error(f"Error contacting model: {e}")