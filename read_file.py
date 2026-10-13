##Read_file##

file = open("#job roles.txt","r")
#lamdaaa.py
content = file.read()                                        #"r" = read
print(content)                                              #"w" = write                          
                                                            #"a" = append
file.close()


##write a file by using python##

with open("hello.txt","w") as file:
    file.write("hello,python ")

with open("hello.txt","a") as file:
    file.write("\n Welcome to python world")

with open("hello.txt","r") as file:
    content = file.read()
    print(content)

          
           