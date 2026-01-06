from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @abstractmethod
    def golos(self):
        pass

    def getInfo(self):
        return f"Name: {self.name}, age: {self._age}"

    @classmethod
    def createAnimal(cls, name, year):
        return cls(name, 2026 - year)

    @staticmethod
    def walk():
        print("walking!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def golos(self):
        print("mau mau")


# animal = Animal("test", 20)
# animal.walk()


cat = Cat("Barsik", 3)
print(cat.getInfo())
cat.golos()


class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentSystem):

    def pay(self, amount):
        print(f"Pay with card {amount}")


class CashPayment(PaymentSystem):

    def pay(self, amount):
        print(f"Pay with cash {amount}")


class TestClass:
    pass


obj = TestClass()

print(type(type(obj)))


def method1(self):
    print("Hello")


NewClass = type('NewClass', (TestClass,), {'attrr1': 1, 'method1': method1})

obj1 = NewClass()
print(obj1)
print(type(obj1))
obj1.method1()


class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        print("Type class created - ", cls)
        print("name of class", name)
        print("bases list", bases)
        print("list attr", dict)
        return type.__new__(cls, name, bases, dict)


class MyClass1(metaclass=MyMetaClass):
    attr1 = 1


print(type(MyMetaClass))
print(type(MyClass1))


class TestAttrMeta(type):
    def __new__(cls, name, bases, dict):
        if 'id' not in dict.keys():
            print("No id attr in class ", name)
        else:
            methods = {key: value for key, value in dict.items() if callable(value)}
            if len(methods) > 2:
                print("More than 2 methods !!")
            else:
                print("Class is creating !", name)
                return type.__new__(cls, name, bases, dict)


class User(metaclass=TestAttrMeta):
    atrr = 3
    id = 1

    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass

user1 = User()
print(user1.id)
