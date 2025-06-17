# Load necessary packages
if (!require("readr")) install.packages("readr", dependencies=TRUE)
if (!require("dplyr")) install.packages("dplyr", dependencies=TRUE)
if (!require("stringr")) install.packages("stringr", dependencies=TRUE)

library(readr)
library(dplyr)
library(stringr)

# Function to load and validate the CSV
load_csv <- function(file_path) {
  tryCatch({
    df <- read_csv(file_path, show_col_types = FALSE)
    colnames(df) <- str_trim(colnames(df))  # Trim whitespace in column names
    
    required_cols <- c("FSN", "Title", "Brand")
    if (!all(required_cols %in% colnames(df))) {
      stop(paste("❌ CSV must contain columns:", paste(required_cols, collapse = ", ")))
    }
    
    return(df)
  }, error = function(e) {
    cat("❌ Error loading file:", e$message, "\n")
    return(data.frame())
  })
}

# Function to perform search
search_fsn <- function(df, query_string) {
  queries <- unlist(strsplit(query_string, ","))
  queries <- str_trim(queries)
  queries <- queries[queries != ""]  # Remove empty queries
  
  if (length(queries) == 0) {
    cat("⚠️ Please provide at least one keyword.\n")
    return(data.frame())
  }
  
  results <- data.frame()
  
  for (query in queries) {
    matched <- df %>%
      filter(str_detect(tolower(Title), tolower(query))) %>%
      mutate(search_query = query)
    
    results <- bind_rows(results, matched)
  }
  
  return(results)
}

# Main function
main <- function() {
  file_path <- readline(prompt = "📁 Enter path to 'selection_master.csv': ")
  master_df <- load_csv(file_path)
  
  if (nrow(master_df) == 0) return()
  
  query_string <- readline(prompt = "🔎 Enter search queries (comma-separated): ")
  results <- search_fsn(master_df, query_string)
  
  if (nrow(results) == 0) {
    cat("🔍 No matches found.\n")
  } else {
    unique_results <- distinct(results)
    cat("✅ Found", nrow(results), "total matches,", nrow(unique_results), "unique matches.\n")
    cat("📊 Sample Results:\n")
    print(head(unique_results %>% select(search_query, Title, FSN, Brand)))
    
    write_csv(results, "matched_fsn_results.csv")
    write_csv(unique_results, "matched_unique_fsn_results.csv")
    
    cat("⬇️ CSVs saved as 'matched_fsn_results.csv' and 'matched_unique_fsn_results.csv'.\n")
  }
}

# Run
main()
