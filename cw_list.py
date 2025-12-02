# list

nums = [10, 20, 30, 40, 50, 50]
print(nums)

for num in nums:
    print(num)

emptyList = []

students = ['Djon', 'Bill', "Kate"]
mixList = [123, -123, 3.76, True, "text", [1, 2, 3]]
print(mixList)

newList = list((1, 2, 3))
print(newList)

print(len(mixList))

print(students[0])
print(students[1])

print(nums[:len(nums) // 2])

# change item
students[0] = "Miha"
print(students)

print(nums.count(50))
if 100 in nums:
    print(nums.index(100))

print(nums.append(60))
print(nums)

nums.insert(0, -10)
print(nums)

nums.pop(0)
nums.remove(10)

print(nums)

nums.extend([1, 2, 3])
print(nums)

import random

prices = []

for i in range(10):
    prices.append(random.randint(100, 500))

print(prices)

print(sum(prices))
print(max(prices))
print(min(prices))

# Рівень 1
# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних і непарних чисел.
# Результати вивести на екран.

nums = []
for i in range(10):
    nums.append(random.randint(-100, 100))

evenNum = 0
oddnum = 0
for num in nums:
    if not num % 2:
        evenNum += 1
    else:
        oddnum += 1

print(nums)
print(f"even nums: {evenNum}")
print(f"odd nums: {oddnum}")

#
# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення у списку.
# Результати вивести на екран.decorator

min = nums[0]
for num in nums[1:]:
    if num < min:
        min = num
print(f"min num - {min}")
#
# Рівень 2
# Завдання 3
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний, від'ємний елемент,
# порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран.
min = nums[0]
i = 0
while min < 0:
    i += 1
    min = nums[i]

for num in nums:
    if num < min and num > 0:
        min = num
print(f"min num - {min}")
