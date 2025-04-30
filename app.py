from flask import Flask, jsonify, render_template, request
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection string from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

conn_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

# Connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sanctions')
def sanctions():
    return render_template('sanctions.html')

@app.route('/data')
def get_data():
    try:
        query = "SELECT * FROM ofac_sdn_list_cleaned LIMIT 100"
        df = pd.read_sql(query, engine)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500