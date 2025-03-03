# -*- coding: UTF-8 -*-
'''
@File           : code-04.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/18 2:29 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

str_string= ["The","is","python","happy"]
sorted_list = sorted(str_string)
print(f"\'sorted\'方法返回一个新的排序列表，结果为: {sorted_list}")

print("-----------------")
print("-----------------")
fruits = ['apple','orange','banana','grage']
fruits.sort()
print(fruits)

print("-----------------")
words = ['python','is','awesome','language']
sorted_words = sorted(words,key=len)
print(sorted_words)

print("-----------------")
words = ['python','is','awesome','language']
sorted_desc = sorted(words, reverse=True)
print(sorted_desc)