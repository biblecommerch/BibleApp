import re
import pandas as pd
import streamlit as st
from styles import apply_global_styles
from auth_helper import render_sidebar_auth

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(page_title="Bible Translations Guide | Bible Focus", page_icon="📖", layout="centered")
apply_global_styles()
render_sidebar_auth()

# ==========================================
# TRANSLATION DATA & LOADER
# ==========================================
TRANSLATIONS = {
    "KJV (King James Version)": "KJV.csv",
    "ASV (American Standard Version)": "ASV.csv",
    "BSB (Berean Standard Bible)": "BSB.csv",
    "YLT (Young's Literal Translation)": "YLT.csv",
    "BBE (Bible in Basic English)": "BBE.csv",
    "DRC (Douay-Rheims Catholic Bible)": "DRC.csv",
}

@st.cache_data
def load_bible_data(csv_filename):
    try:
        return pd.read_csv(csv_filename)
    except Exception:
        return None

# ==========================================
# HEADER
# ==========================================
st.markdown(
    """
    <div class="header-box">
        <h1 style="margin:0;">Bible Translations Guide</h1>
        <p style="margin-top:5px;">Understand &amp; Compare All 6 Public Domain Translations on Bible Focus</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 1. SIDE-BY-SIDE VERSE COMPARISON TOOL
# ==========================================
st.subheader("⚖️ Compare Any Verse Across All 6 Translations")
st.write("Enter a Book, Chapter, and Verse below to read all six translations side by side:")

verse_query = st.text_input(
    "Enter Verse Reference:",
    value="John 3:16",
    placeholder="e.g., John 3:16, Romans 8:28, Genesis 1:1...",
)

if verse_query:
    match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", verse_query)
    if match:
        b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
        found_any = False

        for label, csv_file in TRANSLATIONS.items():
            df = load_bible_data(csv_file)
            if df is not None and not df.empty:
                b_col = "Book" if "Book" in df.columns else "book"
                c_col = "Chapter" if "Chapter" in df.columns else "chapter"
                v_col = "Verse" if "Verse" in df.columns else "verse"
                t_col = "Text" if "Text" in df.columns else "text"

                hit = df[
                    (df[b_col].astype(str).str.lower() == b_name.lower()) &
                    (df[c_col].astype(int) == c_num) &
                    (df[v_col].astype(int) == v_num)
                ]
                if not hit.empty:
                    found_any = True
                    row = hit.iloc[0]
                    st.markdown(
                        f"""
                        <div class="card" style="margin-bottom: 12px;">
                            <p style="margin: 0 0 6px 0; font-weight: bold;">{label}</p>
                            <p style="margin: 0; font-size: 1.05em;">"{row[t_col]}"</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        if not found_any:
            st.warning(f"Could not find '{verse_query}'. Check the book spelling and verse numbers.")
    else:
        st.info("Tip: Use the format **Book Chapter:Verse** (for example: `John 3:16`).")

# ==========================================
# 2. TRANSLATION PROFILES & DIFFERENCES
# ==========================================
st.markdown("---")
st.subheader("📚 About Each Bible Translation")
st.write("Every translation on Bible Focus is in the Public Domain and serves a unique purpose for reading and study:")

profiles = [
    (
        "KJV (King James Version) - 1611 / 1769",
        "Word-for-Word / Formal Equivalence",
        "The classic English translation known for its poetic rhythm, reverence, and historic influence. Uses traditional pronouns (thee, thou, thy) and translates from the Textus Receptus and Masoretic Text."
    ),
    (
        "ASV (American Standard Version) - 1901",
        "Strict Word-for-Word",
        "Prized by Bible students for extreme literal accuracy. Famous for consistently rendering God's covenant name as 'Jehovah' throughout the Old Testament."
    ),
    (
        "BSB (Berean Standard Bible) - Modern",
        "Balanced Word-for-Word & Readability",
        "A clean, modern English translation that blends accuracy to the original Hebrew and Greek with smooth, natural phrasing for everyday reading."
    ),
    (
        "YLT (Young's Literal Translation) - 1862",
        "Ultra-Literal (Preserves Original Verb Tenses)",
        "Translated by Robert Young to mirror the exact grammar and verb tenses of the original Hebrew and Greek texts, making it an invaluable tool for deep word study."
    ),
    (
        "BBE (Bible in Basic English) - 1949",
        "Simple, Clear English (1,000-Word Vocabulary)",
        "Created using a focused vocabulary of 1,000 basic English words so the message of Scripture is clear, accessible, and easy to grasp for readers of all ages."
    ),
    (
        "DRC (Douay-Rheims Catholic Bible) - 1582 / 1752",
        "Translated from the Latin Vulgate (73 Books)",
        "The historic English Catholic Bible translated from St. Jerome's Latin Vulgate. Includes the 7 Deuterocanonical Old Testament books and follows the Septuagint/Vulgate Psalm numbering."
    ),
]

for title, style, desc in profiles:
    with st.container(border=True):
        st.markdown(f"#### {title}")
        st.caption(f"**Translation Style:** {style}")
        st.write(desc)

st.markdown("---")
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")
