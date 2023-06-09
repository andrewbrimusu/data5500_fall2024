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
    # print(lst) # each iteration
    
print("selection sort: ", lst)