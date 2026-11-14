import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bible App", page_icon="📖", layout="centered")

# --- DEFINE YOUR PAGES WITH CLEAN TITLES ---
home_page = st.Page("app.py", title="Home", icon="🏠")
search_page = st.Page("pages/bible_search.py", title="Bible Search", icon="🔍")
challenge_page = st.Page(
    "pages/thirty_day_challenge.py", title="30 Day Challenge", icon="📅"
)

# --- SET UP NAVIGATION ---
pg = st.navigation([home_page, search_page, challenge_page])
pg.run()

# --- HOME PAGE CONTENT (Shows when "Home" is selected) ---
if pg == home_page:
    st.markdown(
        """
        <div style="background-color: #2b3a2a; padding: 30px; border-radius: 10px; text-align: center; border: 1px solid #4a6b4e; margin-bottom: 25px;">
            <h1 style="margin:0; color: #f4f1ea;">Welcome to Your Bible App</h1>
            <p style="margin-top:5px; color: #b7d5b8;">Your daily space for scripture search, reflection, and reading plans.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    ### Where would you like to go?
    - 🔍 **[Bible Search](https://kjv-bible.streamlit.app/bible_search)**: Look up verses across the King James Version easily.
    - 📅 **[30 Day Challenge](https://kjv-bible.streamlit.app/thirty_day_challenge)**: Build a daily habit of reading God's Word through our curated reading guide.
    """
    )
