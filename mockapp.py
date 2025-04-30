from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load a small demo CSV (in place of SQL)
try:
    df = pd.read_csv("sdn_list.csv")
except Exception:
    df = pd.DataFrame([{"error": "No data found"}])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sanctions')
def sanctions():
    return render_template('sanctions.html')

@app.route('/data')
def get_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
