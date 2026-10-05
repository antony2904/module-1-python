def detail(name,age,):

    print(f'My name is {name},i am {age} year old')


detail('anjo',23)




def detail(name,age,place):

        return f'I am {name},coming from {place} and i am {age} year old'

print(detail('anjo',23,'Thrissur'))


#arguments


def addition(x,y):
      result = sum ([x,y])
      print(result)

addition(2,5)


def addition(*args):
      result = sum(args)
      print(result)

addition(2,5,7,9,2,4,5,2)


#looping statement

lst = [25,24,85,45,75]
new_lst=[]

for i in lst:
    result = i * 2
    new_lst.append(result)

print(new_lst)


lst = [2,58,57,8]
new_lst = []

def addition():
      for i in lst:
        result = i*2
        new_lst.append(result)

addition()
print(new_lst)

x=34

def addition():
      y=54
      print(x+y)
    
addition()

#range

for i in range(20):
     print(i)

for i in range(1,50,5): #start/stop/size
     print(i)

#list comprenhenssion

print([i*5 for i in range(40)])

print([i for i in range (1,41) if i%5 == 0])













