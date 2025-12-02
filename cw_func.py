# функції

def printMsg():
    print("Hello from my first function !")


printMsg()
printMsg()
printMsg()
printMsg()

print("hello", 'test')


def printMsgnew(msg):
    print(msg)


printMsgnew("new facts")


def plusNums(num1, num2, num3):
    # print(num1 + num2 + num3)
    return num1 + num2 + num3


sum = plusNums(2, 2, 2) + 10
print(sum)

if "2".isdigit():
    print("ok")


def checkLog(userLog):
    if userLog == 'admin':
        return userLog.lower()
    elif userLog == 'user':
        return userLog.upper()
    else:
        return "wrong str"


print(checkLog('admin'))
print(checkLog('user'))


def userGreetings(login, passw="admin"):
    if login == 'admin' and passw == 'admin':
        print("Welcome !")
    elif login == 'student':
        print("Welcome student!")
    else:
        print("Welcome guy!")


userGreetings("admin", "qewrty")


# *args
def sumOfNums(*args):
    print(list(args))
    sum = 0
    for elem in args:
        sum += elem
    return sum


nums = [1, 2, 3]

print(sumOfNums(*nums))

# local and global namespace
number = 100


def multiplyNums(num1, num2):
    # start local namespace
    global number
    number = 200
    print(number)
    localNum = 1
    return num1 * num2


# print(localNum)

multiplyNums(2, 2)
print(number)




