import streamlit as st
import pandas as pd

# Title
st.title("🔍 FSN Search Query Matcher")

# File uploader
uploaded_file = st.file_uploader("📁 Upload 'selection_master.csv'", type="csv")

# instock_file = st.file_uploader("📁 Upload 'instock_new.csv'", type="csv")

# ds_master = st.file_uploader("📁 Upload 'ds_master.csv'", type="csv")


# Initialize DataFrame
master = pd.DataFrame()

if uploaded_file is not None:
    try:
        master = pd.read_csv(uploaded_file)
        if not {'FSN', 'Title', 'Brand'}.issubset(master.columns):
            st.error("❌ CSV must contain 'FSN', 'Title' and 'Brand ' columns.")
        else:
            st.success("✅ File uploaded successfully!")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

# Search input
if not master.empty:
    user_input = st.text_area(
        "🔎 Enter search query or multiple keywords (comma-separated):",
        placeholder="e.g., raincoat, mosquito refill, ponds powder"
    )

    if st.button("Search"):
        queries = [q.strip() for q in user_input.split(',') if q.strip()]

        if not queries:
            st.warning("⚠️ Please enter at least one valid keyword.")
        else:
            results = pd.DataFrame()

            for query in queries:
                matched = master[master['Title'].str.lower().str.contains(query.lower(), na=False)].copy()
                matched.insert(0, "search_query", query)
                results = pd.concat([results, matched], ignore_index=True)

            if results.empty:
                st.warning("🔍 No matches found.")
            else:
                unique_results = results.drop_duplicates()
                st.success(f"✅ Found {len(unique_results)} matches.")
                st.dataframe(results[['search_query', 'Title', 'FSN', 'Brand']])

                # Download buttons
                csv = results.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Download All Matches CSV", csv, "matched_fsn_results.csv", "text/csv")

                # unique_results = results.drop_duplicates()
                csv_unique = unique_results.to_csv(index=False).encode('utf-8')
                st.download_button("⬇️ Download Unique Matches CSV", csv_unique, "matched_unique_fsn_results.csv", "text/csv")
