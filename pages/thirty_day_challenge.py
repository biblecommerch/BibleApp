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
    .day-box {
        background-color: #2b3a2a;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #4a6b4e;
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HEADER ---
st.markdown(
    """
    <div class="challenge-header">
        <h1 style="margin:0;">30 Day Bible Challenge</h1>
        <p style="margin-top:5px; color: #b7d5b8;">Build a daily habit of reading God's Word, one day at a time.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- 30 DAY READING LIST ---
challenge_days = [
    {"day": 1, "topic": "Creation & Beginnings", "verse": "Genesis 1:1-3"},
    {"day": 2, "topic": "The Fall & Promise", "verse": "Genesis 3:15"},
    {"day": 3, "topic": "Faith of Abraham", "verse": "Genesis 12:1-3"},
    {"day": 4, "topic": "The Lord is My Shepherd", "verse": "Psalm 23"},
    {"day": 5, "topic": "Trust in the Lord", "verse": "Proverbs 3:5-6"},
    {"day": 6, "topic": "Awaiting the Savior", "verse": "Isaiah 9:6"},
    {"day": 7, "topic": "The Birth of Jesus", "verse": "Luke 2:1-14"},
    {"day": 8, "topic": "The Sermon on the Mount", "verse": "Matthew 5:1-12"},
    {"day": 9, "topic": "The Lord's Prayer", "verse": "Matthew 6:9-13"},
    {"day": 10, "topic": "Seeking First His Kingdom", "verse": "Matthew 6:33"},
    {"day": 11, "topic": "The Good Samaritan", "verse": "Luke 10:25-37"},
    {"day": 12, "topic": "The Prodigal Son", "verse": "Luke 15:11-32"},
    {"day": 13, "topic": "God's Great Love", "verse": "John 3:16-17"},
    {"day": 14, "topic": "The Bread of Life", "verse": "John 6:35"},
    {"day": 15, "topic": "The True Vine", "verse": "John 15:1-8"},
    {"day": 16, "topic": "The Fruit of the Spirit", "verse": "Galatians 5:22-23"},
    {"day": 17, "topic": "Faith Definition", "verse": "Hebrews 11:1-3"},
    {"day": 18, "topic": "Armor of God", "verse": "Ephesians 6:10-18"},
    {"day": 19, "topic": "Love is Patient", "verse": "1 Corinthians 13:4-7"},
    {"day": 20, "topic": "Peace That Passes Understanding", "verse": "Philippians 4:6-7"},
    {"day": 21, "topic": "Strength in Weakness", "verse": "Philippians 4:13"},
    {"day": 22, "topic": "New Creation", "verse": "2 Corinthians 5:17"},
    {"day": 23, "topic": "Saved by Grace", "verse": "Ephesians 2:8-9"},
    {"day": 24, "topic": "The Word of God", "verse": "Hebrews 4:12"},
    {"day": 25, "topic": "Drawing Near to God", "verse": "James 4:8"},
    {"day": 26, "topic": "A Chosen Generation", "verse": "1 Peter 2:9"},
    {"day": 27, "topic": "Walking in the Light", "verse": "1 John 1:5-7"},
    {"day": 28, "topic": "God is Love", "verse": "1 John 4:7-12"},
    {"day": 29, "topic": "The Alpha and Omega", "verse": "Revelation 21:1-6"},
    {"day": 30, "topic": "Final Benediction", "verse": "Revelation 22:20-21"},
]

# --- INITIALIZE SESSION STATE ---
if "completed_days" not in st.session_state:
    st.session_state.completed_days = {i: False for i in range(1, 31)}

# --- PROGRESS BAR TRACKING ---
completed_count = sum(st.session_state.completed_days.values())
progress_percent = completed_count / 30

st.subheader(f"Your Progress: {completed_count} / 30 Days Completed")
st.progress(progress_percent)

if completed_count == 30:
    st.balloons()
    st.success(
        "🎉 **Praise God! You have completed the 30 Day Bible Challenge!**"
    )

st.markdown("---")
st.markdown("### Daily Reading Checklist")
st.write(
    "Check off each day as you read and reflect on the scripture passage:"
)

# --- DISPLAY INTERACTIVE CHECKLIST ---
for item in challenge_days:
    day_num = item["day"]
    col1, col2 = st.columns([0.15, 0.85])

    with col1:
        # Checkbox state bound to session state
        is_checked = st.checkbox(
            f"Day {day_num}",
            value=st.session_state.completed_days[day_num],
            key=f"day_{day_num}",
            label_visibility="collapsed",
        )
        st.session_state.completed_days[day_num] = is_checked

    with col2:
        st.markdown(
            f"**Day {day_num}: {item['topic']}** — *{item['verse']}*"
        )

# --- RESET BUTTON ---
if st.button("Reset Challenge Progress"):
    for k in st.session_state.completed_days:
        st.session_state.completed_days[k] = False
    st.rerun()
