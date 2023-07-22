import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
import os
import sys

from settings import *

def load_train_dataset(eth_p=True):
    symbols = os.listdir(dir_path)
    print("Symbols : ", symbols)
    eth_symbols = [sym for sym in symbols if 'ETH' in sym]
    btc_symbols = [sym for sym in symbols if 'BTC' in sym]
    eth_symbols.sort()
    btc_symbols.sort()
    
    if(eth_p):
        symbols = eth_symbols
    
    dict_symbols = {}

    for symbol in symbols :
        print(symbol, end = ' -- ')
        symbol_freq = symbol+"/1h/"

        dir_sym = dir_path + symbol_freq

        try : 
            months = os.listdir(dir_sym)
            months.sort()

            df_temp = None 
            for m in months : 
                temp = pd.read_csv(dir_sym+m, names=header)
                temp['OpenTime'] = pd.to_datetime(temp['OpenTime']*10**6)
                temp.set_index('OpenTime', inplace=True)
                df_temp = pd.concat([df_temp, temp])
        except : 
            print("\n", dir_sym)


        dict_symbols[symbol] = df_temp
        
    keys = list(dict_symbols.keys())
    eth_keep = []
    intersection = None
    for k in keys: 
        last_date_symbol = dict_symbols[k].index[-1]
        if(last_date_symbol > last_date): 
            eth_keep.append(k)
            if(intersection is None):
                intersection = dict_symbols[k].index
            else : 
                intersection = list(set(intersection) & set(dict_symbols[k].index))
        
            print(k, last_date_symbol, dict_symbols[k].index[0], len(dict_symbols[k].index))
    
    
    last_df = {}
    open_df = {}

    for k in eth_keep: 
        print(k, end =' -- ')
        symbol = (dict_symbols[k])
        selection = symbol.index.isin(intersection)
        last_df[k] = symbol[selection]
        open_df[k] = last_df[k].Open

    df = pd.DataFrame(open_df)
    df_train = df[df.index < split_date]
    df_test = df[df.index >= split_date]
    
    return dict_symbols, df, df_train, df_test
            
  
            
    