def sum_numbers(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
    
print(sum_numbers(13))

def sum_numbers_rec(n):
    # base case 1
    if n == 1:
        return n
    return n * sum_numbers_rec(n-1)
    # (100 + (99 + (98 + (97 + (96 + (95 + ... + 1))))))
    
    
    
print(sum_numbers_rec(13)) # 5050