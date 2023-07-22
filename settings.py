import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
import os
import sys

dir_path = './data/spot/monthly/klines/'
header = ['OpenTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QuoteAssetVolume', 'NbrTrades', 'TbuyBaseVolume', 'TbuyQuoteVolume', 'Ignore']
last_date = date(2023, 6, 29)
split_date = pd.to_datetime(date(2023, 1, 1))