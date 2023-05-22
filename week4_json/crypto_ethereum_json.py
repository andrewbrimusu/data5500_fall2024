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

coin = "ethereum"

# create csv for coin
file = open(coin + ".csv", "w")
file.write("Date," + coin + "\n")

# iterate through days, request data, write price to csv
for i in range(364):
    # increment day using a timedelta object
    dt += timedelta(days=1)
    dts = dt.strftime("%d-%m-%Y")
    
    # generate url for each day
    url = url1 + coin + url2 + dts + url3
    print("url: ", url)
    
    #request data from coingecko
    req = requests.get(url)
    time.sleep(1)
    d = json.loads(req.text)
    
    # write price to csv file, flush allows writing each time
    print(dts, d[key1][key2][key3])
    file.write(dts + "," + str(d[key1][key2][key3]) + "\n")
    file.flush()

# close file when done
file.close()