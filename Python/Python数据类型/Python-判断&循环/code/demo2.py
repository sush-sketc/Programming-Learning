# -*- coding: UTF-8 -*-
'''
@File           : demo2.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/8 4:18 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print(fruit)
        break
    print(fruit)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

total = 0
number = 1
while number <= 5:
    total += number
    number += 1
print("从1到5的和分别是：", total)

number = 1
while number <= 5:
    if number == 3:
        break  # 当遇到 3 时，提前终止循环
    print(number)
    number += 1

numberr = 1
while numberr <= 5:
    if numberr == 3:
        numberr += 1
        continue  # 当遇到 3 时，跳过本次进入下次循环
    print(numberr)
    numberr += 1

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 使用 range() 函数生成数字序列
for i in range(1, 6):  # 从 1 到 5
    print(i)

# 统计循环执行的次数
count = 0
for _ in range(10):
    count += 1
print("循环执行了", count, "次")

# 累积计算
total = 0
for number in range(1, 6):
    total += number
print("从1到5的和是:", total)

# 从用户输入获取数据
# name = input("请输入您的名字: ")
# print("您的名字是:", name)

# ----------

## for 循环高级应用

### 迭代对象和可迭代性
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)
my_tuple = ("apple", "banana", "cherry")
for num in my_tuple:
    print(num)
my_string = "Hello"
for num in my_string:
    print(num)

for i in range(5):
    print(i)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for enumerate in row:
        print(row, enumerate)

colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]

for color in colors:
    for size in sizes:
        print(f"{color} {size}")

# print("----------------------------")
# fruits_enumerate = ['apple', 'banana', 'cherry']
# for index, value in enumerate(fruits_enumerate):
#     print(f"Index: {index},Value: {value}")

print("----------------------------")
fruits_zip = ['apple', 'banana', 'cherry']
colors_zip = ['red', 'yellow', 'purple']
for fruit, color in zip(fruits_zip, colors_zip):
    print(f"Fruit: {fruits},Color: {colors}")

print("----------------------------")
count_bu = 0
while count_bu < 4:
    print("Inside the loop", count_bu)
    count_bu += 1
else:
    print("Loop finished", count_bu)

print("----------------------------")
squares = [x ** 2 for x in range(3)]
print(squares)

print("----------------------------")
enen_squaraes = [x ** 2 for x in range(5) if x % 2 == 0]
print(enen_squaraes)

print("----------------------------")

num = 1
mte1 = 1

while num <= 5:
    if num % 2 != 0:
        mte1 *= num
    num += 1
print(f"1-5奇数的累积乘积是{mte1}")

print("----------------------------")
num1 = 1
while num1 <= 5:
    if num1 == 3:
        print(f"num1 value: {num1}")
        break
    num1 += 1
print(f"num1 value: {num1}")

# i = 1
# while i <= 3:
#     age = int(input('input: '))
#     girl_age = 18
#     if age == girl_age:
#         print('猜对了')
#         break
#     else:
#         print('猜错了')
#     i += 1
# else:
#     print("对不起，我们不合适")
# print('结束游戏')

print("----------------------------")
# value = float(input("请输入长度:"))
# unit = input("请输入单位：")
#
# # 如果输入的是厘米
# if unit == "cm" or unit == "厘米":
#     output_value = value / 2.54
#     print("%f 厘米 = %f 英寸" % (value, output_value))
# # 如果输入的是英寸
# elif unit == "in" or unit == "英寸":
#     output_value = value * 2.54
#     print("%f 英寸 = %f 厘米" % (value, output_value))
# else:
#     print("输入有效单位！")


print("----------------------------")
from random import randint

# 产生 1～6的随机数
num = randint(1, 6)
if num == 1:
    res = '吃饭'
elif num == 2:
    res = '睡觉'
elif num == 3:
    res = '喵喵叫'
elif num == 4:
    res = '汪汪叫'
elif num == 5:
    res = '打豆豆'
elif num == 6:
    res = '写代码'
print(res)

print("----------------------------")
import random

print(random.randint(1, 100))  # 产生 1 ~ 100 的整数型随机数
print(random.random())  # 产生 0 ~ 1 之间的随机浮点数
print(random.uniform(1.1, 5.4))  # 产生 1.1 ~ 5.4 之间的随机浮点数，区间可以不是整数
print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数

# 将序列a中的元素顺序打乱
a = [1, 3, 5, 6, 7]
random.shuffle(a)
print(a)

print("----------------------------")
from random import randint

d = {1: "吃饭", 2: "睡觉", 3: "喵喵叫", 4: "汪汪叫", 5: "打豆豆", 6: "写代码"}
# 产生 1-6 随机整数
num = randint(1, 6)
print(d[num])

print("----------------------------")
# import math
#
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     p = a + b + c
#     arae = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("周长 = %.2f,面积 = %.2f" % (p, arae))
# else:
#     print("所输入的值无法形成三角形")

# salary = float(input('本月收入：'))
# insurance = float(input('五险一金：'))
# diff = salary - insurance - 5000
# if diff <= 0:
#     rate = 0
#     deduction = 0
# elif diff < 3000:
#     rate = 0.03
#     deduction = 0
# elif diff < 12000:
#     rate = 0.1
#     deduction = 210
# elif diff < 25000:
#     rate = 0.2
#     deduction = 1410
# elif diff > 35000:
#     rate = 0.25
#     deduction = 2660
# elif diff > 55000:
#     rate = 0.3
#     deduction = 4410
# elif diff > 80000:
#     rate = 0.35
#     deduction = 7160
# else:
#     rate = 0.45
#     deduction = 15160
# tax = abs(diff * rate - deduction)
# print('个人所得税: ¥%.2f元' % tax)
# print('实际到手收入: ¥%.2f元' % (diff + 5000 - tax))

import time
for i in range(5):
    print("Hello Python")
    time.sleep(1)


