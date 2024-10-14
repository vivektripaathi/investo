import unittest
import pandas as pd
from decimal import Decimal
from datetime import datetime
from django.conf import settings

# Create your tests here.


# Helper functions to classify data types
def is_decimal(s):
    """Check if the input can be converted to a decimal."""
    try:
        float(s)
        return '.' in s
    except ValueError:
        return False

def is_integer(s):
    """Check if the input can be converted to an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_strict_string(s):
    """Check if the input is strictly a string that is not a number."""
    return not is_integer(s) and not is_decimal(s)

def is_datetime(s, date_format='%Y-%m-%d %H:%M:%S'):
    """Check if the input can be parsed into a datetime."""
    try:
        datetime.strptime(s, date_format)
        return True
    except ValueError:
        return False


class TestStockDataValidation(unittest.TestCase):
    def setUp(self):
        # Fetch data from Google Sheets but force pandas to read everything as strings
        url = settings.GOOGLE_SHEET_URL
        self.data = pd.read_csv(url, dtype=str)  # Force all columns to be read as strings

    def validate_columns(self, record, validations, index):
        """Helper method to validate multiple columns at once."""
        for column, validator in validations.items():
            value = record[column]
            self.assertTrue(
                validator(value),
                f"Column '{column}' with value '{value}' in row {index} failed validation."
            )

    def test_data_validation(self):
        """Test data validation for all fields."""
        # Define expected validators for each column
        validations = {
            'open': is_decimal,
            'high': is_decimal,
            'low': is_decimal,
            'close': is_decimal,
            'volume': is_integer,
            'instrument': is_strict_string,
            'datetime': is_datetime
        }

        for index, record in self.data.iterrows():
            self.validate_columns(record, validations, index)


if __name__ == '__main__':
    unittest.main()
