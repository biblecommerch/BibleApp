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

st.markdown(
    """
    <style>
    /* Notepad Card Styling */
    .notepad-card {
        background-color: #FFFFFF;
        border: 1px solid #E2D9C8;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
    "KJV": "King James Version (KJV)",
    "ASV": "American Standard Version (ASV)",
    "BSB": "Berean Standard Bible (BSB)",
    "YLT": "Young's Literal Translation (YLT)",
    "BBE": "Bible in Basic English (BBE)",
    "DRC": "Douay-Rheims Catholic Bible (DRC)",
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

# Initialize Session State for Active Translations Order
if "active_order" not in st.session_state:
    st.session_state.active_order = ["KJV", "ASV", "BSB"]

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
# 1. VERSE SEARCH (CLEAN INPUT)
# ==========================================
st.subheader("⚖️ Compare Any Verse")
verse_query = st.text_input(
    "Enter Verse Reference:",
    value="John 3:16",
    placeholder="e.g., John 3:16, Romans 8:28...",
)

# ==========================================
# 2. TRANSLATION PILLS SELECTOR (GREEN WHEN ON / GRAY WHEN OFF)
# ==========================================
st.write("Select which translations to display:")
selected_translations = st.pills(
    "Choose Translations",
    options=list(TRANSLATIONS.keys()),
    default=st.session_state.active_order,
    selection_mode="multi",
    label_visibility="collapsed"
)

# Update session state order immediately when user clicks pills
if selected_translations:
    # Keep user's custom arrangement order if they already had it, or update it
    st.session_state.active_order = selected_translations
# ==========================================
# 3. TWO-COLUMN NOTEPAD GRID (WITH CONTROLS)
# ==========================================
active_codes = st.session_state.active_order

if verse_query and active_codes:
    match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", verse_query)
    if match:
        b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
        st.write("")

        # Render cards in a clean 2-column grid based on active ordering
        for i in range(0, len(active_codes), 2):
            cols = st.columns(2)
            for j in range(2):
                idx = i + j
                if idx < len(active_codes):
                    code = active_codes[idx]
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
                            <div class="notepad-card">
                                <div>
                                    <p style="margin: 0 0 8px 0; font-weight: bold; color: #5C4B37; font-size: 1.05em;">{full_title}</p>
                                    <p style="margin: 0 0 12px 0; font-size: 1.05em; font-style: italic;">"{verse_text}"</p>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                        # Directional Controls (Left, Right, Up, Down)
                        c_l, c_r, c_u, c_d = st.columns(4)
                        with c_l:
                            if idx > 0 and st.button("◀", key=f"left_{code}_{idx}", use_container_width=True, help="Move Left"):
                                active_codes[idx], active_codes[idx - 1] = active_codes[idx - 1], active_codes[idx]
                                st.session_state.active_order = active_codes
                                st.rerun()
                        with c_r:
                            if idx < len(active_codes) - 1 and st.button("▶", key=f"right_{code}_{idx}", use_container_width=True, help="Move Right"):
                                active_codes[idx], active_codes[idx + 1] = active_codes[idx + 1], active_codes[idx]
                                st.session_state.active_order = active_codes
                                st.rerun()
                        with c_u:
                            if idx >= 2 and st.button("▲", key=f"up_{code}_{idx}", use_container_width=True, help="Move Up"):
                                active_codes[idx], active_codes[idx - 2] = active_codes[idx - 2], active_codes[idx]
                                st.session_state.active_order = active_codes
                                st.rerun()
                        with c_d:
                            if idx < len(active_codes) - 2 and st.button("▼", key=f"down_{code}_{idx}", use_container_width=True, help="Move Down"):
                                active_codes[idx], active_codes[idx + 2] = active_codes[idx + 2], active_codes[idx]
                                st.session_state.active_order = active_codes
                                st.rerun()

        # ==========================================
        # 4. PERSONAL STUDY NOTES & EXPANDED THEME TAGS
        # ==========================================
        st.markdown("---")
        st.subheader("📝 Personal Study Notes")
        st.write(f"Jot down your thoughts and takeaways for **{verse_query}**:")
        
        user_notes = st.text_area(
            "Study Notes:",
            placeholder="Type your personal insights or observations here...",
            label_visibility="collapsed"
        )

        selected_themes = st.pills(
            "Tag Note Theme:",
            [
                "Faith", "Grace", "Mercy", "Salvation", "Redemption", 
                "Holiness", "Righteousness", "Truth", "Glory",
                "Wisdom", "Guidance", "Obedience", "Discipline", 
                "Patience", "Humility", "Discernment",
                "Peace", "Comfort", "Hope", "Joy", 
                "Strength", "Courage", "Rest", "Refuge", 
                "Healing", "Provision"
            ],
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
elif not active_codes:
    st.warning("Please select at least one translation button above to display your cards.")

st.markdown("---")
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")
