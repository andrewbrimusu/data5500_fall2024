'''
This program queries coingecko for ethereum prices in USD
It only runs for one coin, ethereum
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

# start date 2022-05-30  NOTE: integers do not start with 0 in Python like they often do in dates
dt = datetime(2022, 5, 30)

# example increasing the day by 1
dt += timedelta(days=1)
dt_s = dt.strftime("%d-%m-%Y") # string format required by coingecko
    
coin = "ethereum"


# example generating a url for a specific coin and date
url = url1 + coin + url2 + dt_s + url3
    
#example requesting  data from coingecko
req = requests.get(url)
time.sleep(1) # sleep to avoid "too many requests" errors from coingecko
d = json.loads(req.text)

# printing the price
print(dt_s, d[key_md][key_prc][key_usd])




#####################################################################
# Running the program, for 365 days and saving to a csv file


# create csv file for coin
curr_dir = os.path.dirname(__file__) # get the current directory of this file

file = open(curr_dir + "/" + coin + ".csv", "w")
file.write("Date," + coin + "\n")

# iterate through 365 days, request data, write prices to csv
for i in range(365):
    # increment day using a timedelta object
    dt += timedelta(days=1)
    dt_s = dt.strftime("%d-%m-%Y")
    
    # generate url for each day
    url = url1 + coin + url2 + dt_s + url3
    print("url: ", url)
    
    #request data from coingecko
    req = requests.get(url)
    time.sleep(1) # sleep to avoid "too many requests" errors from coingecko
    d = json.loads(req.text)
    
    # write price to csv file, flush allows writing each time
    print(dt_s, d[key_md][key_prc][key_usd])
    file.write(dt_s + "," + str(d[key_md][key_prc][key_usd]) + "\n")
    file.flush()

# close file when done
file.close()