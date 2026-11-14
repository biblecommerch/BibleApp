import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bible App", page_icon="📖", layout="centered")

# --- DEFINE YOUR PAGES WITH CLEAN TITLES ---
home_page = st.Page("pages/home.py", title="Home", icon="🏠")
search_page = st.Page("pages/bible_search.py", title="Bible Search", icon="🔍")
challenge_page = st.Page(
    "pages/thirty_day_challenge.py", title="30 Day Challenge", icon="📅"
)

# --- SET UP NAVIGATION ---
pg = st.navigation([home_page, search_page, challenge_page])
pg.run()
