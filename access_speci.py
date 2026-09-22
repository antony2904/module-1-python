#class Detail ():

#    def __init__(self,name,age,password):
#        self.name = name
#        self._age = age
#        self.__password = password

#    def show_password(self):
#        return f'password : {self.__password}'

#obj = Detail('john',28,2468)

#print(obj.name)
#print(obj._age)
#print(obj.show_password())

#write a program to calculte the area and perimeter of a square ?


class Square ():

    def __init__(self,side):#
        self.side = side

    def area_of_square(self):
        return self.side *self.side

    def perimeter_of_square(self):
        return 4 * self.side

obj = Square(6)

print(obj.area_of_square())
print(obj.perimeter_of_square())