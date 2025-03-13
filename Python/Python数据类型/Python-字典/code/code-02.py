# -*- coding: UTF-8 -*-
'''
@File           : code-02.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/18 6:53 PM 
@Author         : None
@Version        : None
@Desciption     : None
返回文档         (../Python-字典常用方法.md)
'''

"""
dict.clear()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', 99, '男']
dic1 = dict(zip(list1, list2))
dic1.clear()

"""
dict.copy()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
dic2 = dic1
dic3 = dic1.copy()
dic4 = copy.deepcopy(dic1)
dic1['age'].remove(18)
dic1['age'] = 20

"""
dict.fromkeys()
"""
list1 = ['Author', 'age', 'sex']
dic1 = dict.fromkeys(list1)
dic2 = dict.fromkeys(list1, 'Python')

"""
dict.get()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18,99], '男']
dic1 = dict(zip(list1, list2))
Author = dic1.get('Author')
phone = dic1.get('phone')
phone = dic1.get('phone','12345678')

"""
dict.items()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 19], '男']

items = dict(zip(list1, list2))
items = dict.items(items)
print(f"items= ${items}")
print(type(items))
print('items = ', list(items))

"""
dict.keys()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 88], '男']
dic1 = dict(zip(list1, list2))
keys = dic1.keys()
print('Keys = ', keys)
print(type(keys))
print('keys = ', list(keys))
"""
dict.pop()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 88], '男']
dic1 = dict(zip(list1, list2))
print('dic1 = ', dic1)
sex = dic1.pop('sex')
print('sex = ', sex)
print('dict1 = ', dic1)

"""
dict.popitem()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [189.19], '男']
dic1 = dict(zip(list1, list2))
dic1.popitem()
print('dic1 = ', dic1)

"""
dict.setdefault()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
dic1.setdefault('Author', '')
print('dic1 = ', dic1)
dic1.setdefault('name', 'Hello')
print('dic1 = ', dic1)

"""
dict.update()
"""
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
print("dic1 = ", dic1)
list3 = ['Author', 'phone']
list4 = ['Gello', 12343]

dic2 = dict(zip(list3, list4))
print("dic2 = ", dic2)
dic1.update(dic2)
print("dic1 = ", dic1)

"""
dict.values()
"""
list1 = ['author', 'age', 'sex']
list2 = ['Python', [12, 234], '男']
dic1 = dict(zip(list1, list2))
values = dic1.values()
print('values = ', values)
print(type(values))
print('values = ', list(values))
