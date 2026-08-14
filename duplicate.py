lst=[1,2,3,4,5,6,7,7,8,2,1]

new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print( new_lst)