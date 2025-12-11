class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("some sound!")

    def get_info(self):
        return f"Name: {self.name}"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print("mau mau")

    def get_info(self):
        return super().get_info() + f"\nage: {self.age}"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print("gav gav")

    def guard_house(self):
        print(f"{self.name} start guard house!")


cat1 = Cat("murzik", 10)
cat1.speak()
print(cat1.get_info())

dog1 = Dog("sharik")
dog1.speak()
dog1.guard_house()

# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_info(self):
#         return f"Name: {self.__name}\nage: {self.__age}\ncolor: {self.__color}"
#
#
# class Dog:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_info(self):
#         return f"Name: {self.__name}\nage: {self.__age}\ncolor: {self.__color}"
#
#
# class Cow:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_info(self):
#         return f"Name: {self.__name}\nage: {self.__age}\ncolor: {self.__color}"
