# src/simple_etl.py

import pandas as pd
from datetime import datetime

def extract_data(file_path):
    """
    Extract data from CSV file
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Extracted {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def transform_data(df):
    """
    Clean and transform the data
    """
    if df is None:
        return None
    
    # Make a copy to avoid modifying original data
    df_transformed = df.copy()
    
    # Basic transformations
    df_transformed['age'] = df_transformed['age'].fillna(df_transformed['age'].mean())
    df_transformed['salary'] = df_transformed['salary'].fillna(0)
    
    # Create new feature
    df_transformed['salary_category'] = df_transformed['salary'].apply(
        lambda x: 'high' if x > 75000 else ('medium' if x > 50000 else 'low')
    )
    
    print("Transformation completed")
    return df_transformed

def load_data(df, output_file):
    """
    Load transformed data to CSV
    """
    if df is None:
        return False
    
    try:
        df.to_csv(output_file, index=False)
        print(f"Data loaded to {output_file}")
        return True
    except Exception as e:
        print(f"Error loading data: {e}")
        return False

def run_etl():
    """
    Execute the ETL pipeline
    """
    print(f"Starting ETL job at {datetime.now()}")
    
    # Define input and output paths
    input_file = "data/raw_employees.csv"
    output_file = "data/transformed_employees.csv"
    
    # Execute ETL steps
    df = extract_data(input_file)
    df_transformed = transform_data(df)
    success = load_data(df_transformed, output_file)
    
    print(f"ETL job finished at {datetime.now()}")
    return success

if __name__ == "__main__":
    run_etl()