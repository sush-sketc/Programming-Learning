# -*- coding: UTF-8 -*-
'''
@File           : code-06.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-11 12:14 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''
from collections import OrderedDict

"""
pop方法删除指定键的值
"""
my_dict = {'apple': 3, 'banana': 5, 'cherry': 7}
# 删除'banana'键对应的值
value = my_dict.pop('banana')
print(f"Before Delete my_dict = {my_dict},After deletion my_dict = {my_dict},返回删除对应的值: {value}")

# 删除pear键
value = my_dict.pop('pear', "没有")
print(value)

"""
popitem 方法随机删除一项
"""
my_dict = {'apple': 3, 'banana': 6, 'cherry': 9}
# 随机删除一项
item = my_dict.popitem()
print(item)

"""
扩展方法pop
"""
inventory = {'apple': 2, 'banana': 5, 'charry': 3}
# 使用pop方法从库存中取出并计算苹果的数量
apple_cont = inventory.pop('apple', 0)
total_cost = apple_cont * 2.5
print(f"Apple Count: {apple_cont},Total Cost: {total_cost}")

"""
动态更新字典中的值
"""
user_data = {"name": "John", "age": 35, 'poinst': 60}
# 使用pop更新用户的积分并添加新的值
points = user_data.pop('poinst', 0)
user_data['leve'] = 'Silver' if points >= 50 else 'Bronze'
print(user_data)

print("----------------")
"""
popitem 简单的缓存
"""

def get_data_from_server(key):
    # 模拟从服务器获取数据的操作
    return f"Data for {key}"

from collections import OrderedDict
cache = OrderedDict()

# 使用popitem实现一个简单的缓存，最多存储5个数据
def update_cache(key, data):
    if len(cache) >= 5:
      cache.popitem(last=False)  # 删除最早加入的数据
    cache[key] = data


# 测试缓存更新
for i in range(1,6):
    key = f"key-{i}"
    data = get_data_from_server(key)
    update_cache(key, data)
    # print(key,data)

# print(cache)
for key,value in cache.items():
    print(f"key=[{key}],value=[{value}]")

"""
随机删除元素
"""
import random

my_list = [1, 2, 3, 4, 5, 6, 7]
# 使用popitem随机删除列表中的一个元素
while my_list:
    index = random.randint(0, len(my_list) - 1)
    element = my_list.pop(index)
    print(f"Removed: {element},Remaining: {my_list}")