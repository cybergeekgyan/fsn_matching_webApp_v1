import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()  # Clean column names
        required_columns = {'FSN', 'Title', 'Brand'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"CSV must contain columns: {required_columns}")
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return pd.DataFrame()

def search_fsn(df, query_string):
    queries = [q.strip().lower() for q in query_string.split(',') if q.strip()]
    if not queries:
        print("⚠️ Please provide at least one keyword.")
        return pd.DataFrame()

    results = pd.DataFrame()

    for query in queries:
        matched = df[df['Title'].str.lower().str.contains(query, na=False)].copy()
        matched.insert(0, "search_query", query)
        results = pd.concat([results, matched], ignore_index=True)

    return results

def main():
    file_path = input("📁 Enter path to 'selection_master.csv': ").strip()
    master_df = load_csv(file_path)

    if master_df.empty:
        return

    query_string = input("🔎 Enter search queries (comma-separated): ").strip()
    results = search_fsn(master_df, query_string)

    if results.empty:
        print("🔍 No matches found.")
    else:
        unique_results = results.drop_duplicates()
        print(f"✅ Found {len(results)} total matches, {len(unique_results)} unique matches.")
        print("📊 Sample Results:\n", unique_results[['search_query', 'Title', 'FSN', 'Brand']].head())

        results.to_csv("matched_fsn_results.csv", index=False)
        unique_results.to_csv("matched_unique_fsn_results.csv", index=False)
        print("⬇️ CSVs saved as 'matched_fsn_results.csv' and 'matched_unique_fsn_results.csv'.")

if __name__ == "__main__":
    main()
