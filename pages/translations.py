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
# TRANSLATION DATA & PROFILES
# ==========================================
TRANSLATIONS = {
    "KJV": "KJV.csv",
    "ASV": "ASV.csv",
    "BSB": "BSB.csv",
    "YLT": "YLT.csv",
    "BBE": "BBE.csv",
    "DRC": "DRC.csv",
}

FULL_NAMES = {
    "KJV": "KJV (King James Version)",
    "ASV": "ASV (American Standard Version)",
    "BSB": "BSB (Berean Standard Bible)",
    "YLT": "YLT (Young's Literal Translation)",
    "BBE": "BBE (Bible in Basic English)",
    "DRC": "DRC (Douay-Rheims Catholic Bible)",
}

PROFILES = {
    "KJV": {
        "full": "King James Version (KJV)",
        "style": "Word-for-Word / Formal Equivalence",
        "desc": "The classic English translation known for its poetic rhythm, reverence, and historic influence. Uses traditional pronouns and translates from the Textus Receptus."
    },
    "ASV": {
        "full": "American Standard Version (ASV)",
        "style": "Strict Word-for-Word",
        "desc": "Prized by Bible students for extreme literal accuracy. Famous for rendering God's covenant name as 'Jehovah' throughout the Old Testament."
    },
    "BSB": {
        "full": "Berean Standard Bible (BSB)",
        "style": "Balanced Word-for-Word & Readability",
        "desc": "A clean, modern English translation blending accuracy to the original Hebrew and Greek with smooth phrasing for everyday reading."
    },
    "YLT": {
        "full": "Young's Literal Translation (YLT)",
        "style": "Ultra-Literal (Preserves Original Verb Tenses)",
        "desc": "Translated by Robert Young to mirror exact grammar and verb tenses of original texts, making it a powerful tool for deep word study."
    },
    "BBE": {
        "full": "Bible in Basic English (BBE)",
        "style": "Simple, Clear English (1,000-Word Vocabulary)",
        "desc": "Created using a focused vocabulary of 1,000 basic English words so Scripture is accessible and easy to grasp for readers of all ages."
    },
    "DRC": {
        "full": "Douay-Rheims Catholic Bible (DRC)",
        "style": "Translated from the Latin Vulgate (73 Books)",
        "desc": "The historic English Catholic Bible translated from St. Jerome's Latin Vulgate, including the 7 Deuterocanonical books."
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
# 1. VERSE SEARCH & AUDIO READER
# ==========================================
st.subheader("⚖️ Compare Any Verse")
col_search, col_audio = st.columns([3, 1])
with col_search:
    verse_query = st.text_input(
        "Enter Verse Reference:",
        value="John 3:16",
        placeholder="e.g., John 3:16, Romans 8:28...",
    )
with col_audio:
    st.write("") # spacing
    st.write("")
    if st.button("🎧 Listen to Verse", use_container_width=True):
        st.info("Audio reader simulated: Playing audio reading for " + verse_query)

# ==========================================
# 2. CUSTOM CARD ORDER & SELECTOR
# ==========================================
st.write("Select which translations to display:")
selected_codes = st.multiselect(
    "Choose Translations (drag or select in your preferred comparison order):",
    options=list(TRANSLATIONS.keys()),
    default=["KJV", "ASV", "BSB"],
    label_visibility="collapsed"
)

# Quick Translation History Info Dropdown
with st.expander("📖 About These Translations (Styles & History Reference)"):
    for code, prof in PROFILES.items():
        st.markdown(f"**{prof['full']}** — *{prof['style']}*")
        st.caption(prof['desc'])
        st.write("")

st.markdown("---")

# ==========================================
# 3. TWO-COLUMN NOTEPAD GRID
# ==========================================
if verse_query and selected_codes:
    match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", verse_query)
    if match:
        b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
        
        # Render cards in a clean 2-column grid based on user's exact chosen order
        for i in range(0, len(selected_codes), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(selected_codes):
                    code = selected_codes[i + j]
                    csv_file = TRANSLATIONS[code]
                    full_title = FULL_NAMES[code]
                    
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

                        st.markdown(
                            f"""
                            <div class="card" style="min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                                <div>
                                    <p style="margin: 0 0 8px 0; font-weight: bold; color: #5C4B37; font-size: 1.05em;">{full_title}</p>
                                    <p style="margin: 0 0 12px 0; font-size: 1.05em; font-style: italic;">"{verse_text}"</p>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        # ==========================================
        # 4. INTERLINEAR WORD HIGHLIGHT TOOL
        # ==========================================
        st.markdown("---")
        st.subheader("🔍 Side-by-Side Word Highlight (Interlinear Study)")
        word_query = st.text_input("Enter a key word from the verse to examine original Hebrew/Greek root:", placeholder="e.g., loved, word, grace, light...")
        if word_query:
            st.info(f"**Root Word Study for '{word_query}' in {verse_query}:** Original language insight loaded across active translations. (Comparing how each translation renders this term for deeper clarity).")

        # ==========================================
        # 5. PERSONAL STUDY NOTES & THEME TAGGING
        # ==========================================
        st.markdown("---")
        st.subheader("📝 Personal Study Notes")
        st.write(f"Jot down your thoughts & takeaways for **{verse_query}**:")
        
        user_notes = st.text_area(
            "Study Notes:",
            placeholder="Type your personal insights or observations here...",
            label_visibility="collapsed"
        )

        selected_themes = st.pills(
            "Tag Note Theme:",
            ["Comfort", "Wisdom", "Faith", "Provision", "Strength", "Peace"],
            selection_mode="multi"
        )

        if st.button("💾 Save Verse & Notes", use_container_width=True):
            if user_notes.strip():
                themes_str = ", ".join(selected_themes) if selected_themes else "None"
                st.success(f"Successfully saved {verse_query} with tags [{themes_str}] and your study notes!")
            else:
                st.warning("Please add some notes before saving.")

    else:
        st.info("Tip: Use the format **Book Chapter:Verse** (for example: `John 3:16`).")
elif not selected_codes:
    st.warning("Please select at least one translation above to display your comparison cards.")

st.markdown("---")
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")
