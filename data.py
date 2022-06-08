
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Quantitative analysis of the market microstructure for a crypto-asset market                                                         -- #
# -- script: requirements.txt : text file with the required libraries for the project                    -- #
# -- author: MarcoSC08                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/MarcoSC08/myst-masc-lab1                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import json


f=open("orderbooks_05jul21.json")


orderbooks_data= json.load(f)
ob_data=orderbooks_data['bitfinex']

ob_data= {i_key: i_value for i_key, i_value in ob_data.items() if i_value is not None}

ob_data= {i_ob: pd.DataFrame(ob_data[i_ob])[['bid_size', 'bid', 'ask', 'ask_size']]
                if ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}



#publict = pd.read_csv('btcusdt_binance.csv')
#x= publict.head(5)
#print(x)

#p=("hola")
#print(p)
