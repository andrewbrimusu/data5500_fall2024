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
    # print(lst) # each iteration
print("bubble sort: ", lst)
