# global namespace
messege = ""


def showInfo(messege):
    print(messege)
    return messege


showInfo("Some text")

text = showInfo("test")
print(text)


def temp_analise(temp):
    if temp > 50 or temp < -50:
        return "Error temp"
    else:
        if temp > 30:
            return f"Very hot.Temp is {temp}"
        elif temp > 15:
            return f"Warm.Temp is {temp}"
        elif temp > 0:
            return f"Cold.Temp is {temp}"


def decor_temp_f(func):
    def wrapper(*args):
        result = func(*args)
        return f"{result} F"

    return wrapper


@decor_temp_f
def fahrengeit_from_C(tempC):
    if isinstance(tempC, (int, float)):
        return 1.8 * tempC + 32
    else:
        return Exception("Error temp")


temperature = int(input("Enter temp - "))

fahrengeit_temp = fahrengeit_from_C(10)
print(fahrengeit_temp)
