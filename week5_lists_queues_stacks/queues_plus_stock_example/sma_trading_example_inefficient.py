'''
This program executes a simple moving average trading strategy
but stores all the prices in memory as a list first
This program can be improved in memory efficiency by loading the prices
in one at a time, right when you need them, using a queue
'''
import os


# load all the prices from the file, into a Python List
# stock prices file
curr_dir = os.path.dirname(__file__) # get the current directory of this file

tkr = "AAPL"
stock_fil = curr_dir + "/" + tkr + ".txt" # dirname and __file__ (this file) returns the current folder

file = open(stock_fil, "r")

prices = [float(x) for x in file.readlines()]

# iterate through prices in list and run strategy
days= 5
buy = 0
profit = 0.0
for i in range(len(prices)):
    if i >= days:
        p = prices[i]
        avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
        
        if p > avg and buy == 0: #buy
            print("buying at: ", p)
            buy = p
        elif p < avg and buy != 0: #sell
            print("selling at: ", p)
            profit += p - buy
            
            print("trade profit: ", p - buy)
            buy = 0
        else:
            pass # do nothing today, except hopefully my position is becoming more profitable
        
        
print("profit: ", profit)
print("percentage returns%: ", 100 * (profit/prices[0]))

input("press enter")