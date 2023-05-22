# the logic to save multiple coins to multiple csv files
import requests
import json
import time
from datetime import datetime, timedelta

# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=31-05-2022&localization=false"


# url pieces
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

# variables to pull coingecko data
key1 = 'market_data'
key2 = 'current_price'
key3 = 'usd'

# start date
dt = datetime(2022, 5, 30)

coins = [ "bitcoin", "ethereum", "ripple", "cardano", "bitcoin-cash", "eos", "litecoin"]

# iterate through coins, generate csv files, write prices
for coin in coins:
    # create csv for coin
    file = open(coin + ".csv", "w")
    file.write("Date," + coin + "\n")
    for i in range(364):
        # increment day using a timedelta object
        dt += timedelta(days=1)
        dts = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
        print("url: ", url)
        
        # get json from coingecko for coin and date
        req = requests.get(url)
        time.sleep(1)
        d = json.loads(req.text)
        
        # write price to csv file
        print(dts, d[key1][key2][key3])
        file.write(dts + "," + str(d[key1][key2][key3]) + "\n")
        file.flush()
        
# close file
file.close()
