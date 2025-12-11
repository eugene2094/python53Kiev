import random


class Student:
    spec = "Computer science"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"name: {self.name},age: {self.age}"

    def showMsg(self, text):
        return f"Student {self.name} says {text}"


st1 = Student('bob', 55)

print(st1.show_info())

st2 = Student('nick', 33)
# st2.name = 'Bob'
print(st2.show_info())
print(st1.showMsg("tsts"))


class Car:
    def __init__(self):
        self.color = "red"

    def get_color(self):
        return self.color


car1 = Car()
car1.color = "black"
print(car1.get_color())


class Person:
    def __init__(self, name, age, salary):
        # public prop
        self.age = age
        self.salary = salary
        # private prop
        self.__name = name
        self.__personID = random.randint(1, 100)

    def __getId(self):
        return f"{self.__personID}"

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Value not str!")
        self.__name = value

    def getInfo(self):
        return f"Name: {self.name}, age: {self.age}, salary: {self.salary} , id: {self.__getId()}"

    @property
    def personID(self):
        return self.__personID

    @personID.setter
    def personID(self, value):
        if value > 0:
            self.__personID = value


person1 = Person('Kris', 30, 1000)
# print(person1.name)


print(person1.personID)
person1.personID = 10

person1.name = "test new name"
print(person1.getInfo())
