import uuid
from django.db import models

# Create your models here.

class StockData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True, primary_key=True)
    datetime = models.DateTimeField()
    close = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    instrument = models.CharField(max_length=100)

    class Meta:
        db_table = 'stock_data'
