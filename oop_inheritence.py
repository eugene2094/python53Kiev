class Animal:
    def __init__(self, name):
        self.name = name
        self.__id = 0
        self._protected_prop = 1

    def speak(self):
        print("some sound!")

    def get_info(self):
        return f"Name: {self.name}"

    @property
    def protected_prop(self):
        return self._protected_prop


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
print(cat1.name)
# cat1.protected_prop = 2
print(cat1.protected_prop)
print(cat1.get_info())

dog1 = Dog("sharik", 2)
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


class MathTools:

    @staticmethod
    def add(a, b):
        return a + b


print(MathTools.add(4, 5))


class User:
    def __init__(self, name, age):
        self.name = name
        if not User.is_valid_age(age):
            raise ValueError("Age must be positive !")
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return age > 0


user1 = User('Mask', 23)
print(User.is_valid_age(-10))


