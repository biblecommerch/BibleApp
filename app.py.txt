# Import the pandas library and give it the short nickname 'pd'
# Pandas is the tool Python uses to open and read spreadsheet files like CSVs.
import pandas as pd

# Import the streamlit library and give it the short nickname 'st'
# Streamlit is the tool that turns our Python code into a live website.
import streamlit as st

# Set the main large title that appears at the very top of your webpage
st.title("📖 My Bible Verse Search Tool")

# Display a subtitle or introductory helper text right under the title
st.write(
    "Search through your CSV database instantly by keyword, book, or topic!"
)


# Define a function to load our data
# The '@st.cache_data' decorator tells Streamlit to save the CSV in memory
# so the app loads instantly on future clicks instead of reloading every time.
@st.cache_data
def load_data():
  # Read the CSV file into a data table (DataFrame)
  return pd.read_csv("KJV.csv")


# Run our function and store the loaded spreadsheet table inside the variable 'df'
df = load_data()

# Create an interactive text input box on the website for the user to type in
search_query = st.text_input(
    "Enter a keyword or topic (e.g., *love*, *faith*, *peace*):"
)

# Check if the user has actually typed something into the search box
if search_query:
  # Filter the spreadsheet table:
  # 1. Look at text columns.
  # 2. Check if they contain the search word (ignoring upper/lower case).
  # 3. Keep any row where a match is found.
  results = df[
      df.select_dtypes(include=["object"])
      .apply(lambda col: col.str.contains(search_query, case=False, na=False))
      .any(axis=1)
  ]

  # Display a count of how many matching verses were found on the page
  st.write(f"Found **{len(results)}** results for *'{search_query}'*:")

  # Display all the matching rows in a clean, scrollable spreadsheet table on the site
  st.dataframe(results)

else:
  # If the search box is empty, show a helpful blue info box telling the user what to do
  st.info("Type a word above to search your Bible database.")