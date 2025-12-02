'''
if умова:  якщо правда в умові то виконується дія 1  інікше дія 2
   дія 1
else:
   дія 2
'''
# number = int(input("Enter number - "))
# if number > 0:
#     print("positive")
# else:
#     print("negative")
#
# num1 = int(input("Enter num 1:"))
# num2 = int(input("Enter num 2:"))
# select = input("What to do + - ")
# if select == '+':
#     print(num1, " + ", num2, "=", num1 + num2)
# else:
#     print(num1, " - ", num2, "=", num1 - num2)

# Треба запитати вік людини та сказати чи повнолітня вона


#  <  >    >=    <=  == !=   True False

print(3 <= 2)
print(3 > 2)
print('qwerty' > 'asd')

#  and  or

# True  and True
number = 11
if number > 0 and number < 10:
    print("number ok")
else:
    print("error number")

year = 2025

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Year ", year, "високосний")
else:
    print("Year ", year, " не високосний")

if not year % 4 and year % 100 or not year % 400:
    print("Year ", year, "високосний")
else:
    print("Year ", year, " не високосний")

# 0 - False 1 - True

car_speed = 100
if 50 < car_speed < 130:  # car_speed > 50 and car_speed < 130:
    print("speed is ok")
else:
    print("to fast !")

temp = 35
if temp >= 30:
    print("very hot")
elif temp >= 20 and temp < 30:
    print("warm")
elif temp > 0 and temp < 20:
    print("cold")
else:
    print("too cold")

# треба запитати вік і як результат сказати до якої вікової групи належить людина - школяр, студент, співробітник

login = "admin"
password = "admin"

if login == 'admin2':
    print("Your login is correct !")
    if password == "admin":
        print("Welcome in app!")
    else:
        print("Error password !")
else:
    print("Error login !")
