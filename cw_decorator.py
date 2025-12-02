# decoration

def simpleDecorator(func):
    print("Hello ! i am decorator !")

    def simpleWrapper():
        print("func start working !")
        func()
        print("end working!")

    return simpleWrapper


def simpleDecorator_v2(func):
    print("Hello ! i am decorator 2!")

    def simpleWrapper():
        print("func start working !")
        func()
        print("end working!")

    return simpleWrapper


def simpleDecorator_v3(func):
    print("Hello ! i am decorator 3!")

    def simpleWrapper(n1, n2):
        print("func start working !")
        func(n1, n2)
        print("end working!")

    return simpleWrapper


def simpleDecorator_v4(func):
    print("Hello ! i am decorator 4!")

    def simpleWrapper(n1, n2):
        print("func start working !")
        result = func(n1, n2)
        print("end working!")
        return result

    return simpleWrapper


def decoratorWrapper(argForDec):
    print(f"I have {argForDec}")

    def simpleDecorator_v5(func):
        print(f"Hello ! i am decorator 5 with args {argForDec}")

        def simpleWrapper(n1, n2):
            print("func start working !")
            result = func(n1, n2)
            print("end working!")
            return result

        return simpleWrapper

    return simpleDecorator_v5


# @simpleDecorator
# @simpleDecorator_v2
def sayHi():
    print("Welcome !")


# @simpleDecorator
def sayBye():
    print("Bye!")


# sayHi()
#
# sayHiPro = simpleDecorator(sayHi)
#
# sayHiPro()

# sayHi = simpleDecorator(simpleDecorator_v2(sayHi))
# sayHi()

@simpleDecorator_v4
def addNums(num1, num2):
    return num1 + num2


print(addNums(2, 2))


def calcMultiply(a, b):
    return a * b


decoratingWithArg = decoratorWrapper(10)

calcMultiplyPro = decoratingWithArg(calcMultiply)

print(calcMultiplyPro(2, 2))

# example 1

pricesUSD = [100, 35, 77, 86, 34]
print(pricesUSD)


def priceToGrn(priceList):
    return list(map(lambda x: x * 42, priceList))


# def changePriceDecorator_v1(func):
#     print("Hello, let's change your price...")
#
#     def simpleWrapper(argList):
#         print("I have got list of prices ", argList)
#         result = func(argList)
#         resultWithDesc = list(map(lambda x: x * (1 - 0.15), result))
#         print("Set a discount !")
#         return resultWithDesc
#
#     return simpleWrapper


def setDiscountDecoratorWrapper(disc):
    print(f"I have {disc}")

    def changePriceDecorator_v2(func):
        print("Hello, let's change your price...")

        def simpleWrapper(argList):
            print("I have got list of prices ", argList)
            result = func(argList)
            resultWithDesc = list(map(lambda x: x * (1 - disc), result))
            print("Set a discount !")
            return resultWithDesc

        return simpleWrapper

    return changePriceDecorator_v2


# priceGrnsWithDesc = changePriceDecorator_v1(priceToGrn)
# print(priceGrnsWithDesc(pricesUSD))

priceGrnsWithDesc_v2 = setDiscountDecoratorWrapper(0.5)
newPrices = priceGrnsWithDesc_v2(priceToGrn)

print(newPrices(pricesUSD))

# print(priceToGrn(pricesUSD))

import time


def checkTime(func):
    def wrapper(*args):
        startTime = time.time()
        result = func(*args)
        print(f"Working time {time.time() - startTime}")
        if not result:
            return
        return result

    return wrapper


@checkTime
def testFunc():
    print("func working")
    time.sleep(1)


print(testFunc())