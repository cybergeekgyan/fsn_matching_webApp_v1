# 🔍 FSN Finder - Keyword Matching WebApp

This WebApp allows users to **match product titles** against **search queries & keywords** using multiple strategies (Partial, Exact, Fuzzy Match), and returns the **matched FSNs** in a downloadable csv format.

---

## 🎯 Features :

  - ✅ Dropdown option to select search query for most searched keyword/query and a search bar to take user input as search query/keyword
  - ✅ appends and uploads search keyword list in the dropdown option
  - ✅ Radio buttons to select matching logic (partial, exact, fuzzy)
  - ✅ Slider to control fuzzy threshold
  - ✅ Live searchable, exportable FSN table
  - ✅ Download full search query results as a .csv file
  - ✅ Real time interactive UI with search, sort and filter

## 📝 Instructions for Use

- Upload selection_master.csv
- Must include: Product_Title, FSN, City, Buying
- Enter search_query to match
- Select matching type (Partial, Exact, Fuzzy, Synonym Expansion, TF-IDF + Cosine, BERT)
- Batch match across all search queries at once
- Click on view results in a searchable, sortable table
- View live results in table
- Click on download and Download matched FSNs as a CSV: `search_query` | `Product_Title` | `FSN` | 'City' | 'Buying' |

## 📁 Example File Formats:

- ✅ selection_master.csv

| Product_Title |	FSN | City | Buying |
| ---------| ------|-------| --------|
| Maggi 2-Minute Masala, Easy to Make Instant Noodles Vegetarian... |	NDLEUB3GENCEZNWA | Pune | Yes

- ✅ search_query

| search_query|
| -----|
| maggi |

## 🔄 Future Enhancements

- Upload CSV files dynamically via fileInput
- Add text input for custom queries
- Export results as CSV or Excel
- Add highlight to matched text
- add multiple search queries entries as an option seperated with commas

## ✅ Final App Features:

- Upload product dataset (selection_master) CSV
- Upload instock_new file in .csv format to calculate instock
- Upload ds_master.csv file to get live darkstores
- Enter search queries 
- Choose matching type: `Partial`, `Exact`, `Fuzzy`, 'TF-IDF + Cosine', 'BERT'
- Get search_query, FSN, City, Buying as a result
- Calculate Instock %, for each search_querXcity where that particular FSN is live 

## ▶️ Run the App

- Install pre-requisites:
  ```python
  pip install -r requirements.txt
  ```
- Clone the repository and run the app:

    ```python
    streamlit run app.py
    ```
## 📥 Output

We'll get a table with matched results like:

| search_query |	product_title |	FSN | City | Buying |
| ----------| ----------------| ---------| -----|-----|
| maggi	| maggi 2-minute masala noodles vegetarian 70 g	| NDLEUB3GFGYA5TJG | Pune | Yes
| maggi	| maggi chilly chow cup noodles vegetarian 70 g	| NDLEUB3GHSYTATZR | Mumbai | Yes

*You can download this table as a `.csv` using the **Download** Matched Results button.*

