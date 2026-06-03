# News Scraper API

## About

News Scraper API is a Python application that automates the collection of news articles from a website, stores the data in SQL Server, and exposes the information through a REST API built with Flask.

## Technologies

- Python
- Flask
- Selenium
- SQL Server
- PyODBC
- Python Dotenv

## Features

- Automated news collection
- Article detail extraction
- SQL Server integration
- REST API endpoints
- Execution logging

## Project Structure

```text
news-scraper-api/
│
├── app.py
├── database.py
├── browser.py
├── scraper_listing.py
├── scraper_details.py
├── logger_config.py
├── run_scrapers.py
├── requirements.txt
└── logs/
```

## Installation

```bash
git clone <repository-url>
cd news-scraper-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
URL=https://example.com

DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=localhost
DB_NAME=NoticiasDB
```

## Running

Run the complete scraping process:

```bash
python run_scrapers.py
```

Start the API:

```bash
python app.py
```


## Author

Donizetti Roberto