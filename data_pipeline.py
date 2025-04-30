import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load database credentials from .env
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

conn_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

# Example pipeline function
def process_and_load_csv(file_path, table_name):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} records from {file_path}")

        # Perform any data transformation here (placeholder)
        df_cleaned = df.dropna(how='all')  # basic cleaning example

        df_cleaned.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data loaded to table: {table_name}")

    except Exception as e:
        print(f"Failed to process file {file_path}: {e}")

# Example usage:
# process_and_load_csv("your_file.csv", "your_table_name")