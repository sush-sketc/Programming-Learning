## Python条件控制编程 <a name="Python_if_002"> </a>
<a href="https://docs.python.org/3/tutorial/controlflow.html#if-statements">if Statements </a>
### 1. 比较运算符
比较运算符用于比较两个值，并返回一个布尔值(True或flase),表示比较结果的真假，以下是常用的比较比较运算符
```plantuml
==  等于  [检查两个值是否相等]
!=  不等于 [检查两个值是否不相等]
<   大于 [检查一个值是否大于另一个值]
\>  小于 [检查一个值是否小于另一个值]
<=  小于等于 [检查一个值是否小于等于另一个值]
\>= 大于等于 [检查一个值是否大于等于另一个值]
```
### 2. 逻辑运算符
逻辑运算用于组合多个条件，以生成更复杂的条件表达式
```plantuml
and 逻辑与.返回 True 如果两个条件都为 True，否则返回 Flase
or 逻辑或,返回 True 如果至少一个条件为 True,否则返回 Flase
not 逻辑非,返回 True 如果条件为 Flase，否则返回 Flase
```
### 3. Python条件控制示例
```python
"""
Python条件控制示例
"""
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
```
### 4. 示例练习
> <span style="color: #8968CD; "> 示例2： 英制单位英寸和公制单位厘米互换</span>
```python
"""
1英寸(in) = 2.54厘米(cm)
输入: 长度 value 与 单位 unit
输出: 另外一类的长度与单位
"""
value = float(input("请输入长度:"))
unit = input("请输入单位：")

# 如果输入的是厘米
if unit == "cm" or unit == "厘米":
    output_value = value / 2.54
    print("%f 厘米 = %f 英寸" % (value, output_value))
# 如果输入的是英寸
elif unit == "in" or unit == "英寸":
    output_value = value * 2.54
    print("%f 英寸 = %f 厘米" % (value, output_value))
else:
    print("输入有效单位！")
```
>> <span style="color: #FF6EB4"> 上面代码需要注意的是，判断输入的单位有效性 </span>

> <span style="color: #8968CD"> 示例3: 掷骰子决定做什么</span>
```python
"""
掷骰子决定做什么事情
摇出1~6的数字，判断要做的事情
"""
from random import randint    #使用 random 模块的 randint 函数生成特定范围的随机数

# 产生 1～6的随机数
num = randint(1, 6)
if num == 1:
    res = '吃饭'
elif num == 2:
    res = '睡觉'
elif num == 3:
    res = '喵喵叫'
elif num == 4:
    res = '汪汪叫'
elif num == 5:
    res = '打豆豆'
elif num == 6:
    res = '写代码'
print(res)
```
> <span style="color: #8968CD"> 示例4: 扩展 `random`函数 </span>
```python
"""
random 常见函数
"""
import random
print( random.randint(1,100))       # 产生 1 ~ 100 的整数型随机数
print( random.random())             # 产生 0 ~ 1 之间的随机浮点数
print( random.uniform(1.1,5.4))     # 产生 1.1 ~ 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow'))   # 从序列中随机选取一个元素
print( random.randrange(1,100,2))   # 生成从1到100的间隔为2的随机整数

#将序列a中的元素顺序打乱
a =[1,3,5,6,7]
random.shuffle(a)
print(a)
```
> <span style="color: #8968CD"> 示例5: 结合以上重写掷骰子代码 </span>
```python
from random import  randint
d = {1:"吃饭",2:"睡觉",3:"喵喵叫",4:"汪汪叫",5:"打豆豆",6:"写代码"}
#产生 1-6 随机整数
num = randint(1,6)
print(d[num])
```
> <span style="color: #8968CD"> 示例6: 验证用户输入 </span>
```python
username = input("请输入名称")
password = input("请输入密码")
if username == "amdin" and password == "123":
    print("欢迎您")
else:
    print("输入账号或密码错误")
```
> <span style="color: #8968CD"> 示例7: 检查文件扩展名 </span>
```python
filename = "example.txt"
if filename.endswith(".txt"):
    print("这是一个.txt文本文件")
elif filename.endswith(".jpg"):
    print("这是一个.jpg结尾文件")
else:
    print("未知的文件结尾")
```
> <span style="color: #8968CD"> 示例8: 输入三条边长如果能构成三角形就计算周长和面积</span>
```python
"""
判断输入的编程能否构成三角形
如果能则计算出三角形的周长和面积
海伦公式: area = sprt(p(p-a)(p-b)(p-c))
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    arae = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("周长 = %.2f,面积 = %.2f" % (p, arae))
else:
    print("所输入的值无法形成三角形")
```

> <span style="color: #8968CD"> 示例9: 个人所得税计算 </span>
```python
"""
输入月收入和五险一金计算个人所得税
"""
salary = float(input('本月收入：'))
insurance = float(input('五险一金：'))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 3000:
    rate = 0.03
    deduction = 0
elif diff < 12000:
    rate = 0.1
    deduction = 210
elif diff < 25000:
    rate = 0.2
    deduction = 1410
elif diff > 35000:
    rate = 0.25
    deduction = 2660
elif diff > 55000:
    rate = 0.3
    deduction = 4410
elif diff > 80000:
    rate = 0.35
    deduction = 7160
else:
    rate = 0.45
    deduction = 15160
tax = abs(diff * rate - deduction)
print('个人所得税: ¥%.2f元' % tax)
print('实际到手收入: ¥%.2f元' % (diff + 5000 - tax))
```
---
### 5. if语句高级用法
在Python编程中，控制流语句是构建逻辑和执行流程的基础。if语句是控制流语句中最基本、最常用的语句之一。通过if语句，可以根据条件执行不同的代码块。
将详细介绍Python中if语句的高级用法，包括嵌套if、elif的使用、条件表达式、逻辑运算符、组合条件、短路逻辑等，并提供具体的示例代码，帮助全面掌握if语句的高级用法。 

#### 5.1 嵌套`if`
可以在一个`if`或`else`中嵌套另一个`if`语句
```python
x = 15
if x > 10:
    print("x大于0")
    if x > 20:
        print("x大于20")
    else:
        print("x小于等于20")
else:
    print("x小于等于10")
```

#### 5.2 条件表达式 
条件表达式 （也称为三元运算符）是一种简洁的if-else语句形式，用于根据条件选择值 语法:<br>
`value_if_true if condition else value_if_false`
```python
result = "大于10" if x > 10 else "x小于10"
print(result)
```

#### 5.3 逻辑运算符
逻辑运算符用于组合多个条件，创建更复杂的逻辑表达式。
```python
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
```
#### 5.4 组合条件
通过组合条件，可以处理更复杂的逻辑
```python
x = 18
y = 25
if x > 10 and y > 20:
    print("x大于10且y大于20")
elif x > 10 or y > 20:
    print("x大于10或y大于20")
else:
    print("x不大于10且y不大于20")
```

#### 5.5 短路逻辑
`Python` 中的逻辑运算符具有短路特性，即第一个条件已经决定了表达式的结果，则不再计算第二个条件
```python
def is_greater_than_5(x):
    print(f"检查{x}是否大于5")
    return x > 5


x = 3
y = 10
if is_greater_than_5(x) and is_greater_than_5(y):
    print("x和y都大于5")
else:
    print("x和y都不大于5")
```

#### 5.6 复杂条件判断
在处理复杂条件时，使用括号来表达明确的条件优先级
```python
x = 12
y = 7
z = 10
if (x > 10 and y < 10) or z == 10:
    print("条件满足")
else:
    print("条件不满足")
```
----


### 6. 深入探索`if-elif-else`的高级用法
#### 6.1 条件表达式(三元运算)
条件表达式，也称为三元运算符，是一种简洁的条件判断方法。它的语法如下：<br>
`value = true_value if condition else false_value`
```python
x = 5
y = 10
max_value = x if x > y else y
print(f"最大值是:{max_value}")
```
>> 根据x和y的值，max_value会被赋值为较大者。

#### 6.2 利用字典实现条件判断
使用字典来代替if-elif-else语句可以使代码更加简洁和高效。特别是在需要处理大量条件时，这种方法尤为有用
```python
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
```
>> 使用字典将操作字符串映射到相应的函数，从而避免了大量的if-elif-else语句

#### 6.3 使用lambda表达式
```python
x = 10
y = 20
max_value = (lambda a,b: a if a> b else b)(x,y)
print(f"最大值是:{max_value}")
```
#### 6.4 使用`any`和`all`
在进行多个条件判断时，可以使用内置函数any和all
  + `any`:&emsp;只要有一个条件为真返回`True`
  + `all`:&emsp;所有条件都为真，返回`True`

```python
x, y, z = 10, 0, -5
# 检查是否有任意一个正数
if any(x > 0, y > 0, z > 0):
    print("至少有一个是正数")
else:
    print("没有正数")
# 检查是否所有都是正数
if all(x > 0, y > 0, z > 0):
    print("所有都是正数")
else:
    print("并非所有都是正数")
```
#### 6.5 条件断言
断言`assert`是一种用于调试的工具，它在条件为假时引发异常。可以使用断言在开发过程中验证程序的正确性。
```python
x = 10
y = -5
assert x > 0
"x应该是正数"
assert y > 0
"y应该是正数"
```
>> 会引发异常因为y不是正数

#### 6.6 结合`try-except`处理异常
```python
a, b = 10, 0
try:
    result = a / b
except ZeroDivisionError:
    print("除数不能为0")
else:
    print(f"结果是{result}")
```

