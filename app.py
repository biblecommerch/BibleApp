import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mel's Goods - Northwoods", page_icon="🌲", layout="centered"
)

# --- CUSTOM CSS FOR NORTHWOODS CABIN VIBE ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1b261c;
        color: #f4f1ea;
    }
    .northwoods-header {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1542224566-6e85f2e6772f?auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        padding: 40px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        border: 2px solid #3a5a40;
    }
    .card {
        background-color: #2b3a2a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #4a6b4e;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- NORTHWOODS HEADER ---
st.markdown(
    """
    <div class="northwoods-header">
        <h1>🌲 Welcome to Mel's Goods 🌲</h1>
        <p><i>Straight from the Northwoods of Wisconsin — Faith, Fellowship, and Fine Finds.</i></p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- DAILY VERSE SECTION ---
st.markdown(
    """
    <div class="card">
        <h3>📖 Daily Northwoods Reflection</h3>
        <p><b>"The Lord is my strength and my shield; my heart trusted in him, and I am helped."</b><br>
        <i>— Psalm 28:7</i></p>
        <p style="font-size: 0.9em; color: #b7d5b8;">Take a quiet moment today to reflect on His guidance, just like a quiet morning in the northern woods.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- NAVIGATION & QUICK LINKS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    <div class="card" style="text-align: center;">
        <h3>🛒 Mel's eBay Store</h3>
        <p>Browse our curated selection of unique goods and treasures.</p>
        <a href="https://www.ebay.com/str/shopmelsgoods" target="_blank">
            <button style="background-color: #4a6b4e; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Visit eBay Store</button>
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="card" style="text-align: center;">
        <h3>✍️ Bible Com Blog</h3>
        <p>Read our latest thoughts, devotionals, and updates.</p>
        <a href="https://www.biblecomblog.com" target="_blank">
            <button style="background-color: #4a6b4e; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Visit the Blog</button>
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

# --- QUICK NAVIGATOR TO BIBLE SEARCH ---
st.markdown("---")
st.subheader("🔍 Ready to study?")
st.write(
    "Use your sidebar menu on the left to jump right into the **Bible Search** page, or click below:"
)

if st.button("📖 Go to Bible Search Tool"):
    st.switch_page("pages/bible_search.py")
