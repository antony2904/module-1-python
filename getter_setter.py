class Person():

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print(self.__name)

    def get_age(self):
        print(self.__age)

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

obj = Person('john',34)
obj.get_name()
obj.get_age()

obj.set_name('johny')
obj.get_name()

obj.set_age(45)
obj.get_age()




