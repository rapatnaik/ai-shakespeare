# pages/4_AdviceGiver.py

import streamlit as st
import requests

st.set_page_config(
    page_title="Advice Giver | AI Shakespeare",
    page_icon="💡",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b"

st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:32px;'>"
    "💭 Shakespearean Advice Giver</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "Ask any question or describe your dilemma, and receive guidance in Shakespearean English.</p>",
    unsafe_allow_html=True
)

question = st.text_area(
    "What would you like advice on?",
    height=120,
    placeholder="e.g., How can I prepare for my final exams wisely?"
)

if st.button("Get Advice"):
    if not question.strip():
        st.warning("Please type your question or dilemma first.")
    else:
        with st.spinner("Consulting the Bard…"):
            prompt = (
                f"You are a wise counselor at the Elizabethan court. "
                f"Respond to the following query in Shakespearean English, using archaic phrasing:\n\n"
                f"Query: {question.strip()}\n"
                f"Counsel:"
            )
            payload = {
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
            try:
                resp = requests.post(OLLAMA_URL, json=payload, timeout=100)
                resp.raise_for_status()
                advice = resp.json().get("response", "").strip()
              
                html_advice = advice.replace("\n", "<br>")


                st.markdown(
                    f"<div style='font-size:18px; line-height:1.5;'>{html_advice}</div>",
                    unsafe_allow_html=True

                )
            except requests.RequestException as e:
                st.error(f"Error contacting model: {e}")