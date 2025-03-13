# -*- coding: UTF-8 -*-
'''
@File           : code-05.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-07 12:54 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''


def remove_duplicates(lst):
    """
    使用结合去重
    """
    return list(set(lst))


# 测试代码
original_list = [1, 2, 2, 3, 3, 4, 5, 6, 6, 0, 0]
deduplicated = remove_duplicates(original_list)
print("原始列表:", original_list)
print("去重后列表:", deduplicated)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % 2 == 0:
        del my_list[i]
print(my_list)

"""
使用列表解析
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [x for x in my_list if x % 2 != 0]
print(my_list)

"""
使用迭代器itertools
"""
import itertools

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in itertools.chain(my_list):
    if i % 2 == 0:
        my_list.remove(i)
print(my_list)

str_list = ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
for i in itertools.chain(str_list):
    if i == "h":
        str_list.remove(i)
print(str_list)

"""
切片操作
"""
my_list = [1, 2, 3, 4, 45, 7, 6]
for i in my_list[::-1]:
    if i % 2 == 0:
        my_list.remove(i)
print(my_list)

str_list = ['h', 'e', 'l', 'l', 'o']
for i in str_list[::-1]:
    if i == 'l':
        str_list.remove(i)
print(str_list)

"""
使用while 循环
"""
my_list = [1, 2, 4, 5, 6, 7, 3, 8]
while my_list:
    if my_list[0] % 2 == 0:
        my_list.pop(0)
print(my_list)


str_list = ['h', 'e', 'l', 'l', 'o']
while str_list:
    if str_list[0] == 'e':
        str_list.pop(0)
print(str_list)
