# -*- coding: UTF-8 -*-
'''
@File           : code-01.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/17 3:51 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

fruits = ["apple", "banana", "bcherry"]
print(f"获取列表fruits的第一个元素: {fruits[0]} 索引为0")
print(f"获取列表fruits的第二个元素: {fruits[1]} 索引为1")
print(f"获取列表fruits的第三个元素: {fruits[2]} 索引为2")

words = ["hello", "world"]
upper_words = list(map(str.upper, words))
print(upper_words)

import itertools

# 使用itertools.cycle()创建一个无限循环的列表生成器
cycle_gen = itertools.cycle([1, 2, 3])
for _ in range(12):
    print(next(cycle_gen), end=' ')
print()

print(f"重复元素的列表: {list(itertools.repeat(5, 4))}")

matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)

gen_exp = (x ** 2 for x in range(10))
print(list(gen_exp))

my_list = [1, 2, 3, 4, 5]
print(f"获取下标为0的元素: {my_list[0]}")
my_list[0] = 10
print(f"修改下标索引为0的元素内容为10, value: {my_list[0]}")

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

# 切片赋值
my_list[1:4] = [90, 54, 76]
print(my_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 合并列表
# merged_list = list+list2
print(f"合并两个列表: {list1 + list2}")
# 复制列表
print(f"list1复制一份: {list1 * 2}")

number = [-2, -1, 0, 1, 2]
print(f"{[x ** 2 for x in number if x >= 0]}")

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"{[item for sublist in nested_list for item in sublist]}")

largn_gen = (x for x in range(100000))

# 逐个处理数据
for x in largn_gen:
    if x % 100000:
        print(x)

import itertools

# 创建一个大数据生成器并进行切片
large_gen = (x for x in range(100000))
sliced_gen = itertools.islice(large_gen, 1000, 1010)
print(list(sliced_gen))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"列表{list2}添加到列表{list1}中,添加后list1: {list1}")
