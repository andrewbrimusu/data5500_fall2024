###########################################
# insertion sort
# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]

# Traverse through 1 to len(arr) 
for i in range(1, len(lst)): 

    key = lst[i] 

    # Move elements of lst[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >=0 and key < lst[j] : 
            lst[j+1] = lst[j] 
            j -= 1
    lst[j+1] = key 
    # print(lst) # each iteration
  
# Driver code to test above 
print("insertion sort:", lst)
