#bubble sort
lst =[1,2,2,3,4,2,4,5,6,7,7,2]


new_lst = []

for i in range(len(lst)):
    j = i+1
    for j in range(len(lst)):
        if lst[i] == lst[j] & lst[i] not in new_lst:
            new_lst.append(lst[j])


print(new_lst)

