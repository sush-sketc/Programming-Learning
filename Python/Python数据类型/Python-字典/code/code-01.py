# -*- coding: UTF-8 -*-
'''
@File           : code-01.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/18 4:16 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''
import time , datetime

another_dict = dict(name="Bob", age=25, city="San Francisco")
name = another_dict["name"]
age = another_dict["age"]
print(f"name: {name}, age: {age}")

# 使用 get() 方法获取值
city = another_dict.get("city")
print(f"city: {city}")



my_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
# 添加新的键值对
my_dict["email"] = "alice@example.com"
# 修改已有的键值
my_dict["age"] = 90
print(my_dict)
print("-----------------------------")

my_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"my_dict原值: {my_dict}")
# 使用del语句删除元素
del my_dict["age"]
print(f"删除键为\'age\'的元素,结果为: {my_dict}")

print("-----------------------------")
#使用pop()方法删除元素
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"New_dict原值{New_dict}")
# 使用del语句删除元素
new = New_dict.pop("name")
print(f"pop函数返回被删除指定键的值{new}")
print(f"删除键为\'name\'的元素,结果为: {New_dict}")

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
for key in New_dict.keys():
    print(f"字典New_dict的key: {key}")

print("-----------------------------")
for value in New_dict.values():
    print(f"字典New_dict的value: {value}")

print("-----------------------------")
for key,value in New_dict.items():
    print(f"字典New_dict: key[{key}],value: [{value}]")

print("-----------------------------")
# 使用in
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
if "name" in New_dict:
    print(f"字典New_dict中存在\'name\'键，值为:{New_dict['name']}")
else:
    print(f"字典New_dict中不存在\'name\'键")
print("-----------------------------")
#使用not in
if "age" not in New_dict:
    print(f"字典New_dict中不存在\'name\'键")
else:
    print(f"字典New_dict中存在\'age\'键，值为:{New_dict['age']}")

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"字典New_dict的长度为:{len(New_dict)}")

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}.clear()
print(New_dict)

print("-----------------------------")
numbers = [1, 2, 3, 4, 5]
square_dict = {num: num ** 2 for num in numbers}
print(square_dict)

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
sorted_dict = {key: New_dict[key] for key in sorted(New_dict)}
print(sorted_dict)

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
sorted_dict = {key: value for key, value in sorted(New_dict.items(), key=lambda item: item[1])}
print(sorted_dict)

print("-----------------------------")
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
new_dict = New_dict.copy()  # 使用 copy()
print(f"使用copy方法复制字典 {new_dict}")
another_dict = dict(New_dict)  # 使用字典构造函数
print(f"使用字典构造函数进行字典的复制 {another_dict}")

print(f"----------{datetime.datetime.now()}-------------")
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 22, "city": "Los Angeles"}
}
print(f"students的类型: {type(students)}获取嵌套字典students中Alice的年龄{students['Alice']['age']}")
print(f"----------{datetime.datetime.now()}-------------")
pairs =[("name","Alice"),("age",12)]
person = dict(pairs)
print(person)
print(">>>>>>>{datetime.datetime.now()}<<<<<<<<")
keys=["name","age","city"]
values =["Alice",12,"New York"]
preson = dict(zip(keys,values))
print(f"使用zip创建字典: {preson}")
print(">>>>>>>{datetime.datetime.now()}<<<<<<<<")
from collections import Counter
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 22, "city": "Los Angeles"},
    "Bob": {"age": 12, "city": "Shanghai"}
}
students_counts = Counter(students)
print(f"类型: {type(students)},计数: {students_counts}")
counts = Counter(["apple", "banana", "apple", "orange", "banana", "banana"])
print(f"类型: {type(counts)},计数: {counts}")

print(f">>>>>>>{datetime.datetime.now()}<<<<<<<<")
person1={"name":"Alice","age":12}
person2={"name":"Bob","age":13}
info = {"email":"alice@example.com","city":"New York"}
person1.update(info)
print(f"字典info合并到字典person1中，{person1}")
person2.update(info)
print(f"字典info合并到字典person2中，{person2}")
# result = person1.update(person2)
# result.update(info)
# print(f"字典info,person2合并到字典person1中，{result}")

print(f">>>>>>>{datetime.datetime.now()}<<<<<<<<")
person1={"name":"北京","age":1200}
person2={"name":"上海","age":1300}
merged_dict = {**person1, **person2}
print(merged_dict)
