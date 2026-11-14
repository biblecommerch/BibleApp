import streamlit as st

# --- PAGE STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1b261c;
        color: #f4f1ea;
    }
    .card {
        background-color: #2b3a2a;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #4a6b4e;
        margin-bottom: 25px;
    }
    .content-box {
        background-color: #2b3a2a;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #4a6b4e;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HOME PAGE CONTENT ---
st.markdown(
    """
    <div class="card">
        <h1 style="margin:0; color: #f4f1ea;">Welcome to Your Bible App</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Your daily space for scripture search, reflection, and reading plans.</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="content-box">
    <h3 style="margin-top:0; color: #b7d5b8;">Where would you like to go?</h3>
    <p>🔍 <b><a href="/bible_search" style="color: #b7d5b8;">Bible Search</a></b>: Look up verses across the King James Version easily.</p>
    <p style="margin-bottom:0;">📅 <b><a href="/thirty_day_challenge" style="color: #b7d5b8;">30 Day Challenge</a></b>: Build a daily habit of reading God's Word through our curated reading guide.</p>
</div>
""",
    unsafe_allow_html=True,
)
