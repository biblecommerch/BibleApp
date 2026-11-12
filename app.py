import streamlit as st

# Set up the navigation menu pointing to your pages folder
pg = st.navigation([st.Page("pages/bible_search.py", title="Bible Search", icon="📖")])

# Run the navigation system
pg.run()

# --- Your Main Mel's Goods Home Page Content ---
st.title("Welcome to Mel's Goods! 🛒")
st.write(
    "Use the sidebar menu on the left to switch between pages and access the Bible Search tool."
)
