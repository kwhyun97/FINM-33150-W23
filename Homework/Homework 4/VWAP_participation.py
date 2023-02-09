# imports
import os
import pandas as pd
import numpy as np
import pickle
from enum import Enum
# constants
currency_crypto_cost = 50 * (10 ** (-4))
crypto_crypto_cost = 10 * (10 ** (-4))
p = 0.05
# Enum Class
class Order(Enum):
    Sell = -1
    Buy = 1
# trading algorithm
def VWAP_participation(df_cleaned, Q, p, start_time,
                       side, transaction_cost):
    df = df_cleaned.loc[start_time:].copy()

    if side == Order.Buy:
        f = False
    else:
        f = True

    accumulated = 0
    indexes = df[df['qualify']].index
    i = 0
    ret_df = {'datetime': [],
              'Nano seconds': [],
              'PriceMillionths': [],
              'SizeBillionths': []}

    while(accumulated < Q and i < len(indexes)):
        if i == 0:
            temp = df.loc[:indexes[i]].sort_values(by = ['PriceMillionths'], ascending = f).iloc[0]
        else:
            temp = df.loc[indexes[i-1]:indexes[i]].iloc[1:].sort_values(by = ['PriceMillionths'], ascending = f).iloc[0]

        ret_df['datetime'].append(temp.name[0])
        ret_df['Nano seconds'].append(temp.name[1])
        ret_df['PriceMillionths'].append(temp['PriceMillionths'])
        ret_df['SizeBillionths'].append(temp['SizeBillionths'] * p)

        accumulated += temp['SizeBillionths'] * p
        i += 1

    ret_df = pd.DataFrame(ret_df).set_index(['datetime', 'Nano seconds'])
    ret_df['NotionalMillionths'] = ret_df['PriceMillionths'] * ret_df['SizeBillionths'] / (10**9)
    ret_df['TradingCostsMillionths'] = ret_df['NotionalMillionths'] * transaction_cost
    ret_df['VWAPMillionths'] = (ret_df['NotionalMillionths'].cumsum() / ret_df['SizeBillionths'].cumsum() * (10**9))\
        .apply(int)

    return ret_df
# data handling
def total_participation_opportunities(full_dict, p):
    global currency_crypto_cost
    global crypto_crypto_cost

    for pair, year in full_dict.keys():
        if pair == 'ETH-BTC':
            transaction_cost = crypto_crypto_cost
        else:
            transaction_cost = currency_crypto_cost
        df_Buy = full_dict[(pair, year)][Order.Buy.value]
        dir = r'./data/' + pair + '_' + year + '_total_buy_opportunities.csv'
        VWAP_participation(df_Buy, np.infty, p, df_Buy.index[0][0], Order.Buy, transaction_cost).to_csv(dir)
        df_Sell = full_dict[(pair, year)][Order.Sell.value]
        dir = r'./data/' + pair + '_' + year + '_total_sell_opportunities.csv'
        VWAP_participation(df_Sell, np.infty, p, df_Sell.index[0][0], Order.Sell, transaction_cost).to_csv(dir)
# loading computed data
dir = r'./data/full_data.pkl'
with open(dir, 'rb') as f:
    data_dict = pickle.load(f)
# compile data
total_participation_opportunities(data_dict, p)