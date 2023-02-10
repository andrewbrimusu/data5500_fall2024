#### 
# Recursive Example 1
# Printing numbers iterative
nums = [3, 1, 4, 1, 5, 9, 2, 6]

for i in range(len(nums)):
    print(nums[i])
    
# Printing numbers recursively
def print_nums(nums, i):
    if i >= len(nums):
        return
    
    print(nums[i])
    print_nums(nums, i+1)
    
print_nums(nums, 0)



#### 
# Recursive Example 2
# Sum numbers iteratively
def sum_numbers(n):
    # add up all the numbers 1 to n, and return the result
    val = 0
    for i in range(1,n+1):
        val += i
    return val

print(sum_numbers(5)) # 15

# Sum numbers recursively
def sum_number_rec(n):
    if n == 1:
        return 1
    return n + sum_number_rec(n-1) # 5 + 4 + 3 + 2 + 1
    
print(sum_number_rec(5))



#### 
# Recursive Example 3
# Factorial iteratively
def factorial(n):
    tot = 1
    for i in range(1,n+1):
        tot *= i
    return tot
    
print(factorial(5)) #120

# Factorial recursively
def factorial_rec(n):
    #base case
    if n == 1:
        return n
    #recursive all
    return n * factorial_rec(n-1)
    
print(factorial_rec(5)) #120



#### 
# Recursive Example 4
# Fibonacci recursive example - much easier than iterative solution
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    # recursive call
    return fib(n-1) + fib(n-2)
    
print(fib(41))