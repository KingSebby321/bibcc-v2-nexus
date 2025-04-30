import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create PostgreSQL engine from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
conn_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

# OFAC CSV file URL
csv_url = "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV"

try:
    df = pd.read_csv(csv_url, delimiter=',', header=None, encoding='ISO-8859-1')
    print("CSV file successfully read.")

    expected_columns = 12
    if df.shape[1] != expected_columns:
        raise ValueError(f"Expected {expected_columns} columns, but found {df.shape[1]}.")

    # Assign column names
    df.columns = [
        'ID', 'Name', 'Type', 'Country', 'Location', 'Business Type',
        'Stolen Amount', 'Affiliated Regime', 'Region', 'Notes',
        'Additional Info', 'Miscellaneous'
    ]

    print(df.head())  # Preview data
    df.to_sql('ofac_sdn_list_cleaned', engine, if_exists='replace', index=False)
    print("Data cleaning and insertion completed.")

except pd.errors.EmptyDataError:
    print("CSV is empty or unreadable.")
except ValueError as ve:
    print(f"Validation error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")