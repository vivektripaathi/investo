# SMA Crossover Strategy

This Django project fetches stock data from a Google Sheet, validates it, and uses a Simple Moving Average (SMA) crossover strategy for buy/sell signals.

## Features

1. **Stock Data Import**: 
   - Imports stock data from Google Sheets and stores it in the database.
   - Validates the data to ensure correct types (decimals, integers, strings, datetime).

2. **SMA Crossover Strategy**:
   - Implements a strategy to identify buy/sell signals based on short and long SMA windows.

## Setup

### Prerequisites

- Python
- PostgreSQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/stock-data-sma.git
    cd stock-data-sma
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the `.env` file. A `.env.example` file is provided. Rename it to `.env`:

    ```bash
    cp .env.example .env
    ```

5. Edit the `.env` file and add your PostgreSQL database credentials and the URL for the Google Sheet you want to import. Here's the format:

    ```
    DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:PORT/DATABASE_NAME
    GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/__SPREADSHEET_KEY__/export?format=csv
    ```

    For example:

    ```
    DATABASE_URL=postgresql://postgres:password@localhost:5432/stock_db
    GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/1oCyKT2SFZlw3Ac3GXj0Y1IYcWG183IRgNCNytFojkWA/export?format=csv
    ```

6. Set up the Django application:

    ```bash
    python manage.py migrate
    ```

7. **Migrate Data from Google Sheets to Database**:

   After migrating the database schema, use the custom management command to fetch stock data from the Google Sheet and populate the database:

   ```bash
   python manage.py import_stock_data
   ```


### Running the Application

1. Start the Django server:

    ```bash
    python manage.py runserver
    ```

2. Visit the following URL to view the SMA crossover strategy:

    ```
    http://127.0.0.1:8000/stock/sma-crossover/?short_window=30&long_window=365
    ```

3. **SMA Crossover Strategy Screenshot**:

   Below is a screenshot showing the SMA crossover strategy output:

   ![SMA Crossover Strategy](assets/images/sma_crossover.png)


## Running Unit Tests

Unit tests are provided to validate stock data fetched from Google Sheets, ensuring that the data types are correct (decimals, integers, strings, and datetime).

### Running the Unit Tests

You can run the tests using the Django `test` command:

```bash
python manage.py test stock_data
```

   Below is a screenshot showing the SMA crossover strategy output:

   ![SMA Crossover Strategy](assets/images/unit_test.png)