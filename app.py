import streamlit as st

# 1. Define your pages with custom titles, punctuation, and icons
home_page = st.Page("app.py", title="Mel's Goods Home", icon="🏠")
search_page = st.Page(
    "pages/bible_search.py", title="Bible Search", icon="📖"
)

# 2. Set up the navigation menu
pg = st.navigation([home_page, search_page])

# 3. Run the navigation system
pg.run()

# --- Your Main Home Page Content ---
st.title("Welcome to Mel's Goods! 🛒")
st.write(
    "Use the sidebar menu on the left to switch between the Home page and the Bible Search tool."
)
