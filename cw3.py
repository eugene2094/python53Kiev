# ЦИКЛИ FOR WHILE

# for i in collection:
# дія

for i in 1, 2, 3, 4, 5:
    print(i)

for s in "python":
    print(s, end=" ")

print("\nend for")

# range() - генерує діапазон чисел від 0 до числа яке вказано як аргумент

for num in range(5):
    print(num)

print("----------------")
for num in range(1, 11):
    print(num)

print("----------------")
for num in range(1, 11, 2):
    print(num)

print("----------------")
for num in range(10, 0, -1):
    print(num)

if 'n' in "small":
    print("yes")
else:
    print("no")
#
# total = 0
# count = 0
# lastNum = int(input("Enter upper value - "))
# for num in range(1, lastNum + 1):
#     count += 1
#     total += num
#
# print("Total:", total)
# print(count)
# print("Avg:", total / count)

# while умова:
# тіло цикла

# count = 0
# while count < 10:
#     count += 1
#     print("count:", count)
#
# from random import randint
#
# randNum = randint(1, 100)
# userNum = 0
# print(randNum)
# while userNum != randNum:
#     userNum = int(input("Enter num 1-100 - "))
#     if userNum < randNum:
#         print("Try higher...")
#     elif userNum > randNum:
#         print("Try lower...")
# else:
#     print("Winnner!")
#
# password = "admin"
# user_pass = ""
#
# while user_pass != password:
#     user_pass = input("enter password - ")
# else:
#     print("Success")

# break / continue
# num = 0
# while True:
#     num = int(input("Enter num - "))
#     if num == 0:
#         print("Stop")
#         break
#
#     if num % 2 == 0:
#         print(num)
#     else:
#         print("next iteration")
#         continue
#
# for num in range(20):
#     if num == 10:
#         break
#     print(num)

# вкладені конструкцї

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()


