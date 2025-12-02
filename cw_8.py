# lambda - анонімні функції
# lambda аргумент1, аргумент2 : вираз

def add10(x):
    return x + 10


nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(add10(num))

for num in nums:
    print((lambda x: x + 10)(num))

students = [['Bob', 70],
            ['Jane', 80],
            ['Piter', 60]]

print(students)
sortedSts = sorted(students, key=lambda x: x[1])
print(sortedSts)

grnToDollar = 42
discount = 0.15
priceDol = lambda x: x / grnToDollar * (1 - discount)

price = 4200
print(f"Price: {priceDol(price)} $")
print(f"Price: {priceDol(3500)} $")

userName = lambda firstName, lastName: f"Full name: {firstName.title()} {lastName.title()}"

print(userName("djon", 'gibson'))

studBirthYear = [2000, 1997, 2002, 1999]
print(studBirthYear)
studAges = list(map(lambda x: 2025 - x, studBirthYear))

# for year in studBirthYear:
#     studAges.append(2025 - year)

print(studAges)

number = int(input("enter num - "))
print(abs(number))


def makeLog(userName, maker):
    return maker(userName)


def nameUpper(name):
    return 'user' + name.upper()


def nameLower(name):
    return 'user' + name.lower()


print(makeLog("admin", nameUpper))

# map()  filter()  zip()

userLogs = ['admin', 'STUDENT', 'QWERty', 'User']
print(userLogs)

userLogsLow = list(map(str.lower, userLogs))
print(userLogsLow)

values = ['2.3', '12', '45.34', '3']
print(values)

numbers = list(map(float, values))
print(numbers)

digits = list(map(lambda num: int(num[0]), values))
print(digits)

nums1 = [10, 20, 30]
nums2 = [1, 2, 3, 4]
result = list(map(lambda a, b: a ** b, nums1, nums2))
print(result)

prices = [100, 33, 67, 99, 45]
expensive = list(filter(lambda x: x > 50, prices))
print(prices)
print(expensive)

userPass = ['1111', 'qwer', '3232']

for log, passw in zip(userLogs, userPass):
    print(f"login: {log}, password: {passw}")

print(list(zip(userLogs, userPass)))


