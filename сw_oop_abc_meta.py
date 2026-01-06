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
