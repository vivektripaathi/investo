import uuid
import pandas as pd
from pandas import DataFrame
from django.core.management.base import BaseCommand
from stock_data.domain_models import StockDataDomainModel
from stock_data.models import StockData
from django.conf import settings
from typing import List

class Command(BaseCommand):
    """Management Command to import stock data from Google Sheets"""
    help = 'Import stock data from Google Sheets'


    def create_stock_data_list(self, data: DataFrame) -> List[StockDataDomainModel]:
        """Create a list of StockDataDomainModel instances from a DataFrame."""
        return [ 
            StockDataDomainModel(
                id=uuid.uuid4(),
                **row.to_dict()
            )
            for _, row in data.iterrows()
        ]


    def create_bulk_stock_data_request(self, stock_data_list: List[StockDataDomainModel]) -> List[StockData]:
        """Create a list of StockData instances for bulk insertion into the database."""
        return [
            StockData(
                id=stock_data.id,
                datetime=stock_data.datetime,
                close=stock_data.close,
                high=stock_data.high,
                low=stock_data.low,
                open=stock_data.open,
                volume=stock_data.volume,
                instrument=stock_data.instrument,
            )
            for stock_data in stock_data_list
        ]


    def handle(self, *args, **kwargs):
        """Import stock data from Google Sheets to the database"""
        url: str = settings.GOOGLE_SHEET_URL
        stock_data_list: List[StockDataDomainModel] = self.create_stock_data_list(pd.read_csv(url))

        stock_data_bulk_request: List[StockData] = self.create_bulk_stock_data_request(stock_data_list)
        StockData.objects.bulk_create(stock_data_bulk_request)

        self.stdout.write(self.style.SUCCESS('Stock data imported successfully!'))
