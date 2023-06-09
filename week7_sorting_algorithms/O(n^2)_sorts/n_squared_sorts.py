#########################################
# bubble sort
# compare two adjacent items over and over

lst = [3, 1, 4, 1, 5, 9, 2, 6]

# n = number of items in the list i.e. 13

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        #compare two elements and swap if elemnt 1 is greater
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst) # each iteration
print("bubble sort: ", lst)


#########################################
# selection sort
# select the smallest in list, swap with current position

lst = [3, 1, 4, 1, 5, 9, 2, 6]

# Trlstverse through all array elements 
for i in range(len(lst)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(lst)): 
        if lst[min_idx] > lst[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    lst[i], lst[min_idx] = lst[min_idx], lst[i] 
    print(lst) # each iteration
    
print("selection sort: ", lst)


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
    print(lst) # each iteration
  
# Driver code to test above 
print("insertion sort:", lst)
