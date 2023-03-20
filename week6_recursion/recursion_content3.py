#### 
# Recursive Example 3
# Factorial iteratively

def factorial_numbers(n):
    total = 1
    for i in range(1,n+1):
        total *= i
        
    return total
    
print(factorial_numbers(5))


# Factorial recursively

def factorial_rec(n):
    if n == 1:
        return n
        
    return n * factorial_rec(n-1) # 5 * 4 * 3 * 2 * 1
    
    
print(factorial_rec(5))




# fibonacci

def fib(n):
    lst = [0,1]
    
    for i in range(2,102):
        lst.append(lst[i-2] + lst[i-1])
        
    return lst[n]
    
    
def fib_rec(n):
    if n < 2:
        return n
        
    return fib_rec(n-2) + fib_rec(n-1)
    
    
    
    
    
print(fib(0)) # print 0
print(fib(1)) # print 1
print(fib(20)) # print the correct answer



print(fib_rec(0)) # print 0
print(fib_rec(1)) # print 1
print(fib_rec(20)) # print the correct answer