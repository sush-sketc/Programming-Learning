# -*- coding: UTF-8 -*-
'''
@File           : code-03.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/17 7:09 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

my_list = [1, 2, 3, 4]
my_list.append(10)
print(f"列表{my_list}末尾添加元素10，添加后: {my_list}")

print("---------------")
my_list = [1, 2, 3, ]
my_list.insert(1, 4)
print(f"在索引位置为1，插入元素4,插入后的结果: {my_list}")

print("---------------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"将list2列表合并到list1列表中，合并后的结果为: {list1}")

list2 = list2 + list1
print(f"使用+运算符将list2和list1进行合并，合并后结果为:{list2}")

print("---------------")

my_list = [1, 2, 3, 4]
new_list = [x + 1 for x in my_list]  # 通过for循环将每个元素+1
print(f"每个元素+1后结果为: {new_list}")

print("---------------")
my_list = [1, 2, 3, 4]
new_list = ["hello", "world"]
my_list.remove(3)
new_list.remove("hello")
print(f"删除位置索引为3的元素,结果为: {my_list}")
print(new_list)

print("---------------")
my_list = [1, 2, 3, 4, 5]
new_list = ["hellow", "world", "Python"]
popped_element = my_list.pop(1)
new_element = new_list.pop(2)
print(f"删除下标索引为1的元素,返回被删除的元素: {popped_element},删除后列表my_list: {my_list}")
print(f"删除列表new_list下标索引为2的元素,返回删除被删除的元素: {new_element},删除后列表new_list {new_list}")

print("----------------")
my_list = [1, 2, 3, 4]
del my_list[1]
print(f"删除索引为1的元素。结果为: {my_list}")
del my_list  # 删除整个列表
str_list = ["Hello", "World", "Python"]
del str_list[2]
print(f"删除索引为2的元素，删除后结果为: {str_list}")
del str_list

print("----------------")

my_list = [1, 2, 3, 4, 5, 6, 7]
# 删除所有奇数元素
my_list = [x for x in my_list if x % 2 == 0]
print(my_list)

print("----------------")
my_list = ["Hello", "World", "Python"]
print(f"查找\'Java\'字符串是否包含在列表my_list中，结果为 {'Java' not in my_list}")
print(f"查找\'Python\'字符串是否包含在列表my_list中，结果为 {'Python' not in my_list}")

print("----------------")
my_list = [1, 2, 3, 4, 5]
element_to_ckeck = 3
if element_to_ckeck in my_list:
    print(f"{element_to_ckeck} 存在于列表中")
else:
    print(f"{element_to_ckeck} 不存在于列表中")

# 或者使用not in 判定不存在
element_to_ckeck = 6
if element_to_ckeck not in my_list:
    print(f"{element_to_ckeck} 不存在于列表中")
else:
    print(f"{element_to_ckeck} 存在于列表中")

print("----------------")

my_list = ["Hello", "World", "Python"]
element_to_check = "Hello"
if my_list.count(element_to_check) > 0:
    print(f"{element_to_check} 存在于字符串my_list中")
elif my_list.count("Java") > 0:
    print(f"\'Java\' 存在于字符串my_list中")
else:
    print(f"{element_to_check} 不存在于字符串my_list中")

print("----------------")
my_list = ["Hello", "World", "Python"]
if any(x == "Hello" for x in my_list):
    print(f"\'Hello\' 存在于列表中")
else:
    print(f"\'Hello\' 不存在于列表中")

print("----------------")
my_list = ["Hello", "World", "Python"]
if next(filter(lambda x: x == "Helwlo", my_list), None) is not None:
    print(f"\'Helwlo\' 存在于列表中")
else:
    print(f"\'Helwlo\' 不存在于列表中")

print("----------------")
my_list = ["Hello", "World", "Python"]
if "Hello" in set(my_list):
    print(f"\'Hello\' 存在于列表中,其下标为{my_list.index('Hello')}")
else:
    print(f"\'Hello\' 不存在于列表中")
if "Python" in set(my_list):
    print(f"\'Python\' 存在于列表中,其下标为:{my_list.index('Python')}")
else:
    print(f"\'Hello\' 不存在于列表中")

print("----------------")
from bisect import bisect_left

my_list = ["Hello", "World", "Python"]
sorted_list = sorted(my_list)
if bisect_left(sorted_list, "Python"):
    print(f"排序后: {sorted_list}")
    print(f"\'Python\' 存在于列表中,其下标为:{sorted_list.index('Python')}")
else:
    print(f"\Python\' 不存在于列表中")

print("----------------")
import numpy as np

my_list = ["Hello", "World", "Python"]
if np.isin("Python", my_list):
    print(f"\'Python\' 存在于列表中,其下标索引为 {my_list.index('Python')}")
else:
    print(f"\Python\' 不存在于列表中")

print("----------------")
my_list = ["Hello", "World", "Python"]
if any(element == "World" for element in my_list):
    print(f"\'World\' 存在于列表中,其下标索引为: {my_list.index('World')}")
else:
    print(f"\'World\' 不存在于列表中")

print("----------------")
my_list = [1, 2, 3, 4]
if (all(x > 3 for x in my_list)):
    print("列表中所有元素均大于3")
else:
    print("列表中所有元素有存在小于3的")

my_list = ["Hello", "World", "Python"]


def contains_element(lst, element):
    return any(x == element for x in lst)


print("----------------")
if contains_element(my_list, "Python"):
    print(f"\'Python\' 存在于列表中,其下标索引为: {my_list.index('Python')}")
else:
    print(f"\'Python\' 不存在于列表中")
