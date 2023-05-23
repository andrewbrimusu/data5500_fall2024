'''
This program queries coingecko for crypto currency coins prices in USD
It only runs for multiple coins
The urls require a specific date, and are generated using the datetime timedelta library, to handle things like leap year(s)
The data is written to a csv
'''


import requests
import json
import time
from datetime import datetime, timedelta


# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=31-05-2022&localization=false"


# url pieces, coin and date go in between  
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

# variables to pull coingecko data
key_md = 'market_data'
key_prc = 'current_price'
key_usd = 'usd'

# start date 2022-05-30   NOTE: integers do not start with 0 in Python like they often do in dates
dt = datetime(2022, 5, 30)

# example increasing the day by 1
dt += timedelta(days=1)
dt_s = dt.strftime("%d-%m-%Y") # string format required by coingecko

    
    
#####################################################################
# Running program for all coins
coins = [ "bitcoin", "ethereum", "ripple", "cardano", "bitcoin-cash", "eos", "litecoin"]

# iterate through coins, generate csv files, write prices
for coin in coins:
    # create csv for coin
    file = open(coin + ".csv", "w")
    file.write("Date," + coin + "\n")
    for i in range(364):
        # increment day using a timedelta object
        dt += timedelta(days=1)
        dt_s = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
        print("url: ", url)
        
        # get json from coingecko for coin and date
        req = requests.get(url)
        time.sleep(1) # sleep to avoid "too many requests" errors from coingecko
        d = json.loads(req.text)
        
        # write price to csv file
        print(dt_s, d[key_md][key_prc][key_usd])
        file.write(dt_s + "," + str(d[key_md][key_prc][key_usd]) + "\n")
        file.flush()
        
# close file
file.close()
