import requests
import json

# example url to pull alphavantage data
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8'


# variables to query alphavantage
ticker = 'AAPL'
key1 = "Time Series (Daily)"
key3 = "4. close"
first_date = "2022-05-30"

#generate url
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)

# requests stock data from alphavarange web json api
request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
dct1 = json.loads(request.text)

# create csv file to store stock data
file = open(ticker + ".csv", "w")
file.write("Date," + ticker + "\n")

# iterate through prices and store them in csv
for date in dct1[key1]:
    ### ALERT ####
    # this will write the prices with latest first.  If your csv needs to append newest prices at the end
    # these prices will need to write latest last.  A simple way to do this is append the prices to a list, reverse, then write to a file
    
    # writing prices to csv file
    if date > first_date:
        print(dct1[key1][date][key3])
        file.write(date + "," + dct1[key1][date][key3] + "\n")
        file.flush()
    
file.close()
