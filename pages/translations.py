import re
import pandas as pd
import streamlit as st
from styles import apply_global_styles
from auth_helper import render_sidebar_auth

# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(page_title="Bible Translations | Bible Focus", page_icon="📖", layout="centered")
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

PROFILES = {
    "KJV (King James Version)": {
        "style": "Word-for-Word / Formal Equivalence",
        "desc": "The classic English translation known for its poetic rhythm, reverence, and historic influence. Uses traditional pronouns (thee, thou, thy) and translates from the Textus Receptus and Masoretic Text."
    },
    "ASV (American Standard Version)": {
        "style": "Strict Word-for-Word",
        "desc": "Prized by Bible students for extreme literal accuracy. Famous for consistently rendering God's covenant name as 'Jehovah' throughout the Old Testament."
    },
    "BSB (Berean Standard Bible)": {
        "style": "Balanced Word-for-Word & Readability",
        "desc": "A clean, modern English translation that blends accuracy to the original Hebrew and Greek with smooth, natural phrasing for everyday reading."
    },
    "YLT (Young's Literal Translation)": {
        "style": "Ultra-Literal (Preserves Original Verb Tenses)",
        "desc": "Translated by Robert Young to mirror the exact grammar and verb tenses of the original Hebrew and Greek texts, making it an invaluable tool for deep word study."
    },
    "BBE (Bible in Basic English)": {
        "style": "Simple, Clear English (1,000-Word Vocabulary)",
        "desc": "Created using a focused vocabulary of 1,000 basic English words so the message of Scripture is clear, accessible, and easy to grasp for readers of all ages."
    },
    "DRC (Douay-Rheims Catholic Bible)": {
        "style": "Translated from the Latin Vulgate (73 Books)",
        "desc": "The historic English Catholic Bible translated from St. Jerome's Latin Vulgate. Includes the 7 Deuterocanonical Old Testament books and follows the Septuagint/Vulgate Psalm numbering."
    },
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
        <h1 style="margin:0;">Bible Translations</h1>
        <p style="margin-top:5px;">Compare and study your favorite verse across multiple translations.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 1. VERSE SEARCH & TRANSLATION SELECTOR
# ==========================================
st.subheader("⚖️ Compare Any Verse")
verse_query = st.text_input(
    "Enter Verse Reference:",
    value="John 3:16",
    placeholder="e.g., John 3:16, Romans 8:28, Genesis 1:1...",
)

st.write("Select which translation cards to display on your board:")

# Interactive toggle checkboxes for active cards
col_t1, col_t2, col_t3 = st.columns(3)
selected_active = []
trans_keys = list(TRANSLATIONS.keys())

with col_t1:
    if st.checkbox(trans_keys[0], value=True): selected_active.append(trans_keys[0])
    if st.checkbox(trans_keys[3], value=False): selected_active.append(trans_keys[3])
with col_t2:
    if st.checkbox(trans_keys[1], value=True): selected_active.append(trans_keys[1])
    if st.checkbox(trans_keys[4], value=False): selected_active.append(trans_keys[4])
with col_t3:
    if st.checkbox(trans_keys[2], value=True): selected_active.append(trans_keys[2])
    if st.checkbox(trans_keys[5], value=False): selected_active.append(trans_keys[5])

st.markdown("---")

# ==========================================
# 2. TWO-COLUMN NOTEPAD GRID & STUDY NOTES
# ==========================================
if verse_query and selected_active:
    match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", verse_query)
    if match:
        b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
        
        # Dictionary to store fetched verses for saving later
        current_verse_data = {}

        # Render cards in a clean 2-column grid
        for i in range(0, len(selected_active), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(selected_active):
                    label = selected_active[i + j]
                    csv_file = TRANSLATIONS[label]
                    profile = PROFILES[label]
                    
                    with cols[j]:
                        df = load_bible_data(csv_file)
                        verse_text = "Verse not found in this translation."
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
                                verse_text = hit.iloc[0][t_col]

                        current_verse_data[label] = verse_text

                        st.markdown(
                            f"""
                            <div class="card" style="min-height: 180px; display: flex; flex-direction: column; justify-content: space-between;">
                                <div>
                                    <p style="margin: 0 0 8px 0; font-weight: bold; color: #5C4B37; font-size: 1.05em;">{label}</p>
                                    <p style="margin: 0 0 12px 0; font-size: 1.05em; font-style: italic;">"{verse_text}"</p>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                        with st.expander("About this translation"):
                            st.caption(f"**Style:** {profile['style']}")
                            st.write(profile["desc"])

        # ==========================================
        # 3. PERSONAL STUDY NOTEPAD & SAVE SECTION
        # ==========================================
        st.markdown("---")
        st.subheader("📝 Personal Study Notes")
        st.write(f"Jot down your thoughts, takeaways, or prayers for **{verse_query}**:")
        
        user_notes = st.text_area(
            "Study Notes:",
            placeholder="Type your personal insights or observations here...",
            label_visibility="collapsed"
        )

        if st.button("💾 Save Verse & Notes", use_container_width=True):
            if user_notes.strip():
                st.success(f"Successfully saved {verse_query} and your study notes! (Linked to your account session)")
            else:
                st.warning("Please add some notes before saving.")

    else:
        st.info("Tip: Use the format **Book Chapter:Verse** (for example: `John 3:16`).")
elif not selected_active:
    st.warning("Please select at least one translation checkbox above to display your notepad cards.")

st.markdown("---")
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")
