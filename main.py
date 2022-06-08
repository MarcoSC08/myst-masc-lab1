
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Quantitative analysis of the market microstructure for a crypto-asset market                                                         -- #
# -- script: requirements.txt : text file with the required libraries for the project                    -- #
# -- author: MarcoSC08                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/MarcoSC08/myst-masc-lab1                                                                 -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data as dt
import functions as fn

data_ob=dt.ob_data

#Cantidad de libros de ordenes hay en total
n_libros= len(list(data_ob.keys()))
print(f"La cantidad total de libros de ordenes es: {n_libros}")
 
      
      
data_1=fn.f_descriptive_ob(data_ob=data_ob)

      
print(f"Mediana del tiempo esperado para un nuevo OrderBook:{data_1['median_ts_ob']}")


