from typing import List
from django.shortcuts import render
from stock_data.models import StockData
import numpy as np
import pandas as pd

# Create your views here.

def get_stock_data() -> List[StockData]:
    stock_data_db_entry = StockData.objects.all().order_by('datetime')
    return list(stock_data_db_entry)

def sma_crossover_strategy(request):
    stock_data = get_stock_data()

    close_prices = [data.close for data in stock_data]
    dates = [data.datetime for data in stock_data]

    short_window = int(request.GET.get('short_window', 30))
    long_window = int(request.GET.get('long_window', 365))
    
    df = pd.DataFrame({
        'datetime': dates,
        'close': close_prices
    })

    df['SMA_Short'] = df['close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['close'].rolling(window=long_window).mean()

    df['Signal'] = 0
    df['Signal'][short_window:] = np.where(df['SMA_Short'][short_window:] > df['SMA_Long'][short_window:], 1, 0)

    df['Position'] = df['Signal'].diff()

    buy_signals = df[df['Position'] == 1][['datetime', 'close', 'SMA_Short', 'SMA_Long']]
    sell_signals = df[df['Position'] == -1][['datetime', 'close', 'SMA_Short', 'SMA_Long']]
    
    context = {
        'buy_signals': buy_signals.to_dict(orient='records'),
        'sell_signals': sell_signals.to_dict(orient='records'),
        'stock_data': stock_data,
    }

    return render(request, 'sma_crossover.html', context)
