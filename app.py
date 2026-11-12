# ==========================================
# SECTION 1: IMPORTS & TOOL SETUP
# ==========================================
# Import the pandas library (nickname 'pd') to read and handle CSV spreadsheets.
import pandas as pd

# Import the streamlit library (nickname 'st') to build our web app interface.
import streamlit as st


# ==========================================
# SECTION 2: DATA LOADING FUNCTION
# ==========================================
# The '@st.cache_data' decorator saves the CSV file in your app's memory
# so it doesn't have to reload from scratch every time someone searches.
@st.cache_data
def load_data():
  # Open and read your Bible CSV file
  return pd.read_csv("KJV.csv")


# Run our function right away to load the spreadsheet into a variable called 'df'
df = load_data()


# ==========================================
# SECTION 3: WEB PAGE LAYOUT & TITLE
# ==========================================
# Set the main large title displayed at the top of your webpage
st.title("📖 My Bible Verse Search Tool")

# Display introductory helper text right under the title
st.write(
    "Search through your CSV database instantly by keyword, book, or topic!"
)


# ==========================================
# SECTION 4: SEARCH BAR & INPUT
# ==========================================
# Create an interactive text input box for visitors to type keywords into
search_query = st.text_input(
    "Enter a keyword or topic (e.g., *love*, *faith*, *peace*):"
)


# ==========================================
# SECTION 5: FILTERING & DISPLAY LOGIC
# ==========================================
# Check if the user has typed something into the search box
if search_query:
  # Filter the spreadsheet table:
  # - Look through all text columns
  # - Check if they contain the search word (ignoring upper/lower case)
  # - Keep every matching row
  results = df[
      df.select_dtypes(include=["object"])
      .apply(lambda col: col.str.contains(search_query, case=False, na=False))
      .any(axis=1)
  ]

  # Show how many total matching verses were found
  st.write(f"Found **{len(results)}** results for *'{search_query}'*:")

  # Display the matched rows inside a clean, scrollable website table
  st.dataframe(results)

else:
  # If the search box is completely empty, show a helpful info box
  st.info("Type a word above to search your Bible database.")
