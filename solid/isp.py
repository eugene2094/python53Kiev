from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


# Ostriche is a type of Bird but cannot fly,
# so an exception is raised when fly method is called
class Ostriche(Walkable):
    def walk(self):
        print("Ostriche is walking")


# Eagle is a type of Bird that can both fly and walk
class Eagle(Walkable, Flyable):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")


# Create instances and call methods
try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostriche()
    obj2.walk()

except Exception as e:
    # Print the exception message
    print(e)
