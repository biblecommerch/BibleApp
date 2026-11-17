import streamlit as st
import pandas as pd
import os
from datetime import datetime
from styles import apply_global_styles
from auth_helper import render_sidebar_auth

st.set_page_config(
    page_title="Bible Focus — Home",
    page_icon="📖",
    layout="centered"
)

apply_global_styles()
render_sidebar_auth()

# ==========================================
# HELPER FUNCTIONS
# ==========================================
@st.cache_data
def load_bible_data(csv_filename):
    path = os.path.join("data", csv_filename)
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

def get_daily_verse_index():
    day_of_year = datetime.now().timetuple().tm_yday
    return day_of_year

def generate_verse_reflection(book_name: str, chap: int, v_num: int, verse_text: str) -> str:
    t = verse_text.lower()
    b = book_name.strip().lower()
    
    if any(w in t for w in ["rich", "gold", "silver", "bless", "blessed", "increase", "prosper", "inheritance", "land"]):
        return (
            f"In {book_name} {chap}:{v_num}, we see how God's provision and blessing unfold in the lives of His people. "
            f"True abundance isn't just about material increase—it's a reminder that everything we hold comes from God's faithful hand "
            f"and is meant to be stewarded with gratitude, humility, and generosity."
        )
    elif any(w in t for w in ["fear not", "afraid", "dismayed", "trouble", "anxious", "peace", "refuge", "shield", "strength"]):
        return (
            f"{book_name} {chap}:{v_num} speaks directly to moments when worry or uncertainty tries to take hold. "
            f"God doesn't ask you to muster up strength on your own; He invites you to anchor your heart in His steady presence."
        )
    elif any(w in t for w in ["love", "charity", "kindness", "mercy", "forgive", "compassion", "grace"]):
        return (
            f"The heart of {book_name} {chap}:{v_num} points us toward the character of God—steadfast in mercy, rich in grace, "
            f"and overflowing with love."
        )
    elif any(w in t for w in ["wisdom", "understanding", "knowledge", "teach", "counsel", "way", "path", "light", "truth"]):
        return (
            f"Scripture in {book_name} {chap}:{v_num} reminds us that true wisdom begins with seeking God's perspective above our own."
        )
    elif any(w in t for w in ["pray", "prayer", "cry", "heard", "call upon", "ask", "seek"]):
        return (
            f"{book_name} {chap}:{v_num} is an open invitation to bring every burden, question, and thank-you directly before God."
        )
    elif any(w in t for w in ["faith", "believe", "trust", "hope", "promise", "covenant", "faithful"]):
        return (
            f"In {book_name} {chap}:{v_num}, we're called to hold fast to God's promises even before we see the full picture."
        )
    elif any(w in t for w in ["sin", "repent", "cleanse", "righteous", "holy", "obey", "command", "law", "statutes"]):
        return (
            f"{book_name} {chap}:{v_num} calls us back to a life aligned with God's heart and holiness."
        )
        
    return (
        f"Every detail in {book_name} {chap}:{v_num} sits inside God's larger story of redemption and faithfulness. "
        f"Take a quiet moment to read this verse in its surrounding chapter today."
    )

# ==========================================
# HEADER SECTION
# ==========================================
st.markdown(
    """
    <div style="background-color: #2b3a2a; padding: 30px; border-radius: 10px; text-align: center; border: 1px solid #4a6b4e; margin-bottom: 25px;">
        <h1 style="margin:0; color: #f4f1ea;">Welcome to Your Bible App</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Your daily space for scripture search, reflection, and reading plans.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# QUICK NAVIGATION BUTTONS
# ==========================================
st.markdown(
    """
    ### Where would you like to go?
    - 🔍 **[Bible Search](https://kjv-bible.streamlit.app/~/+/bible_search)**: Look up verses across the King James Version easily.
    - ⚖️ **[Bible Translations](https://kjv-bible.streamlit.app/~/+/translations)**: Compare and study your favorite verses side by side.
    - 📅 **[30 Day Challenge](https://kjv-bible.streamlit.app/~/+/thirty_day_challenge)**: Build a daily habit of reading God's Word through our curated reading guide.
    """
)

st.write("")

# ==========================================
# DAILY VERSE SECTION
# ==========================================
st.markdown("### ✨ Daily Verse")

kjv_master = load_bible_data("KJV.csv")
if kjv_master is not None and not kjv_master.empty:
    idx = get_daily_verse_index() % len(kjv_master)
    daily_row = kjv_master.iloc[idx]
    
    book = daily_row.get("Book", "Genesis")
    chapter = daily_row.get("Chapter", 1)
    target_verse = 1
    for col_candidate in ["Verse", "verse", "v"]:
        if col_candidate in daily_row.index:
            target_verse = daily_row[col_candidate]
            break
            
    v_col = None
    t_col = None
    for col in kjv_master.columns:
        if str(col).strip().lower() in ["verse", "v"]:
            v_col = col
        if str(col).strip().lower() in ["text", "content", "verse_text"]:
            t_col = col
            
    if v_col is None:
        v_col = kjv_master.columns[1] if len(kjv_master.columns) > 1 else kjv_master.columns[0]
    if t_col is None:
        t_col = kjv_master.columns[2] if len(kjv_master.columns) > 2 else kjv_master.columns[1]
        
    verse_num = daily_row.get(v_col, target_verse)
    text = daily_row.get(t_col, "")
    ver_code = "KJV"

    reflection_text = generate_verse_reflection(str(book), int(chapter), int(verse_num), str(text))

    st.markdown(
        f"""
        <div class="card" style="background-color: #f9f6f0; padding: 20px; border-radius: 8px; border: 1px solid #e2d9c8;">
        <p style="font-size: 1.15em; color: #2c221e;"><b>"{text}"</b></p>
        <p style="margin-bottom: 12px; color: #5c4b37;">— {book} {chapter}:{verse_num} ({ver_code})</p>
        <hr style="border: 0; border-top: 1px solid #e2d9c8; margin: 10px 0;">
        <p style="margin: 0; font-size: 0.95em; color: #2c221e;">
            <b>Daily Reflection &amp; Encouragement:</b> {reflection_text}
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# FOOTER SECTION
# ==========================================
st.markdown("---")
st.info("💡 **Tip:** Use the sidebar menu to navigate between your study tools, personal notes, and reading challenges.")
