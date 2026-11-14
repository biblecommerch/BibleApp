from datetime import datetime
import pandas as pd
import streamlit as st
from styles import apply_global_styles  # <-- ADD THIS

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mel's Goods", page_icon="📖", layout="centered")
apply_global_styles()  # <-- ADD THIS


# --- LOAD BIBLE DATA ---
@st.cache_data
def load_bible_data():
    try:
        return pd.read_csv("KJV.csv")
    except Exception:
        return None


df = load_bible_data()

# --- HEADER SECTION ---
st.markdown(
    """
    <div class="header-box">
        <h1 style="margin:0;">Mel's Goods</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Faith, Fellowship, & Fine Finds</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- AUTOMATIC DAILY VERSE ---
st.markdown("### Daily Verse")
if df is not None and not df.empty:
    # Use the current day of the year (1 to 365) to pick a verse automatically
    day_of_year = datetime.now().timetuple().tm_yday
    verse_index = day_of_year % len(df)
    daily_row = df.iloc[verse_index]

    book = daily_row.get("Book", daily_row.get("book", ""))
    chapter = daily_row.get("Chapter", daily_row.get("chapter", ""))
    verse_num = daily_row.get("Verse", daily_row.get("verse", ""))
    text = daily_row.get("Text", daily_row.get("text", ""))

    st.markdown(
        f"""
        <div class="card">
            <p style="font-size: 1.1em;"><b>"{text}"</b></p>
            <p style="color: #b7d5b8; margin: 0;">— {book} {chapter}:{verse_num}</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="card">
            <p><b>"The Lord is my strength and my shield; my heart trusted in him, and I am helped."</b></p>
            <p style="color: #b7d5b8; margin: 0;">— Psalm 28:7</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# --- LINK BOXES ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div class="card" style="text-align: center;">
            <h3>Mel's eBay Store</h3>
            <p>Browse our selection of unique goods and items.</p>
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
            <h3>Bible Com Blog</h3>
            <p>Read our latest articles, devotions, and updates.</p>
            <a href="https://www.biblecomblog.com" target="_blank">
                <button style="background-color: #4a6b4e; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Visit the Blog</button>
            </a>
        </div>
    """,
        unsafe_allow_html=True,
    )

# --- DIRECT BIBLE SEARCH ---
st.markdown("---")
st.subheader("Bible Search")
st.write(
    "Type any keyword, phrase, or passage reference below to search directly through the King James Bible:"
)

search_query = st.text_input(
    "Search the Bible:", placeholder="e.g., John 3:16, love, hope, strength..."
)

if search_query:
    if df is not None and not df.empty:
        results = df[
            df.apply(
                lambda row: row.astype(str)
                .str.contains(search_query, case=False)
                .any(),
                axis=1,
            )
        ]
        if not results.empty:
            st.success(f"Found {len(results)} matching verse(s):")
            st.dataframe(results, use_container_width=True)
        else:
            st.warning(f"No verses found matching '{search_query}'.")
    else:
        st.error(
            "Bible dataset (KJV.csv) could not be loaded. Please ensure KJV.csv is in your GitHub repository."
        )
