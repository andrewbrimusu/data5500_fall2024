#### 
# Recursive Example 5
# Towers of Hanoi iteratively


ct = 0
def hanoi(n , source, destination, auxiliary):
    global ct
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        ct += 1    
        return
    hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    ct += 1
    hanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 2
hanoi(n,'A','C','B')
print("ct: ", ct)

input("press enter")
