# -*- coding: UTF-8 -*-
'''
@File           : demo1.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/8 10:13 AM 
@Author         : None
@Version        : None
@Desciption     : None
'''
"""Python条件控制示例"""
# 1，使用if语句
age = 18
if age >= 10:
    print("恭喜，可以去网吧了")

# 2，使用if和else
grade = 85
if grade >= 60:
    print("及格了")
else:
    print("不及格")

# 3，使用if-elif-else
score = 75
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
else:
    print("不及格")
# 4，使用条件表表达式
x, y = 10, 20
max_value = x if x > y else y
print("较大值是: ", max_value)

# 1,if嵌套
x = 15
if x > 10:
    print("x大于0")
    if x > 20:
        print("x大于20")
    else:
        print("x小于等于20")
else:
    print("x小于等于10")

# 2,条件表达式
result = "大于10" if x > 10 else "x小于10"
print(result)

# 3,逻辑运算
"""
and: and运算符在两个条件都为真时返回真
"""
x = 12
if x > 5 and x < 20:
    print("x大于5且小于20")
"""
or: or运算符在至少一个条件为真时返回真。
"""
x = 21
if x < 10 or x > 20:
    print("x小于10或大于20")
"""
not: not运算符用于取反一个条件的布尔值
"""
x = 8
if not x > 10:
    print("x不大于10")

# 组合条件
x = 18
y = 25
if x > 10 and y > 20:
    print("x大于10且y大于20")
elif x > 10 or y > 20:
    print("x大于10或y大于20")
else:
    print("x不大于10且y不大于20")


# 短路逻辑
def is_greater_than_5(x):
    print(f"检查{x}是否大于5")
    return x > 5


x = 3
y = 10
if is_greater_than_5(x) and is_greater_than_5(y):
    print("x和y都大于5")
else:
    print("x和y都不大于5")

# username = input("请输入名称")
# password = input("请输入密码")
# if username == "admin" and password == "123":
#     print("欢迎您")
# else:
#     print("输入账号或密码错误")


filename = "example.xt"
if filename.endswith(".txt"):
    print("这是一个.txt文本文件")
elif filename.endswith(".jpg"):
    print("这是一个.jpg结尾文件")
else:
    print("未知的文件结尾")


def operation_add(a, b):
    return a + b


def operation_subtract(a, b):
    return a - b


def operation_multiply(a, b):
    return a * b


def operation_divide(a, b):
    return a / b


operations = {
    'add': operation_add,
    'subtract': operation_subtract,
    'multiply': operation_multiply,
    'divide': operation_divide
}

operation = 'multiply'
a, b = 10, 5

result = operations[operation](a, b)
print(f"结果是: {result}")  # 输出：结果是: 50

x = 10
y = 20
max_value = (lambda a, b: a if a > b else b)(x, y)
print(f"最大值是:{max_value}")

# x = 10
# y = -5
# assert x > 0
# "x应该是正数"
# assert y > 0
# "y应该是正数"



a, b = 10, 0
try:
    result = a / b
except ZeroDivisionError:
    print("除数不能为0")
else:
    print(f"结果是{result}")