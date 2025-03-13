# -*- coding: UTF-8 -*-
'''
@File           : code-03.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-05 9:55 PM 
@Author         : None
@Version        : None
@Desciption     : None
返回文档        （../Python-字典(dict)常用操作.md）
'''
"""
字典创建
"""
my_dict = dict(name='张三', age=30, city="北京")
print("name = ", my_dict['name'])

"""
dict()函数
"""
my_dict = dict(name='张三', age=30, city="北京")
address = my_dict.get('address', '地址未知')
print(address)

"""
访问字典中的值
"""
my_dict = dict(name='张三', age=30, city="北京")
print("name = ", my_dict['name'])
address = my_dict.get('address', '地址未知')
print(address)  # 输出：地址未知

"""
修改字典中的值
"""
my_dict = dict(name='张三', age=30, city="北京")
print("原 my_dict = ", my_dict)
my_dict['age'] = 44
my_dict['address'] = "上海"
print("修改后 my_dict = ", my_dict)

"""
删除字典中的元素
"""
my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
del my_dict['age']
print("del 删除", my_dict)
print("pop方法删除", my_dict.pop('city'))

"""
字典的遍历
"""
my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
for key, value in my_dict.items():
    print("keys =%s \tvalues = %s" % (key, value))

my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
for key, value in my_dict.items():
    if key == 'title':
        print(f"{key}-{value}")
        # 按值排序
        sourted_dict = {key: value for key, value in sorted(my_dict.items(), key=lambda item: item[1])}
        break
    elif key != 'title':
        # copy()拷贝
        new_dict = my_dict.copy()
        # 向新拷贝的字典中添加值
        new_dict["title"] = "alice@example.com"
        # 输出new_dict中所有元素的键
        print("Keys = ", new_dict.keys())
        # 输出new_dict中所有值
        print("values = ", new_dict.values())
        # 获取字典的长度
        print("length", len(new_dict))
        break
    else:
        print("not key")
        break
# print(my_dict)
# print(new_dict)

https://www.yuque.com/fcant/python/nef08f5gh9i0vnrw#iDuPR

