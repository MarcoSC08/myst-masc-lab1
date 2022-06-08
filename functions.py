
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Quantitative analysis of the market microstructure for a crypto-asset market                                                         -- #
# -- script: requirements.txt : text file with the required libraries for the project                    -- #
# -- author: MarcoSC08                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/MarcoSC08/myst-masc-lab1                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import numpy as np
import json
import data as dt


data_ob=dt.ob_data

def f_descriptive_ob(data_ob:dict)-> dict:
    
    #Median Time of Orderbook update
    ob_ts=list(data_ob.keys())
    l_ts= [pd.to_datetime(i_ts) for i_ts in ob_ts]
    ob_m1 = np.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds() * 1000

    #Spread, Midprice
    ob_m2= [data_ob[ob_ts[i]]['ask'][0]- data_ob[ob_ts[i]]['bid'][0] for i in range(0, len(ob_ts))]
    ob_m3= [(data_ob[ob_ts[i]]['ask'][0]+ data_ob[ob_ts[i]]['bid'][0])*0.5 for i in range(0,len(ob_ts))]

    #No.Price Levels
    ob_m4=[data_ob[i_ts].shape[0] for i_ts in ob_ts]

    #Bid Volume, Ask Volume, Total Volume
    ob_m5=[np.round(data_ob[i_ts]['bid_size'].sum(), 6) for i_ts in ob_ts]
    ob_m6=[np.round(data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]
    ob_m7=[np.round(data_ob[i_ts]['bid_size'].sum() + data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]
    
    r_data= {'median_ts_ob': ob_m1, 'spread': ob_m2, 'midprice': ob_m3}
    
    return r_data

#Median Time of Orderbook update
ob_ts=list(data_ob.keys())
l_ts= [pd.to_datetime(i_ts) for i_ts in ob_ts]
ob_m1 = np.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds() * 1000

#Spread, Midprice
ob_m2= [data_ob[ob_ts[i]]['ask'][0]- data_ob[ob_ts[i]]['bid'][0] for i in range(0, len(ob_ts))]
ob_m3= [(data_ob[ob_ts[i]]['ask'][0]+ data_ob[ob_ts[i]]['bid'][0])*0.5 for i in range(0,len(ob_ts))]

#No.Price Levels
ob_m4=[data_ob[i_ts].shape[0] for i_ts in ob_ts]

#Bid Volume, Ask Volume, Total Volume
ob_m5=[np.round(data_ob[i_ts]['bid_size'].sum(), 6) for i_ts in ob_ts]
ob_m6=[np.round(data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]
ob_m7=[np.round(data_ob[i_ts]['bid_size'].sum() + data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]

#Orderbook Imbalance (v: volume, d: depth)
obimb= lambda v,d : np.sum(v[0][:d]) / np.sum([v[0][:d]])