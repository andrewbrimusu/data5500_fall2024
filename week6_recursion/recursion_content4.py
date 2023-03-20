#### 
# Recursive Example 4
# Fibonacci recursive example - much easier than iterative solution

def fibiter(n):
    f1=1
    f2=1
    tmp=1
    for i in range(1,int(n)-1):
        tmp = f1+f2
        f1=f2
        f2=tmp
    return f2
    
print(fibiter(20))


def fib(n):
    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)
    
print(fib(200))


