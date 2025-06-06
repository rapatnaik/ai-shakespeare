# pages/3_SonnetWriter.py

import streamlit as st
import requests

st.set_page_config(
    page_title="Sonnet Writer | AI Shakespeare",
    page_icon="✒️",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b"

st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:32px;'>"
    "📜 Shakespearean Sonnet Writer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "Provide a theme or topic, and receive a 14‐line Shakespearean sonnet.</p>",
    unsafe_allow_html=True
)

theme = st.text_input(
    "Enter a theme for your sonnet (e.g., \"love and loss\"):",
    placeholder="e.g., love, the sea, time, friendship…"
)

if st.button("Compose Sonnet"):
    if not theme.strip():
        st.warning("Please enter a theme for your sonnet.")
    else:
        with st.spinner("Composing a sonnet…"):
            prompt = (
                f"You are William Shakespeare. Write a 14‐line Shakespearean "
                f"sonnet about '{theme.strip()}'. Follow the classic ABAB CDCD EFEF GG rhyme scheme."
            )
            payload = {
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
            try:
                resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
                resp.raise_for_status()
                sonnet = resp.json().get("response", "").strip()

                html_sonnet = sonnet.replace("\n", "<br>")

                st.markdown(
                    f"<div style='font-size:18px; line-height:1.4;'>{html_sonnet}</div>",
                    unsafe_allow_html=True
                )
            except requests.RequestException as e:
                st.error(f"Error contacting model: {e}")