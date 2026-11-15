import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bible App", page_icon="📖", layout="centered")

# --- DEFINE YOUR PAGES ---
home_page = st.Page("pages/home.py", title="Home", icon="🏠")
search_page = st.Page("pages/bible_search.py", title="Bible Search", icon="🔍")
challenge_page = st.Page("pages/thirty_day_challenge.py", title="30 Day Challenge", icon="📅")
privacy_page = st.Page("pages/privacy.py", title="Privacy Policy", icon="🔒")

# --- REGISTER ALL PAGES BUT HIDE DEFAULT TOP MENU ---
pg = st.navigation([home_page, search_page, challenge_page, privacy_page], position="hidden")

# --- BUILD CLEAN TOP MENU (WITHOUT PRIVACY POLICY) ---
st.sidebar.page_link(home_page, label="Home", icon="🏠")
st.sidebar.page_link(search_page, label="Bible Search", icon="🔍")
st.sidebar.page_link(challenge_page, label="30 Day Challenge", icon="📅")

pg.run()
