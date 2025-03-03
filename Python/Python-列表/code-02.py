# -*- coding: UTF-8 -*-
'''
@File           : code-02.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/17 5:25 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"列表合并list1={list1},list2={list2},合并后{list1 + list2}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print(list1)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)


from itertools import chain
list1 =[1,2,3]
list2=[4,5,6]
print(f"实现多个列表的合并:{list(chain(list1,list2))}")



hr_department = ['Alice','Bob','Charlie']
it_department = ['David','Eva','Frank']
hr_department.extend(it_department)
print(f"使用extend()方法合并: {hr_department}")


students=[{'name':'Alice','age':13},{'name':'Bob','age':15}]
teachers = [{'name':'Eva','subject':"Math"},{'name':'Mike','subject':'English'}]
all_personnel = [*students,*teachers]
print(all_personnel)