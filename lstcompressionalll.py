
print([0 if i %2 == 0 else i  for i in range(1,10)])

lst=[]
for i in range(1,50):
    if i %5 == 0:
        lst.append(5)
    else:
         lst.append(i)

print(lst)


print([5 if i % 5 == 0 else i  for i in range(1,50)])