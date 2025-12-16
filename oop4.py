import random
from datetime import date


class Person:
    hobby = 'cooking'

    def __init__(self, name, age):
        # public
        self.name = name
        # protected
        self._age = age
        # private
        self.__personId = random.randint(1, 1000)

    def __showID(self):
        return self.__personId

    def getInfo(self):
        return f"Person name: {self.name}, age: {self._age}, id: {self.__showID()}"

    @classmethod
    def setDefaultHobby(cls, newhobby):
        cls.hobby = newhobby

    @classmethod
    def basedOnBYear(cls, name, byear):
        personAge = date.today().year - byear
        return cls(name, personAge)

    @classmethod
    def basedOnStr(cls, strInf):
        name, age = strInf.split(" ")
        return cls(name, age)


pr1 = Person("Bob", 30)
print(pr1.getInfo())

Person.setDefaultHobby('driving')

pr2 = Person("Djon", 30)
print(pr2.getInfo())
print(pr2.hobby)
print(pr1.hobby)

pr3 = Person.basedOnBYear("Lola", 2000)
print(pr3.getInfo())

pr4 = Person.basedOnStr("Max 45")
print(pr4.getInfo())


class Developer(Person):
    def __init__(self, name, age, jobTitle):
        super().__init__(name, age)
        self.jobTitle = jobTitle
        self.__salary = 0

    def setBasicSalary(self):
        if self.__rung == 'junior':
            self.__salary = 1000
        elif self.__rung == 'middle':
            self.__salary = 2000
        elif self.__rung == 'senior':
            self.__salary = 5000

    @classmethod
    def setRung(cls, rung):
        cls.__rung = rung

    def getInfo(self):
        return super().getInfo() + f"\njob title: {self.jobTitle},\nrung: {self.__rung},\nsalary: {self.__salary}"

    def calcSalary(self, perc):
        return self.__salary + self.__salary * perc


jun1 = Developer('Bill', 23, 'frontend')
Developer.setRung('middle')
# jun1.setBasicSalary()
jun2 = Developer('Joe', 33, 'backend')

# print(jun1.__dict__)

for jun in zip((jun1, jun2), (0.1, 0.3)):
    jun[0].setBasicSalary()
    print(jun[0].getInfo())
    print(f"Expected salary: {jun[0].calcSalary(jun[1])}")


class Book:
    def __init__(self, title, auther, pages):
        self.title = title
        self.auther = auther
        self.pages = pages

    def showInfo(self):
        print("Title: ", self.title)
        print("Auther: ", self.auther)
        print("Pages: ", self.pages)


class File:
    def __init__(self, fileSize, src):
        self.fileSize = fileSize
        self.src = src

    def showInfo(self):
        print("File size: ", self.fileSize)
        print("File src: ", self.src)


class Ebook(Book, File):
    def __init__(self, title, auther, pages, fileSize, src):
        Book.__init__(self, title, auther, pages)
        File.__init__(self, fileSize, src)


ebook1 = Ebook("python", 'gvido', 400, 123, "C://book.txt")
ebook1.showInfo()
print(Ebook.mro())
