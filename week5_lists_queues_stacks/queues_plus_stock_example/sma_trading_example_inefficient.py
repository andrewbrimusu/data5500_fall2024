'''
This program executes a simple moving average trading strategy
but stores all the prices in memory as a list first
This program can be improved in memory efficiency by loading the prices
in one at a time, right when you need them, using a queue
'''

# load all the prices from the file, into a Python List
file_path = "/home/ubuntu/environment/data5500_code/week5_lists_queues_stacks/queues_plus_stock_example/AAPL.txt"
prices = [float(x) for x in open(file_path).readlines()]

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

input("pause")