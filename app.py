import streamlit as st

# Configure the page layout
st.set_page_config(page_title="Mel's Goods", page_icon="🛍️", layout="wide")

# Store Header
st.title("🛍️ Welcome to Mel's Goods!")
st.write(
    "Discover quality items, curated collections, and your favorite everyday"
    " essentials."
)

st.markdown("---")

# Navigation layout
col1, col2, col3 = st.columns(3)

with col1:
  st.subheader("🏠 Home")
  st.write("Browse our welcome page and featured items right here.")

with col2:
  st.subheader("🔍 Search App")
  st.write("Use the sidebar menu on the left to open your search tool.")

with col3:
  st.subheader("📞 Contact")
  st.write("Reach out to our team for questions or support.")

st.markdown("---")
st.header("✨ Featured Collections")
st.write("Check out the sidebar to navigate to your search page!")
