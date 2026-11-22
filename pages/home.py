# ==========================================
# IMPORTS & DEPENDENCIES
# ==========================================
from datetime import datetime
from pathlib import Path
import re
import pandas as pd
import streamlit as st
from styles import apply_global_styles

# Import custom auth helper functions to manage sidebar login, user sessions, and database saves
from auth_helper import render_sidebar_auth, require_email_to_save, get_supabase


# ==========================================
# PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(page_title="Mel's Bible Apps", page_icon="📖", layout="centered")
apply_global_styles()


# ==========================================
# SIDEBAR ACCOUNT & SITE UPDATES MANAGER
# ==========================================
# Renders the email login/status box and the Privacy Policy link in the left sidebar on every page
try:
    render_sidebar_auth()
except Exception as e:
    st.sidebar.warning("Sidebar account panel is temporarily unavailable.")
    st.sidebar.caption(f"Sidebar notice: {e}")


# ==========================================
# LOAD BIBLE DATA & TRANSLATION MAP
# ==========================================
# Dictionary connecting user-facing dropdown labels to exact CSV filenames stored in GitHub
TRANSLATIONS = {
    "KJV (King James Version)": "KJV.csv",
    "ASV (American Standard Version)": "ASV.csv",
    "BSB (Berean Standard Bible)": "BSB.csv",
    "YLT (Young's Literal Translation)": "YLT.csv",
    "BBE (Bible in Basic English)": "BBE.csv",
    "DRC (Douay-Rheims Catholic Bible)": "DRC.csv",
}

def _resolve_data_path(csv_filename):
    """Checks current working directory first, then repository root if running from pages/."""
    local_path = Path(csv_filename)
    if local_path.exists():
        return local_path
    root_path = Path(__file__).resolve().parent.parent / csv_filename
    return root_path if root_path.exists() else local_path

@st.cache_data
def load_bible_data(csv_filename):
    """
    Loads the chosen Bible CSV file into memory once and caches it.
    Caching ensures switching translations later is instant without reloading from disk.
    """
    try:
        resolved = _resolve_data_path(csv_filename)
        loaded_df = pd.read_csv(resolved)
        loaded_df.columns = [col.strip() for col in loaded_df.columns]
        return loaded_df
    except Exception:
        return None


def _is_valid_email(email):
    return bool(email and "@" in email and "." in email.split("@")[-1])


# ==========================================
# 1. HEADER & BIBLE VERSIONS
# ==========================================
# Renders the main title header box at the top of the home page
st.markdown(
    """
    <div class="header-box">
        <h1 style="margin:0;">Mel's Bible Apps</h1>
        <p style="margin-top:5px;">Read, Research, &amp; Stay Centered on God's Word</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Preserve the user's chosen translation across different pages using Streamlit session state
if "selected_version" not in st.session_state:
    st.session_state.selected_version = "KJV (King James Version)"

ver_col1, ver_col2, ver_col3 = st.columns([1, 2, 1])
with ver_col2:
    version = st.selectbox(
        "Select Bible Translation:",
        options=list(TRANSLATIONS.keys()),
        index=list(TRANSLATIONS.keys()).index(st.session_state.selected_version),
    )

# Save the user's latest translation selection and extract the short code (e.g., "KJV", "BSB")
st.session_state.selected_version = version
ver_code = version.split(" ")[0]

# Load only the selected translation DataFrame into memory for use across the rest of the page
df = load_bible_data(TRANSLATIONS[version])


# ==========================================
# 2. DAILY VERSE + COMMENTARY / ENCOURAGEMENT
# ==========================================
st.markdown("### ✨ Daily Verse")


def _safe_int(val, default=1):
    """Safely converts a chapter or verse cell to int without crashing on blanks/text."""
    num = pd.to_numeric(val, errors="coerce")
    return int(num) if pd.notna(num) else default


def _find_col(columns, candidates):
    """Finds the first matching column name case-insensitively."""
    col_map = {str(c).strip().lower(): c for c in columns}
    for cand in candidates:
        if cand.lower() in col_map:
            return col_map[cand.lower()]
    return None


if df is not None and not df.empty:
    day_of_year = datetime.now().timetuple().tm_yday
    kjv_master = load_bible_data("KJV.csv")

    # 1. Pick today's target (Book, Chapter, Verse) from KJV.csv when available
    if kjv_master is not None and not kjv_master.empty:
        m_book_col = _find_col(kjv_master.columns, ["Book", "book"])
        m_chap_col = _find_col(kjv_master.columns, ["Chapter", "chapter"])
        m_verse_col = _find_col(kjv_master.columns, ["Verse", "verse"])

        master_row = kjv_master.iloc[day_of_year % len(kjv_master)]
        target_book = str(master_row[m_book_col]).strip() if m_book_col else ""
        target_chap = _safe_int(master_row[m_chap_col], 1) if m_chap_col else 1
        target_verse = _safe_int(master_row[m_verse_col], 1) if m_verse_col else 1
    else:
        # Fallback if KJV.csv cannot be loaded: pick from active df by day_of_year
        d_book_col = _find_col(df.columns, ["Book", "book"])
        d_chap_col = _find_col(df.columns, ["Chapter", "chapter"])
        d_verse_col = _find_col(df.columns, ["Verse", "verse"])

        fallback_row = df.iloc[day_of_year % len(df)]
        target_book = str(fallback_row[d_book_col]).strip() if d_book_col else ""
        target_chap = _safe_int(fallback_row[d_chap_col], 1) if d_chap_col else 1
        target_verse = _safe_int(fallback_row[d_verse_col], 1) if d_verse_col else 1

    # 2. Match that exact Book, Chapter, and Verse in the currently selected translation (df)
    book_col = _find_col(df.columns, ["Book", "book"])
    chap_col = _find_col(df.columns, ["Chapter", "chapter"])
    verse_col = _find_col(df.columns, ["Verse", "verse"])
    text_col = _find_col(df.columns, ["Text", "text"])

    daily_row = None
    if book_col and chap_col and verse_col and text_col and target_book:
        chap_series = pd.to_numeric(df[chap_col], errors="coerce")
        verse_series = pd.to_numeric(df[verse_col], errors="coerce")
        book_series = df[book_col].astype(str).str.strip().str.lower()

        matched = df[
            (book_series == target_book.lower())
            & (chap_series == target_chap)
            & (verse_series == target_verse)
        ]
        if not matched.empty:
            daily_row = matched.iloc[0]

    # Fallback to day_of_year % len(df) if the reference isn't found in the active CSV
    if daily_row is None:
        daily_row = df.iloc[day_of_year % len(df)]

    book = daily_row[book_col] if book_col else target_book
    chapter = daily_row[chap_col] if chap_col else target_chap
    verse_num = daily_row[verse_col] if verse_col else target_verse
    text = daily_row[text_col] if text_col else ""

    st.markdown(
        f"""
        <div class="card">
            <p style="font-size: 1.15em;"><b>"{text}"</b></p>
            <p style="margin-bottom: 12px;">— {book} {chapter}:{verse_num} ({ver_code})</p>
            <hr style="border: 0; border-top: 1px solid #E2D9C8; margin: 10px 0;">
            <p style="margin: 0; font-size: 0.95em;">
                <b>Daily Reflection &amp; Encouragement:</b> Every passage of Scripture reminds us of God's faithfulness and purposeful guidance. Take a quiet moment today to reflect on how {book} {chapter}:{verse_num} speaks into your current walk, trusting that God's Word brings clarity and strength for each step ahead.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # Fallback default card if dataset fails to load
    st.markdown(
        """
        <div class="card">
            <p style="font-size: 1.15em;"><b>"The Lord is my strength and my shield; my heart trusted in him, and I am helped."</b></p>
            <p style="margin-bottom: 12px;">— Psalm 28:7 (KJV)</p>
            <hr style="border: 0; border-top: 1px solid #E2D9C8; margin: 10px 0;">
            <p style="margin: 0; font-size: 0.95em;">
                <b>Daily Reflection &amp; Encouragement:</b> When life feels heavy, God does not ask you to carry it alone. Lean on Him as both your strength to endure and your shield to protect your peace today.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# 3. DUAL BIBLE SEARCH (PASSAGE + KEYWORD)
# ==========================================
st.markdown("---")
st.subheader("🔍 Bible Search")

search_tab1, search_tab2 = st.tabs([
    "📖 Passage / Verse Lookup (e.g., Romans 8:28)",
    "🔎 Keyword & Phrase Search"
])

# Tab 1: Exact Passage Lookup
with search_tab1:
    passage_input = st.text_input(
        "Enter a specific Book, Chapter, and Verse:",
        placeholder="e.g., Romans 8:28, John 3:16, Psalm 23:1...",
        key="passage_lookup",
    )
    if passage_input:
        if df is not None and not df.empty:
            match = re.match(r"^\s*([1-3]?\s*[A-Za-z]+)\s+(\d+):(\d+)\s*$", passage_input)
            book_col = "Book" if "Book" in df.columns else "book"
            chap_col = "Chapter" if "Chapter" in df.columns else "chapter"
            verse_col = "Verse" if "Verse" in df.columns else "verse"
            text_col = "Text" if "Text" in df.columns else "text"

            if match:
                b_name, c_num, v_num = match.group(1).strip(), int(match.group(2)), int(match.group(3))
                found = df[
                    (df[book_col].astype(str).str.lower() == b_name.lower()) &
                    (df[chap_col].astype(int) == c_num) &
                    (df[verse_col].astype(int) == v_num)
                ]
                if not found.empty:
                    row = found.iloc[0]
                    st.markdown(
                        f"""
                        <div class="card">
                            <p style="font-size: 1.1em;"><b>"{row[text_col]}"</b></p>
                            <p style="margin: 0;">— {row[book_col]} {row[chap_col]}:{row[verse_col]} ({ver_code})</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning(f"Could not find '{passage_input}' in {ver_code}. Check book spelling and verse numbers.")
            else:
                st.info("Tip: Use the format **Book Chapter:Verse** (for example: `Romans 8:28`).")
        else:
            st.error(f"Bible dataset ({TRANSLATIONS[version]}) could not be loaded.")

# Tab 2: Keyword & Phrase Search Across Active Translation
with search_tab2:
    keyword_input = st.text_input(
        f"Search by word or phrase across the entire {ver_code} Bible:",
        placeholder="e.g.,
