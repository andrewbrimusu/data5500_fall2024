'''
This program executes a simple moving average trading strategy
The prices are loaded in one by one, in a queue as needed.
This approach using a queue in more memory efficient because it only loads the prices into
memory that are required to calculate the moving average, as needed.
'''

import os


# stock prices file
curr_dir = os.path.dirname(__file__) # get the current directory of this file

tkr = "AAPL"
stock_fil = curr_dir + "/" + tkr + ".txt" # dirname and __file__ (this file) returns the current folder

file = open(stock_fil, "r")

# prices are read in using readline(), not readlines(), one at a time
# prices is a queue implemented as a Python List
prices = []
line = file.readline()
print("line: ", line)
first_price = float(line)

# iterate through prices, and run strategy
buy = 0
tot_profit = 0
while line:
    prices.append(float(line)) # add one price to the queue

    if len(prices) == 6: # 5 day moving average + 1 current day price
        current_price = prices[5]
        avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
        # print("avg: ", avg)
        if current_price > avg and buy == 0:
            print("buying at: ", current_price)
            buy = current_price
        elif current_price < avg and buy != 0:
            print("selling at: ", current_price)
            
            tot_profit += current_price - buy
            print("trade profit: ", current_price - buy)
            buy = 0
        else:
            pass #do nothing
        
        prices.pop(0) # oldes prices no longer needed, removed from queue with pop(0)
    
    line = file.readline()
    
    
print("tot_profit: ", tot_profit)
print("percenage return%: ", 100 * tot_profit/first_price)

input("press enter")