def my_function(x):
    #1 base case.  Stops recursion
    if x == 100:
        #4 return stmt
        return
    #2 logic
    x += 1
    print(x)
    
    #3 recursive call
    my_function(x)
    
    return None
    
    
    
my_function(0)


