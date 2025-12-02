# Винятки
print("Hello")
# print(2 + "4")
# print(2/0)

# try except

# try:
# some bad code
# except:
# what to do with error


# try:
#     amount = int(input("Enter the amount of received items - "))
#     items_type = input("Enter the type of items  - ")
# except:
#     print("Amount should be an integer !")


# try:
#     amount = int(input("Enter the amount of received items - "))
#     items_type = input("Enter the type of items  - ")
#     parts_number = int(input("Enter the number of parts - "))
#     part_amount = amount / parts_number
#     print(f"Supply of {amount}, {items_type} saved!")
# except (ValueError, TypeError):
#     print("Amount should be an integer !")
# except ZeroDivisionError:
#     print("Cant divide by zero !")
# except Exception as ex:
#     print("We have some error - ", ex)
# finally:
#     print("Program has finished !")


# try:
#     num = int(input("Enter num - "))
#     print(num ** 2)
# except ValueError:
#     print("Error! Need a number !")
# else:  # working if no error
#     print("All is good !")
# finally:  # always working
#     print("Program has finished !")
#
#

try:
    salary = int(input("Enter salary - "))
    if salary < 0:
        raise Exception('Salary must be positive')
except Exception as ex:
    print("Error: ", type(ex).__name__, ex)

# Завдання 1
# Створіть програму для розрахунку фінальної ціни товару.
# Запитайте в користувача введення вихідної ціни та відсотка знижки.
# Оберніть перетворення введених даних і обчислення підсумкової ціни в блок try.
# Якщо відбувається помилка перетворення (наприклад, ValueError), перехопіть її в блоці except і виведіть повідомлення про помилку.
# У блоці finally (за необхідності) виведіть повідомлення про завершення обчислень.

print("Final price calculating")
try:
    price = float(input("Enter start product price - "))
    discount = float(input("Enter percent of discount - "))
    if discount < 0 or discount > 100:
        raise ValueError("Percent must be > 0 and < 100!")
    final_price = price * (1 - discount / 100)
    print(f"Final price of product: {final_price:.2f} uah")
except ValueError as ex:
    print(f"Input error: {ex}")
finally:
    print("Calculation finished!")


