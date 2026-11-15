from datetime import datetime
import pandas as pd
import streamlit as st
from styles import apply_global_styles

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Bible Focus", page_icon="📖", layout="centered")
apply_global_styles()

# --- LOAD BIBLE DATA ---
@st.cache_data
def load_bible_data():
    try:
        return pd.read_csv("KJV.csv")
    except Exception:
        return None

df = load_bible_data()

# ==========================================
# 1. HEADER & BIBLE VERSIONS
# ==========================================
st.markdown(
    """
    <div class="header-box">
        <h1 style="margin:0;">Bible Focus</h1>
        <p style="margin-top:5px;">Read, Research, &amp; Stay Centered on God's Word</p>
    </div>
    """,
    unsafe_allow_html=True,
)

ver_col1, ver_col2, ver_col3 = st.columns([1, 2, 1])
with ver_col2:
    version = st.selectbox(
        "Select Bible Translation:",
        ["KJV (King James Version)", "NKJV (Coming Soon)", "ESV (Coming Soon)", "NIV (Coming Soon)"],
        index=0,
    )

# ==========================================
# 2. AUTOMATIC DAILY VERSE
# ==========================================
st.markdown("### Daily Verse")
if df is not None and not df.empty:
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
            <p style="margin: 0;">— {book} {chapter}:{verse_num} (KJV)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="card">
            <p><b>"The Lord is my strength and my shield; my heart trusted in him, and I am helped."</b></p>
            <p style="margin: 0;">— Psalm 28:7 (KJV)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# 3. LIVE BIBLE SEARCH
# ==========================================
st.markdown("---")
st.subheader("Bible Search")
st.write("Type any keyword, phrase, or passage reference below to search directly through the King James Bible:")
search_query = st.text_input("Search the Bible:", placeholder="e.g., John 3:16, love, hope, strength...")

if search_query:
    if df is not None and not df.empty:
        results = df[
            df.apply(
                lambda row: row.astype(str).str.contains(search_query, case=False).any(),
                axis=1,
            )
        ]
        if not results.empty:
            st.success(f"Found {len(results)} matching verse(s):")
            st.dataframe(results, use_container_width=True)
        else:
            st.warning(f"No verses found matching '{search_query}'.")
    else:
        st.error("Bible dataset (KJV.csv) could not be loaded. Please ensure KJV.csv is in your GitHub repository.")

# ==========================================
# 4. BIBLE ABOUT... (HIGH SEARCHED BUBBLES)
# ==========================================
st.markdown("---")
st.subheader("Bible About...")
st.write("Tap a topic below to explore top verses:")

topics = [
    "Anxiety & Worry",
    "Faith",
    "Love",
    "Healing",
    "Strength",
    "Forgiveness",
    "Peace",
    "Marriage & Family",
    "Hope",
    "Prayer",
]
selected_topic = st.pills("Popular Topics", topics, selection_mode="single")

if selected_topic:
    st.info(f"**Top Verses About {selected_topic}:** *(Placeholder — we will connect your curated {selected_topic} verse list here!)*")

# ==========================================
# 5. POPULAR VERSES & 30 DAY CHALLENGE
# ==========================================
st.markdown("---")
col_pop, col_chal = st.columns(2)

with col_pop:
    with st.container(border=True):
        st.markdown("### Popular Verses")
        st.markdown(
            """
            * **John 3:16** — *For God so loved the world...*
            * **Philippians 4:13** — *I can do all things through Christ...*
            * **Jeremiah 29:11** — *For I know the thoughts that I think...*
            * **Psalm 23:1** — *The LORD is my shepherd; I shall not want.*
            """
        )
        st.button("More Popular Verses (Coming Soon)", disabled=True, use_container_width=True)

with col_chal:
    with st.container(border=True):
        st.markdown("### 30 Day Bible Challenge")
        st.write("Build a daily habit in Scripture with a guided 30-day reading path and progress tracker.")
        if st.button("Open 30 Day Challenge", use_container_width=True):
            st.switch_page("pages/thirty_day_challenge.py")

# ==========================================
# 6. OLD & NEW TESTAMENT DIRECTORIES
# ==========================================
st.markdown("---")
st.subheader("Scripture Directories")
dir_col1, dir_col2 = st.columns(2)

with dir_col1:
    with st.container(border=True):
        st.markdown("### Old Testament Directory")
        st.write("Browse all 39 books from Genesis to Malachi by Law, History, Poetry, and Prophets.")
        st.button("Old Testament (Coming Soon)", disabled=True, use_container_width=True)

with dir_col2:
    with st.container(border=True):
        st.markdown("### New Testament Directory")
        st.write("Browse all 27 books from Matthew to Revelation by Gospels, History, Epistles, and Prophecy.")
        st.button("New Testament (Coming Soon)", disabled=True, use_container_width=True)

# ==========================================
# 7. INTERACTIVE: QUIZ, GAME & HOLY DAYS
# ==========================================
st.markdown("---")
st.subheader("Interactive & Calendar")
int_col1, int_col2, int_col3 = st.columns(3)

with int_col1:
    with st.container(border=True):
        st.markdown("### Bible Quiz")
        st.write("Test your Scripture knowledge with chapter & topic quizzes.")
        st.button("Quiz (Soon)", disabled=True, use_container_width=True)

with int_col2:
    with st.container(border=True):
        st.markdown("### Bible Game")
        st.write("Who Said It? Verse Scramble, & Scripture Trivia challenges.")
        st.button("Game (Soon)", disabled=True, use_container_width=True)

with int_col3:
    with st.container(border=True):
        st.markdown("### Calendar & Holy Days")
        st.write("Biblical feasts, Christian calendar dates, & seasonal studies.")
        st.button("Calendar (Soon)", disabled=True, use_container_width=True)

# ==========================================
# 8. TOP BLOGS & EMAIL NEWSLETTER
# ==========================================
st.markdown("---")
blog_col, news_col = st.columns(2)

with blog_col:
    with st.container(border=True):
        st.markdown("### Top Blogs")
        st.write("Read our latest articles, devotions, and community discussions on Bible Com Blog.")
        st.link_button("Visit Bible Com Blog", "https://www.biblecomblog.com", use_container_width=True)

with news_col:
    with st.container(border=True):
        st.markdown("### Join Email Newsletter")
        st.write("Stay updated with daily verses, new studies, and site additions.")
        email_input = st.text_input("Your Email Address:", placeholder="you@example.com", label_visibility="collapsed")
        if st.button("Stay Updated", use_container_width=True):
            if email_input:
                st.success("Thanks for subscribing! *(Placeholder — connect email service later)*")
            else:
                st.warning("Please enter an email address first.")

# ==========================================
# 9. UPCOMING SITE PAGES (PLACEHOLDERS)
# ==========================================
st.markdown("---")
st.subheader("Explore Bible Focus Pages")
st.write("Upcoming sections currently in development:")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    with st.container(border=True):
        st.markdown("#### Bible Research")
        st.caption("Bible Study • Reading Plans • Scripture AI & Commentary DB • Bible Maps • Timelines")
        st.button("Coming Soon", disabled=True, key="p_res", use_container_width=True)

with p_col2:
    with st.container(border=True):
        st.markdown("#### Listen to the Bible")
        st.caption("Audio Bible Player • Chapter Narration • Background Study Listening")
        st.button("Coming Soon", disabled=True, key="p_lis", use_container_width=True)

with p_col3:
    with st.container(border=True):
        st.markdown("#### Prayer Page")
        st.caption("Guided Prayers • Submit a Prayer Request • Prayer Ideas & Prompts")
        st.button("Coming Soon", disabled=True, key="p_pray", use_container_width=True)

p_col4, p_col5, p_col6 = st.columns(3)

with p_col4:
    with st.container(border=True):
        st.markdown("#### Bible Blog & Commentary")
        st.caption("Articles • Reader Discussions • Personal Bible Commentary")
        st.link_button("Open Blog", "https://www.biblecomblog.com", use_container_width=True)

with p_col5:
    with st.container(border=True):
        st.markdown("#### My Mission")
        st.caption("Our Vision • Why Bible Focus Is Free • Support & Donations")
        st.button("Coming Soon", disabled=True, key="p_mis", use_container_width=True)

with p_col6:
    with st.container(border=True):
        st.markdown("#### Contact Me")
        st.caption("Social Media Links • Questions • Feedback & Contact Form")
        st.button("Coming Soon", disabled=True, key="p_con", use_container_width=True)

# ==========================================
# 10. SUPPORT THE PROJECT: SHOP MEL'S GOODS
# ==========================================
st.markdown("---")
st.subheader("Support Bible Focus — Shop Mel's Goods")
with st.container(border=True):
    st.markdown("### Christian Tees & Faith-Inspired Finds")
    st.write(
        "Every purchase from Mel's Goods helps keep Bible Focus free and growing. "
        "Browse our collection of Christian T-shirts and unique goods directly in our store:"
    )
    st.link_button(
        "Shop Christian Tees on eBay",
        "https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=mels_goods&store_name=shopmelsgoods&_oac=1&store_cat=49634617018",
        use_container_width=False,
    )
