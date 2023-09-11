'''
This program queries alphavantage for AAPL stock prices
It only runs for one stock, AAPL
The prices are saved to a csv file with the latest prices first, newest at the bottom
If your csv needs to append newest prices at the end of the csv file, a simple way to do this is append the prices to a list, reverse it, then write to a file
    
'''


import requests
import json


# example url to pull alphavantage data
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8'


# variables to query alphavantage
ticker = 'AAPL'
key_timeseries = "Time Series (Daily)"
key_close = "5. adjusted close"
first_date = "2022-05-30"

#generate url
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)

# requests stock data from alphavarange web json api
request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
dct1 = json.loads(request.text)


# create csv file to store stock data
curr_dir = os.path.dirname(__file__) # get the current directory of this file

file = open(curr_dir + "/" + ticker + ".csv", "w")
file.write("Date," + ticker + "\n")




#####################################################################
# iterate through prices and store them in csv
for date in dct1[key_timeseries]:
    ### ALERT ####
    # this will write the prices with latest first.  
    
    # writing prices to csv file
    if date > first_date:
        print(dct1[key_timeseries][date][key_close])
        file.write(date + "," + dct1[key_timeseries][date][key_close] + "\n")
        file.flush()
    
file.close()
