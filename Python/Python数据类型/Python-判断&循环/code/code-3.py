# -*- coding: UTF-8 -*-
'''
@File           : code-3.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/12 2:28 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

student_scores = {"alice": 85, "Bob": 90, "Charlie": 78}
for student, score in student_scores.items():
    print(f"{student}:{score}")

print("###########################")
while True:
    number = int(input("请输入一个正数: "))
    if number > 0:
        break
    print("输入无效，请重试。")
print(f"你输入的正数是: {number}")

print("###########################")
words = ["apple", "banana", "cherry"]
for index, word in enumerate(words):
    print(f"index: {index},value: {word}")

print("###########################")
names = ["Alice", "Bob", "Charlie"]
scores = [83, 45, 67]
for name, score in zip(names, scores):
    print(f"{name}: {scores}")

print("###########################")
# 字符串
strings = "hello"
# 数组
arr = [1, 2, 3, 4, 5, 6]
# 元组
fruits = ("apple", "banana", "cherry")
# 字典
person = {"name": "Alice", "age": 25, "city": "Shanghai"}

# zip
for i in zip(strings, arr, fruits, person.values()):
    print(i)

print("###########################")

for i in enumerate(fruits, 0):
    print(i)

print("###########################")

for index, value in enumerate(zip(strings, arr, fruits, person.values())):
    print(f"index: {index},value: {value}")

print("###########################")
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

print("###########################")
numb = 5
factorial = 1
while numb > 1:
    factorial *= numb
    numb -= 1
print(f"factorial: {factorial}")
print("###########################")
# 计算两个数的最大公约数
a, b = 48, 18
while b:
    a, b = b, a % b
print(f"最大公约数是: {a}")

print("############鸡兔同笼##############")


def solve_chichen_rabbit_problem(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            return chickens, rabbits
    return None, None


# 输入头和脚的数量
heads_input = int(input('Enter the number of heads: '))
legs_input = int(input('Enter the number of legs: '))

# 解决问题并输出结果

result_chichens, result_rabbits = solve_chichen_rabbit_problem(heads_input, legs_input)
if result_chichens is not None:
    print(f"Number of chichens: {result_chichens}")
    print(f"Number of rebbits: {result_rabbits}")
else:
    print("No solut found.")
