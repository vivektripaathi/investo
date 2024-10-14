from datetime import datetime
from typing import NewType
from pydantic import UUID4, BaseModel

StockDataId = NewType("ShopCategoryId", UUID4)


class StockDataDomainModel(BaseModel):
    id: StockDataId
    datetime: datetime
    close: float
    high: float
    low: float
    open: float
    volume: int
    instrument: str
