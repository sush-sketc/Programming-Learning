# -*- coding: UTF-8 -*-
'''
@File           : code-04.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-07 1:17 PM
@Author         : None
@Version        : None
@Desciption     : None
'''

"""
元组索引和切片
"""

fruits = ("apple", "banana", "cherry")
# 获取第一个元素，索引为0
first_fruit = fruits[0]
print(first_fruit)
# 获取第二个元素，索引为1
second_fruit = fruits[2]
print(second_fruit)
# 获取索引1到2的子元组，不包括索引3
sliced_fruit = fruits[1:3]
print(sliced_fruit)

"""
修改元组值
"""
# fruits = ('apple', 'banana', 'cherry')
# fruits[0] = 'orange'

"""
in关键字查找
"""
fruits = ['apple', 'banana', 'cherry']
contains_apple = 'apple' in fruits
print(contains_apple)

"""
len()获取元组的长度
"""
fruits = ['apple', 'banana', 'cherry']
length = len(fruits)
print(len(fruits))

"""
+ 合并两个元组
"""
fruits1 = ['apple', 'banana', 'cherry']
fruits2 = ['南京', '北京', '上海']
combiend_fruits = fruits1 + fruits2
print(combiend_fruits)
print(fruits1 + fruits2)

"""
元组的解包
"""
fruits = ['apple', 'banana', 'cherry']
first, second, third = fruits
print(f"first={first}, second={second}, third={third}")

"""
元组推导式
"""
numbers = [1.2, 3, 4, 5]
squared_numbers = tuple(x ** 2 for x in numbers)
print(squared_numbers)
print(tuple(x ** 2 for x in numbers))

"""
可变列表
"""
grades = [85, 90, 78, 92]
grades.append(32)
grades[1] = 33
print(grades)
