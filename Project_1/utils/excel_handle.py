import os
import pandas as pd

def Excel_Customer_Command_Process( file_path: str):
    
    # Debug: Print the file path
    if not file_path:
        raise ValueError("FILE_PATH_MAIN is not set or is empty.")
    
    # Read the CSV file
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"No data in the file: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")
    
    # Specify the columns you want to extract
    columns_to_extract = ["Date", "Email", "Name", "Rating", "Comment", "Product_ID"]

    # Ensure the specified columns exist in the DataFrame
    missing_columns = [col for col in columns_to_extract if col not in df.columns]
    if missing_columns:
        raise KeyError(f"The following columns are missing from the CSV: {missing_columns}")

    # Extract the specified columns
    df = df[columns_to_extract]

    return df