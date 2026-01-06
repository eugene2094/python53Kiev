num1 = 1
num2 = 2

print(num1 + num2)

str1 = "1"
str2 = "2"

print(str1 + str2)

print(len("python"))
print(len([1, 2, 3]))


class Film:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def showInfo(self):
        print(f"Film title: {self.title}")
        print(f"Film director: {self.director}")


class Book:

    def __new__(cls, *args, **kwargs):
        print("I am __new__ magic method!")
        return super(Book, cls).__new__(cls)

    def __init__(self, title, auther, pages):
        print("I am __init__ method!")
        self.title = title
        self.auther = auther
        self.pages = pages

    def showInfo(self):
        print(f"Book title: {self.title}")
        print(f"Book auther: {self.auther}")

    def __str__(self):
        return f"Title: {self.title}, auther: {self.auther}"

    def __eq__(self, otherObj):
        return self.auther == otherObj.auther and self.title == otherObj.title

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages

    # film1 = Film('Avatar', 'Cameron')


# book1 = Book('Python', 'Gvido')
# book2 = Book('Harry Potter', 'Rouling', 300)
# book3 = Book('Harry Potter', 'Rouling', 300)
# # for item in (film1, book1):
# #     item.showInfo()
#
# # print(book1 + book2)
# book1 = Book('Python', 'Gvido', 34)
# print(book1)
#
# print(book3 == book2)


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} : {self.y}"

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Point):
            return Point(
                self.x * other.x,
                self.y * other.y
            )
        else:
            raise ValueError

    def __iadd__(self, other):
        if isinstance(other, int):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self

    def __float__(self):
        return Point(float(self.x), float(self.y))


# print(Point(2, 2) * 2.3)
print(Point(2, 2) * Point(3, 3))

num = 1
num += 1
p1 = Point(1, 1)
p1 += 2
print(p1)

print(p1.__float__())


# p1.z = 1
# print(p1.__dict__)


class Point3D(Point):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return super().__str__() + f" : {self.z}"


p3 = Point3D(1, 1, 1)
print(p3)
print(p3.__slots__)
# print(p3.__dict__)




