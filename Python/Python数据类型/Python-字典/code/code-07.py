# -*- coding: UTF-8 -*-
'''
@File           : code-07.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-11 2:13 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

"""
字典-键值互换
"""
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict)

"""
依据某种依赖调价你-过滤字典
"""
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 3:
        new_dict[key] = value
print(new_dict)

"""
利用字典值进行计算
"""
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value
print(total_income)

"""
字典推导式
"""
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

"""
利用字典推导式，实现键值转换
"""
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)

"""
利用字典推导，过滤字典
"""
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)

"""
利用字典推导，计算值
"""
incomes = {'apple': 5600.00, 'orange': 4500.00, 'banana': 4000}
total_icome = sum([value for value in incomes.values()])
total_icome_new= sum(incomes.values())
print(total_icome,total_icome_new)

"""
字典排序
"""
incoms = {'apple':5600.00,'orange':4500.00,'banana':4000}
sorted_incom = {k: incoms[k] for k in sorted(incoms)}
print(sorted_incom)

"""
mao()函数
"""
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount,prices.items()))
print(new_prices)


"""
filter()函数
"""
prices = {'apple':0.40,'orange':0.35,'banana':0.25}
def has_low_price(price):
    return prices[price]<0.4

low_price = list(filter(has_low_price,prices.keys()))
print(low_price)

"""
字典解包运算
"""

vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': 0.25}
print({**vegetable_prices, **fruit_prices})