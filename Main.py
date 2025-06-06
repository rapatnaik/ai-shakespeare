# app.py
'''
import streamlit as st

st.set_page_config(page_title="AI Shakespeare", page_icon="🎭", layout="centered")

st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:40px;'>"
    "AI Shakespeare</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "Welcome to AI Shakespeare! Choose one of the pages from the sidebar:"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(
    """
- **Translate**: Turn modern sentences into two‐line Shakespearean verse (happy/sad).  
- **Insult/Complement Generator**: Get a Bard‐style insult or complement for any target.  
- **Sonnet Writer**: Generate a full 14‐line Shakespearean‐style sonnet.  
- **Advice Giver**: Ask any question and receive advice in Shakespearean English.
"""
)
'''
# app.py
# app.py

import streamlit as st

st.set_page_config(
    page_title="AI Shakespeare",
    page_icon="🎭",
    layout="centered"
)

# Title
st.markdown(
    "<h1 style='text-align:center; font-weight:bold; font-size:32px;'>"
    "🎭 AI Shakespeare</h1>",
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "A simple suite of Bard-inspired tools. Pick a page from the sidebar:</p>",
    unsafe_allow_html=True
)

st.write("")  # small spacer

# List of features with emojis
st.markdown(
    """
- 🎭 **Translate**  
  Convert modern sentences into two-line Shakespearean verse (choose Happy or Sad).

- 🗡️/❤️ **Insult / Compliment**  
  Generate a witty Bard-style insult or a flattering compliment for any target.

- 📜 **Sonnet Writer**  
  Provide a theme and receive a 14-line Shakespearean sonnet (ABAB CDCD EFEF GG).

- 💭 **Advice Giver**  
  Ask any question and get counsel in Shakespearean English, like a royal advisor.
"""
)

st.markdown("---")

# Footer quote
st.markdown(
    "<p style='font-style:italic; text-align:center; font-size:14px;'>"
    "“All the world’s a stage, and all the men and women merely players.”<br>"
    "– William Shakespeare</p>",
    unsafe_allow_html=True
)