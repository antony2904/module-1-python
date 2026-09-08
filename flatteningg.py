lst = [[2,5,8,7,6]]

new_lst =[]

for i in lst:
    for j in i:
        new_lst.append(j)

print(new_lst)

print([j for i in lst for j in i])

print([j*2 for i in lst for j in i])

