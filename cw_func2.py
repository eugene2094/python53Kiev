def sayHello():
    name = "qwerty"
    print(f"Hello, {name}")


print(type(sayHello))

greeting = sayHello
greeting()

customers = ['AdminJane', 'adminBob', 'STUDENTNick', 'studentALICE', 'kate']


def sayHelloForClient(customer):
    if customer.find('admin') != -1:
        print(f"Hello admin - {customer}")
    elif customer.find('student') != -1:
        print(f"Hello student - {customer}")
    else:
        print(f"Hello  - {customer}")


def greeting(customerList, greetFunc):
    if isinstance(customerList, list):
        for c in customerList:
            greetFunc(c.lower())


greeting(customers, sayHelloForClient)


def calculateSum(a, b):
    return a + b


def calculateMinus(a, b):
    return a - b


def calculateDel(a, b):
    if b != 0:
        return a / b


def userChoice(c):
    if c == '1':
        return calculateSum
    elif c == '2':
        return calculateMinus
    elif c == '3':
        return calculateDel


myCalculation = userChoice('1')
print(myCalculation(2, 2))

# рекурсія - функція, яка викликає сама себе.

num = 1

while True:
    if num == 10:
        break
    num += 1


def factorialCalculation(num):
    if num == 0:
        return 1
    else:
        print(num, end="*")
        return num * factorialCalculation(num - 1)  # 5 * 4 * 3 * 2 * 1 * factorialCalculation(0)


print("--------------------------")
print(factorialCalculation(5))


def isStrPalindrom(myStr):
    if len(myStr) == 0:
        return True
    else:
        if myStr[0] == myStr[-1]:
            print(myStr[1:-1])
            return isStrPalindrom(myStr[1:-1])
        else:
            return False


str1 = 'madam'

print(isStrPalindrom(str1))


def findMin(numberList):
    if len(numberList) > 1:
        return min(findMin(numberList[:-1]), numberList[-1])
    else:
        return numberList[0]


nums = [2, 4, 1, 8, 10]
print("min = ", findMin(nums))
