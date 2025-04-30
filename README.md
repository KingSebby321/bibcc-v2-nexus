
# BIBCC V2 Nexus

**BIBCC (Boston InterBank Communications Channel) V2 Nexus** is a Flask-based web platform designed for anti-fraud and compliance research. This project provides a lightweight dashboard for visualizing and interacting with structured regulatory and fraud-related data, such as sanctions lists and scraped financial event data.

## 🚀 Features

- Flask web server with dynamic HTML rendering
- PostgreSQL database integration
- Endpoint for sanctions data (e.g., OFAC SDN List)
- Clean, modular Python scripts for:
  - Data scraping
  - Data cleaning
  - ETL pipelines

## 🔐 Security

Sensitive credentials like database passwords are stored in a `.env` file and **not hardcoded**. Make sure to create your own `.env` file with:

```env
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 📁 Structure

```
├── app.py                  # Flask app with routes
├── data_cleaning.py        # Cleans imported data
├── data_pipeline.py        # ETL pipeline scripts
├── scrape_events.py        # Event scraper
├── templates/              # HTML templates
├── sdn_list.csv            # Example data file
├── requirements.txt        # Python dependencies
```

## ✅ How to Run

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Add a `.env` file in the root directory.

3. Start the Flask server:
```bash
python app.py
```

## 📜 License

This is an open-source project provided for educational and developmental use. Contributions welcome.
