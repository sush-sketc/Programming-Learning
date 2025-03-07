# -*- coding: UTF-8 -*-
'''
@File           : code-04.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/18 2:29 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

"""
sorted()
"""
# 按照字母排序
str_string = ["The", "is", "python", "happy"]
# 按照数字排序
int_sorted = [4, 9, 12, 5, 21, 1]
sorted_list = sorted(str_string)
int_sorted_list = sorted(int_sorted)
print(int_sorted_list)
print(sorted_list)

"""
sort()
"""
fruits = ['apple', 'orange', 'banana', 'grage']
int_sorted = [43, 1, 0, 54, 21, 43]
fruits.sort()
int_sorted.sort()
print(f"{fruits}\n{int_sorted}")

# 高级排序方法
"""
key
"""
words = ['python', 'is', 'awesome', 'language']
sorted_words = sorted(words, key=len)
print(sorted_words)

"""
reverse
"""
# 字符串逆序排序
words = ['python', 'is', 'awesome', 'language']
# 数字逆序排序
int_reversed = [3, 4, 42, 32, 0, 88, 99]
sorted_desc = sorted(words, reverse=True)
sorted_int = sorted(int_reversed, reverse=True)
print(f"{sorted_desc}\n{sorted_int}")

"""
利用Lambda表达式定制排序
"""
students = [('Alice', 12), ('Bob', 20), ('Charlie', 30)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

"""
稳定排序与不稳定排序
"""
pairs = [(91, 2), (0, 43), (32, 13), (4, 343)]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)

"""
sort()（默认升序排序）
"""
numbers = [4, 6, 1, 0, 7, 4]
numbers.sort()
print(numbers)

"""
sort()（降序排序）
"""
numbers = [4, 0, 23, 65, 1, 43, 78]
numbers.sort(reverse=True)
print(numbers)

"""
自定义关键字排序
"""
words = ["apple", "banana", "orange", "kiwi"]
#从下标为1的元素开始排序
words.sort(key=lambda x: x[1])
print(words)
#从下标为2的元素排序，
words.sort(key=lambda x: x[2])
print(words)
#从末尾元素进行排序
words.sort(key=lambda x: x[-1])
print(words)
