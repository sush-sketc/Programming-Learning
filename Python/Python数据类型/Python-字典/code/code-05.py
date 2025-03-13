# -*- coding: UTF-8 -*-
'''
@File           : code-05.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-11 9:44 AM 
@Author         : None
@Version        : None
@Desciption     : None
'''

"""
遍历字典键
"""

my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for k in my_dict.keys():
    print(f"key=[{k}]")

"""
只用values()遍历值
"""
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for value in my_dict.values():
    print(f"value{value}")

"""
items()遍历键值对
"""
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for key, value in my_dict.items():
    print(f"key:[{key}],value:{value}")

"""
判断键是否存在
"""
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
if "name" in my_dict:
    print("Name is in the dictionary.")

"""
获取字典的长度
"""
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
print(f"The dictionary contains {len(my_dict)} key-value pairs.")

"""
字典的排序-按键排序
"""
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print(sorted_dict)

"""
字典排序-按值和自定义排序规则
"""
# my_dict = [11,43,65,76,87,4,0,45]
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
sorted_dict = {key: value for key,value in sorted(my_dict.items(),key=lambda item: item[1])}
print(sorted_dict)