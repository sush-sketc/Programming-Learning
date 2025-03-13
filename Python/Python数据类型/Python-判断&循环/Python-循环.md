## Python 循环<a name="Python_if_002"> </a>

<a href="https://docs.python.org/3/tutorial/controlflow.html#for-statements">for Statements</a>

```plantuml
for-in      明确的知道循环执行的次数或者是要对一个容器进行迭代 
while       不知道据具体循环次数
range()     函数用法
```

for 循环用于遍历可迭代对象（例如列表、元组、字符串等），依次访问其中的每个元素，并执行特定的操作

### 1. `for-in` 循环

如果明确知道循环执行的次数，我们推荐使用for-in循环，例如上面说的那个重复3600次的场景，我们可以用下面的代码来实现。
注意，被for-in循环控制的代码块也是通过缩进的方式来构造，这一点跟分支结构中构造代码块的做法是一样的。我们被for-in循环控制的代码块称为循环体，
通常循环体中的语句会根据循环的设定被重复执行。

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

> <span style="color: #8968CD"> 示例1: 每隔一秒输出一次`Hello Python` 共输出5次</span>

```python
import time

for i in range(5):
    print("Hello Python")
    time.sleep(1)
```

#### 1.2. break and continue语句

在`for`循环中，可以使用`break`和`continue`语句来控制循环的执行流程

- `break`: &emsp;用于提前终止循环，即使迭代器中还有未遍历的元素
- `continue`: &emsp;用于跳过当前迭代，直接进入下一次循环

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print(fruit)
        break
    print(fruit)
```

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        continue  # 当遇到偶数是跳过当前迭代，进入下一次循环
    print(number)
```

#### 1.3. 示例练习

https://github.com/JalanJiang/python-100-practice/blob/master/day04/index.md

#### 1.4. 循环中常见的操作

无论是在 for 循环还是 while 循环中，都可以执行一系列常见操作，包括以下内容：

+ 遍历列表、元组、字符串等可迭代对象。
+ 使用 `range()` 函数生成一系列连续的数字进行循环。
+ 统计循环执行的次数。
+ 累积计算（例如计算总和）。
+ 从键盘或用户输入获取数据。
  下面是一些示例，演示了这些常见操作的使用：<br>

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 使用 range() 函数生成数字序列
for i in range(1, 6):  # 从 1 到 5
    print(i)

# 统计循环执行的次数
count = 0
for _ in range(10):
    count += 1
print("循环执行了", count, "次")

# 累积计算
total = 0
for number in range(1, 6):
    total += number
print("从1到5的和是:", total)

# 从用户输入获取数据
name = input("请输入您的名字: ")
print("您的名字是:", name)
```

#### 1.5. 多层for循环

多层for循环是指在一个for循环内嵌套另一个for循环的结构，它允许遍历多维数据结构，执行排列组合操作以及解决复杂的问题。应用场景如下：

+ 二维数组的遍历，例如遍历二维数组或矩阵
+ 排列组合问题：生成所有可能的组合

> <span style="color: #8968CD">  示例：二维列表的遍历 </span>

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for enumerate in row:
        print(enumerate)
```
> <span style="color: #8968CD"> 示例：多层for循环解决排列组合问题</span>

```python
colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]

for color in colors:
    for size in sizes:
        print(f"{color} {size}")
```
#### 1.6. 多层`for` 循环实际应用场景
> <span style="color: #8968CD"> 待完善 </span>

### 2. 使用 `range()`函数进行循环

`range()`函数生成一个整数序列，常用于控制for循环的次数。

```python
for i in range(5):  # 输出从0-4
    print(i)
```

> <span style="color: #8968CD" > 示例: 打印乘法口诀表 </span>

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()
```

>>  <span style="color: #FF6EB4"> 上面的代码中，`for-in`循环的循环体中又用到了`for-in`循环，外面的循环用来控制产生`i`行的输出，而里面的循环则用来控制在一行中输出`j`列。  
显然，里面的`for-in`循环的输出就是乘法口诀表中的一整行。所以在里面的循环完成时，我们用了一个`print()`来实现换行的效果，</span>
-----

### 3. for循环的高级用法
#### 3.1. `for` 迭代对象和可迭代性

+ 迭代对象是包含多个元素的数据结构，如列表，元组，字符串等。
+ 可迭代性是对象是否可以用于for循环的特性。
> <span style="color: #8968CD">示例：遍历列表，元组和字符串 </span>
```python
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)
my_tuple = ("apple", "banana", "cherry")
for num in my_tuple:
    print(num)
my_string = "Hello"
for num in my_string:
    print(num)
```
#### 3.2. 枚举索引和值
使用`enumerate`函数可以同时获取索引和对应的值
```python
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(f"Index: {index},Value: {value}")
```

#### 3.3. 同时遍历多个序列
  使用`zip`函数可以同时遍历多个序列

```python
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'purple']
for fruit, color in zip(fruits, colors):
    print(f"Fruit: {fruits},Color: {colors}")
```

### 4. while 循环

`while`循环用于在条件为真的情况下反复执行一段代码块，直到条件变为假为止。`while` 循环的基本语法如下：<br>

```plantuml
while: 条件:
  #执行循环体中的操作
```

> <span style="color: #8968CD"> 示例:  使用 while 循环计算从 1 到 5 的和</span>

```python
total = 0
number = 1
while number <= 5:
    total += number
number += 1
print("从1到5的和分别是：", total)
```

#### 4.1. break and continue
在 `while` 循环中，也可以使用 `break` 和 `continue` 语句来控制循环的执行流程，与 `for` 循环类似。 下面是一个示例，演示如何在 `while` 循环中使用这两个控制流语句
```python
number = 1
while number <= 5:
    if number == 3:
        break  # 当遇到 3 时，提前终止循环
    print(number)
    number += 1

number = 1
while number <= 5:
    if number == 3:
        continue  # 当遇到 3 时，跳过本次进入下次循环
    print(number)
    number += 1
```

> <span style="color: #8968CD"> 示例： 根据输入判断 </span>
```python
i = 1
while i <= 3:
    age = int(input('input: '))
    girl_age = 18
    if age == girl_age:
        print('猜对了')
        break
    else:
        print('猜错了')
    i += 1
else:
    print("对不起，我们不合适")
print('结束游戏')   
```

+ <strong>无限循环 </strong><br/>
使用`while True`可以创建无限循环，通常与`break`搭配使用

```python
count = 0
while True:
    print("This is an infinte loop", count)
    count += 1
    if count == 4:
        break
```

+ <strong>循环中的`else`语句</strong><br/>
`else`语句在循环正常结束是执行，但如果循环中有`break`被触发，则不执行

```python
count_bu = 0
while count_bu < 4:
    print("Inside the loop", count_bu)
    count_bu += 1
    # break 则后面语句不执行
else:
    print("Loop finished", count_bu)
```

### 5. 列表推导式

#### 5.1. 基本列表推导式
列表推导是一种紧凑而优雅的方式，用于在一行代码中创建新的列表。
> <span style="color: #8968CD"> 示例: 平方计算</span>
```python
squares_num1 = [x ** 2 for x in range(3)]
print(squares_num1)
```

#### 5.2. 带条件的列表推导式
添加条件语句，根据条件筛选元素

```python
enen_squaraes = [x ** 2 for x in range(5) if x % 2 == 0]
print(enen_squaraes)
```