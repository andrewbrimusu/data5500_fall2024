#### 
# Recursive Example 2
# Sum numbers iteratively

def sum_numbers(n):
    total = 0
    for i in range(1,n+1):
        total += i
        
    return total
    
print(sum_numbers(5))


def sum_numbers_rec(n):
    if n == 1:
        return n
        
    return n + sum_numbers_rec(n-1) # 5 + 4 + 3 + 2 + 1
    
    
print(sum_numbers_rec(5))

