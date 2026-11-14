import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="30 Day Bible Challenge", page_icon="📅", layout="centered"
)

# --- CUSTOM THEME STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1b261c;
        color: #f4f1ea;
    }
    .challenge-header {
        background-color: #2b3a2a;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #4a6b4e;
        margin-bottom: 25px;
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


# --- LOAD BIBLE DATA FOR DROPDOWN READING ---
@st.cache_data
def load_bible_data():
    try:
        return pd.read_csv("KJV.csv")
    except Exception:
        return None


df = load_bible_data()

# --- HEADER ---
st.markdown(
    """
    <div class="challenge-header">
        <h1 style="margin:0;">30 Day Themed Bible Challenge</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Journey through four intentional themes to grow in faith and understanding.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- THEMED 30-DAY CHALLENGE LIST ---
challenge_weeks = {
    "Week 1: Foundations of Faith & Creation": [
        {
            "day": 1,
            "topic": "The Beginning",
            "verse": "Genesis 1:1-3",
            "search_book": "Genesis",
            "chapter": 1,
        },
        {
            "day": 2,
            "topic": "Made in His Image",
            "verse": "Genesis 1:26-28",
            "search_book": "Genesis",
            "chapter": 1,
        },
        {
            "day": 3,
            "topic": "Faith of Abraham",
            "verse": "Genesis 12:1-4",
            "search_book": "Genesis",
            "chapter": 12,
        },
        {
            "day": 4,
            "topic": "The Lord is My Shepherd",
            "verse": "Psalm 23",
            "search_book": "Psalms",
            "chapter": 23,
        },
        {
            "day": 5,
            "topic": "Trusting God's Direction",
            "verse": "Proverbs 3:5-6",
            "search_book": "Proverbs",
            "chapter": 3,
        },
        {
            "day": 6,
            "topic": "The Lamp Unto My Feet",
            "verse": "Psalm 119:105",
            "search_book": "Psalms",
            "chapter": 119,
        },
        {
            "day": 7,
            "topic": "Refuge and Strength",
            "verse": "Psalm 46:1-3",
            "search_book": "Psalms",
            "chapter": 46,
        },
    ],
    "Week 2: The Promised Savior & Life of Christ": [
        {
            "day": 8,
            "topic": "The Prophecy of Hope",
            "verse": "Isaiah 9:6-7",
            "search_book": "Isaiah",
            "chapter": 9,
        },
        {
            "day": 9,
            "topic": "The Birth of Jesus",
            "verse": "Luke 2:10-14",
            "search_book": "Luke",
            "chapter": 2,
        },
        {
            "day": 10,
            "topic": "The Sermon on the Mount",
            "verse": "Matthew 5:1-12",
            "search_book": "Matthew",
            "chapter": 5,
        },
        {
            "day": 11,
            "topic": "Seeking His Kingdom",
            "verse": "Matthew 6:31-34",
            "search_book": "Matthew",
            "chapter": 6,
        },
        {
            "day": 12,
            "topic": "The Good Shepherd",
            "verse": "John 10:11-15",
            "search_book": "John",
            "chapter": 10,
        },
        {
            "day": 13,
            "topic": "God's Great Love",
            "verse": "John 3:16-17",
            "search_book": "John",
            "chapter": 3,
        },
        {
            "day": 14,
            "topic": "The True Vine",
            "verse": "John 15:4-8",
            "search_book": "John",
            "chapter": 15,
        },
    ],
    "Week 3: Grace, Forgiveness, & New Life": [
        {
            "day": 15,
            "topic": "New Creation",
            "verse": "2 Corinthians 5:17-19",
            "search_book": "2 Corinthians",
            "chapter": 5,
        },
        {
            "day": 16,
            "topic": "Saved by Grace",
            "verse": "Ephesians 2:8-10",
            "search_book": "Ephesians",
            "chapter": 2,
        },
        {
            "day": 17,
            "topic": "The Prodigal's Return",
            "verse": "Luke 15:20-24",
            "search_book": "Luke",
            "chapter": 15,
        },
        {
            "day": 18,
            "topic": "Walking in the Light",
            "verse": "1 John 1:7-9",
            "search_book": "1 John",
            "chapter": 1,
        },
        {
            "day": 19,
            "topic": "Fruit of the Spirit",
            "verse": "Galatians 5:22-25",
            "search_book": "Galatians",
            "chapter": 5,
        },
        {
            "day": 20,
            "topic": "The Definition of Love",
            "verse": "1 Corinthians 13:4-8",
            "search_book": "1 Corinthians",
            "chapter": 13,
        },
        {
            "day": 21,
            "topic": "Drawing Near",
            "verse": "James 4:7-10",
            "search_book": "James",
            "chapter": 4,
        },
    ],
    "Week 4: Strength, Peace, & Endurance": [
        {
            "day": 22,
            "topic": "Armor of God",
            "verse": "Ephesians 6:10-13",
            "search_book": "Ephesians",
            "chapter": 6,
        },
        {
            "day": 23,
            "topic": "Peace that Guards the Heart",
            "verse": "Philippians 4:6-7",
            "search_book": "Philippians",
            "chapter": 4,
        },
        {
            "day": 24,
            "topic": "Strength in Weakness",
            "verse": "Philippians 4:11-13",
            "search_book": "Philippians",
            "chapter": 4,
        },
        {
            "day": 25,
            "topic": "Running with Perseverance",
            "verse": "Hebrews 12:1-2",
            "search_book": "Hebrews",
            "chapter": 12,
        },
        {
            "day": 26,
            "topic": "The Power of God's Word",
            "verse": "Hebrews 4:12",
            "search_book": "Hebrews",
            "chapter": 4,
        },
        {
            "day": 27,
            "topic": "A Chosen Generation",
            "verse": "1 Peter 2:9-10",
            "search_book": "1 Peter",
            "chapter": 2,
        },
        {
            "day": 28,
            "topic": "The Alpha and Omega",
            "verse": "Revelation 21:3-6",
            "search_book": "Revelation",
            "chapter": 21,
        },
        {
            "day": 29,
            "topic": "Living in Hope",
            "verse": "Romans 15:13",
            "search_book": "Romans",
            "chapter": 15,
        },
        {
            "day": 30,
            "topic": "Final Benediction",
            "verse": "Revelation 22:20-21",
            "search_book": "Revelation",
            "chapter": 22,
        },
    ],
}

# Flatten for easy lookup
all_challenge_items = [
    item for week in challenge_weeks.values() for item in week
]

# --- INITIALIZE SESSION STATE ---
if "completed_days" not in st.session_state:
    st.session_state.completed_days = {i: False for i in range(1, 31)}

# --- PROGRESS BAR ---
completed_count = sum(st.session_state.completed_days.values())
progress_percent = completed_count / 30

st.subheader(f"Your Progress: {completed_count} / 30 Days Completed")
st.progress(progress_percent)

if completed_count == 30:
    st.balloons()
    st.success(
        "🎉 **Praise God! You have completed the 30 Day Themed Bible Challenge!**"
    )

st.markdown("---")

# --- ONLINE READING DROPDOWN SELECTOR ---
st.subheader("📖 Read Daily Passages Online")
st.write(
    "Select any day from the dropdown below to read the scripture verses directly on the page:"
)

selected_day_option = st.selectbox(
    "Choose a day to read:",
    options=all_challenge_items,
    format_func=lambda x: f"Day {x['day']}: {x['topic']} ({x['verse']})",
)

if selected_day_option and df is not None and not df.empty:
    # Filter CSV for the selected book and chapter
    b_name = selected_day_option["search_book"]
    c_num = selected_day_option["chapter"]

    # Match book and chapter flexibly
    verses_to_show = df[
        (df["Book"].str.contains(b_name, case=False, na=False))
        & (df["Chapter"] == c_num)
    ]

    st.markdown(
        f"""
        <div class="card">
            <h3 style="margin-top:0; color:#b7d5b8;">Day {selected_day_option['day']}: {selected_day_option['topic']}</h3>
            <p><b>Target Passage: {selected_day_option['verse']}</b></p>
            <hr style="border-color: #4a6b4e;">
    """,
        unsafe_allow_html=True,
    )

    if not verses_to_show.empty:
        for _, row in verses_to_show.iterrows():
            v_num = row.get("Verse", row.get("verse", ""))
            v_text = row.get("Text", row.get("text", ""))
            st.markdown(
                f"<p><sup>{v_num}</sup> {v_text}</p>", unsafe_allow_html=True
            )
    else:
        st.info(
            f"Displaying reference: {selected_day_option['verse']} (Full chapter text loading fallback)."
        )

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📋 Themed Daily Reading Checklist")

# --- DISPLAY THEMED WEEKS AND CHECKLISTS ---
for week_title, days in challenge_weeks.items():
    st.markdown(f"### **{week_title}**")
    for item in days:
        day_num = item["day"]
        col1, col2 = st.columns([0.1, 0.9])

        with col1:
            is_checked = st.checkbox(
                f"Day {day_num}",
                value=st.session_state.completed_days[day_num],
                key=f"challenge_day_{day_num}",
                label_visibility="collapsed",
            )
            st.session_state.completed_days[day_num] = is_checked

        with col2:
            st.markdown(
                f"**Day {day_num}: {item['topic']}** — *{item['verse']}*"
            )
    st.markdown("")

# --- RESET BUTTON ---
if st.button("Reset Challenge Progress"):
    for k in st.session_state.completed_days:
        st.session_state.completed_days[k] = False
    st.rerun()
