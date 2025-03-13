# -*- coding: UTF-8 -*-
'''
@File           : 01.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-11 3:31 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

"""
add()添加元素
"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

"""
删除元素
"""
fruits = {"apple", "banana", "cherry", "orange"}
fruits.remove("apple")
print(f"使用remove删除 {fruits}")
fruits.discard("cherry")
print(f"使用discard删除 {fruits}")

"""
in 成员检查
"""
fruits = {"apple", "banana", "cherry"}
contains_apple = "apple" in fruits
print(contains_apple)

"""
并集
"""
set1 = {1, 2, 4}
set2 = {3, 4, 7}
union_set = set1.union(set2)
print(union_set)

"""
交集
"""
set1 = {1, 2, 3,6}
set2 = {6, 3, 8,9}
intersection_set = set1.intersection(set2)
print(intersection_set)

"""
difference() 差集
"""
set1 = {1,2,3,4}
set2 = {1,2,0,4}
print(set1.difference(set2))
print(set1 - set2)

"""
symmetric_difference() 对称差集
"""
set1 = {1,2,3,4}
set2 = {7,6,3,5}
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

"""
集合推导式
"""
numbers = {1,2,3,4,5}
squared_numbers= {x**2 for x in numbers}    #创建一个包含数字平方的新集合
print(squared_numbers)

"""
frozenset类型 冻结集合
"""
frozen_set =frozenset({1,2,3,4})
for value in frozen_set:
    print(f"value : {value},type : {type(frozen_set)}")