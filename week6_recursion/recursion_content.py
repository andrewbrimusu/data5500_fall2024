################### 
# Recursion example - print numbers 1 to 1000

pi = [3,1,4,1,5,9,2,6,5]

def print_lst(lst):
    for i in range(len(lst)):
        print(lst[i])
        
    return

print_lst(pi)

print("------")

def print_rec(lst, start):
    if start == len(lst):
        return
    
    print(lst[start])
    print_rec(lst, start+1)
    

print_rec(pi, 0)