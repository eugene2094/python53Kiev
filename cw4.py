num1 = 10
num2 = 20
num3 = 30

# list списки

# creating list
numbers = [10, 20, 30]
print(numbers)
print(type(numbers))

courses = list(('Math', 'Design', 'Blogging'))
print(courses)

elements = [123, 123, "Djon", True, 3.14]
print(elements)

list1 = [i for i in range(1, 11)]
print(list1)

print(elements[0])
print(elements[2])
print(elements[len(elements) - 1])
print(len(elements))

print(list1[:len(list1) // 2])
print(list1[len(list1) // 2:])
print(list1[::-1])

# change element in list

marks = [10, 2, 9, 11, 8]
print(marks)
marks[1] = 10
print(marks)

marks = []

# python methods for list

prices = [100, 234, 567, 44, 24, 6, 99]
print(f"count of elem: {len(prices)}")
print(f"Sum of proces: {sum(prices)} $")
print(f"max price: {max(prices)}")
print(f"min price: {min(prices)}")
print(f"sorted prices: {sorted(prices)}")

category1 = ["drama", "comedy"]
category2 = ["Action"]
print(category1 + category2)
print(category1 * 2)

# methods of list
categories = category1 + category2
print(categories)
categories.append("Fantasy")
print("add fantasy")
print(categories)
categories.insert(0, "horror")
print(categories)
categories.extend(category1)
print(categories)

# del elem
categories.pop()
categories.pop(1)
categories.remove('drama')
# categories.clear()
print(categories)
if 'horror' in categories:
    print(categories.index('horror'.lower()))

print(categories.count('Fantasy'))
categories.sort()
categories.reverse()
print(categories)

new_cats = categories.copy()
categories.pop()
print(new_cats)

studScores = [['Bob', 11, 6, 8, 12],
              ['Jane', 4, 6, 7, 9],
              ['Bill', 12, 12, 1, 12]]

print(studScores)

for cat in categories:
    print(cat)

for stud in studScores:
    for data in stud:
        print(data, end=" | ")
    print()

# numbers = []
# num = -1
#
# while num != 0:
#     num = int(input("Enter num - "))
#     numbers.append(num)
#
# print(f"sum: {sum(numbers)}")
# print(f"avg: {sum(numbers) / (len(numbers) - 1)}")


nums = input("Enter nums : ")
nums = nums.split()
nums = [int(elem) for elem in nums]

print(nums)
print(f"sum: {sum(nums)}")
print(f"avg: {sum(nums) / (len(nums))}")


