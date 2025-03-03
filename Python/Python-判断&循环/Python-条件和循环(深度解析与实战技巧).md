## Python 条件和循环: 深度解析与实战技巧 <a name="Python_if_003"></a>

### 1. `for`循环

`for`循环用于遍历可迭代对象(如列表，字符串，字典，集合等)，逐个访问其元素并执行代码块

+ <span style="color: #8968CD"> **遍历列表**</span>

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

+  <span style="color: #8968CD"> **遍历字符串**</span>

```python
# 遍历字符串中的每个字符
text = "Hello"
for char in text:
    print(char)
```

+ <span style="color: #8968CD"> **遍历字典**</span>

```python
# 遍历字典的键和值
student_scores = {"alice": 85, "Bob": 90, "Charlie": 78}
for student, score in student_scores.items():
    print(f"{student}:{score}")
```

> > <span style="color: #FF6EB4"> 函数`items()` 返回包含字典的键值对，作为列表中的元组 </span>

+  <span style="color: #8968CD"> **使用`range`函数** </span><br>

<span style="color: #A52A2A">**range**</span> 函数生成一系列数字，用于<span style="color: #A52A2A">**for**</span>循环

```python
# 使用range生成0到9的数字
for i in range(10):
    print(i)
```

### 2. **`while`** 循环

<span style="color: #A52A2A">**while**</span>循环在条件为真时反复执行代码块，直到条件为假

+ <span style="color: #8968CD"> **基本用法**</span>

```python
# 使用while循环打印0到4
count = 0
while count < 5:
    print(count)
    count += 1
```

+ <span style="color: #8968CD"> **用户输入**</span>

```python
# 反复提示用户输入一个正数
while True:
    number = int(input("请输入一个正数: "))
    if number > 0:
        break
    print("输入无效，请重试。")
print(f"你输入的正数是: {number}")
```

### 3. 循环控制语句

+ **`break`**

<span style="color: #A52A2A">break</span>关键字用于提前终止循环

```python
# 遇到数字3时终止循环
for number in range(10):
    if number == 3:
        break
    print(number)
```

+ **`continue`** 语句
  <span style="color: #A52A2A">continue</span>关键字用于跳过当前迭代，直接进入下一次迭代

```python
# 跳过偶数
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
```

+ **`else`** 子句
  <span style="color: #A52A2A">else</span>子句可与<span style="color: #A52A2A">for</span>或<span style="color: #A52A2A">
  while</span>循环一起使用，当循环正常结束(没有被<span style="color: #A52A2A">break</span>终止)时执行。

```python
# 检查一个数字是否为素数
number = 29
for i in range(2, number):
    if number % i == 0:
        print(f"{number}不是素数")
        break
else:
    print(f"{number}是素数")
```

### 4. 高级用法

+ 4.1. **使用<span style="color: #A52A2A">enumerate</span>函数**<br>
  `enumerate`函数用于在循环中获取索引和值。

```python
# 使用enumerate获取索引和值
words = ["apple", "banana", "cherry"]
for index, word in enumerate(words):
    print(f"index: {index},value: {word}")
```

+ 4.2. **使用<span style="color: #A52A2A">zip</span>函数**<br>
  <span style="color: #A52A2A">zip</span> 函数用于并行迭代多个可迭代对象

```python
names = ["Alice", "Bob", "Charlie"]
scores = [83, 45, 67]
for name, score in zip(names, scores):
    print(f"name: {name},scores: {scores}")
```

+ 4.3. **<span style="color: #A52A2A">列表推导式</span>**<br>
  列表推导式是一种简洁的创建列表的方式，通常结合`for`循环使用

```python
# 创建一个包含0到9的平方的列表
squares = [x ** 2 for x in range(10)]
print(squares)
```

+ 4.4. **<span style="color: #A52A2A">字典推导式</span>**<br>
  类似于列表推导式，字典推导式用于创建字典。

```python
# 创建一个字典，其中键为0到9，值为其平方
square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)
```

+ 4.5. **<span style="color: #A52A2A">集合推导式</span>**<br>
  集合推导式用于创建集合

```python
# 创建一个集合，其中包含0到9的平方
square_set = {x ** 2 for x in range(10)}
print(square_set)
```

+ 4.6. **<span style="color: #A52A2A">嵌套循环</span>**<br>
  嵌套循环是指一个循环内部包含另一个循环。

```python
# 打印乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()
```

+ 4.7. **<span style="color: #A52A2A">使用itertools模块</span>**<br>
  `itertools`模块提供了许多用于迭代的函数，支持复杂的循环操作。

```python
import itertools

# 生成笛卡尔积
for item in itertools.product('AB', range(3)):
    print(item)
```

### 5. <span style="color: blueviolet">zip和enumerate函数<br></span>

+ 语法:

```plantuml
zip(*iterables)
enumerate(iterable,start=0) 
```

+ 参数如下:

`iterables` &emsp; 一个或多个可迭代对象，如列表，元组，字符串等
`iterable` &emsp; 一个可迭代对象，如列表，元组，字符串等
`start` (可选) 下标起始位置的值，默认为0

+ 返回值

`zip`: 返回一个迭代器，每个元素都是一个元组，由输入的可迭代对象在相同位置上的元素组成。使用时需要注意`zip`
函数会以最短的可迭代对象的长度为准进行合并
`enumerate`: 返回一个迭代器，每个元素都是一个包含索引和对应元素的元组

> <span style="color: #8968CD" > 示例如下 </span>

```python
# 字符串
strings = "hello"
# 数组
arr = [1, 2, 3, 4, 5, 6]
# 元组
fruits = ("apple", "banana", "cherry")
# 字典
person = {"name": "Alice", "age": 25, "city": "Shanghai"}
```

> <span style="color: #8968CD" >zip方式</span>

```python
for i in zip(strings, arr, fruits, person.values()):
    print(i)
```

**output**

```plantuml
('h', 1, 'apple', 'Alice')
('e', 2, 'banana', 25)
('l', 3, 'cherry', 'Shanghai')
```

> > 可以看到`zip`吧string拆分开了，并以`fruits`和`preson`为最短的结尾，多了的就舍弃了

<span style="color: #8968CD" >enumerate方式</span>

```python
for i in enumerate(fruits, 0):  # 下标从0开始
    print(i)
```

**output**

```plantuml
(0, 'apple')
(1, 'banana')
(2, 'cherry')
```

<span style="color: #8968CD" >结合使用 zip 和 enumerates</span>

```python
for index, value in enumerate(zip(strings, arr, fruits, person.values())):
    print(f"index: {index},value: {value}")
```

**ouput**

```plantuml
index: 0,value: ('h', 1, 'apple', 'Alice')
index: 1,value: ('e', 2, 'banana', 25)
index: 2,value: ('l', 3, 'cherry', 'Shanghai')
```

### 6. 实际应用示例

#### 6.1. 读取文件内容

使用`for`循环逐行读取文件内容

```python
# 读取文件内容并打印每行
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

#### 6.2. 计算阶乘

使用`wile`循环计算一个数的阶乘

```python
# 计算5的阶乘
number = 5
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"5的阶乘是: {factorial}")
```

#### 6.3. 寻找最大公约数
使用`wile`循环实现欧几里得算法，寻找两个数的最大公约数
```python
# 计算两个数的最大公约数
a, b = 48, 18
while b:
    a, b = b, a % b
print(f"最大公约数是: {a}")
```

### 7. Python程序结构控制解鸡兔同笼问题
+ **问题描述**
假设在一个笼子中有若干只鸡和兔子，它们的脚加起来一共有n只，而头的数量加起来一共有m只，编写一个python程序，根据给定的头和脚的数量，计算出鸡和兔子的数量
+ **解决**
在解决这个问题的过程中，将学习如何使用Python的程序控制结构，包括条件语句和循环语句。首先，可以使用条件语句判断脚和头的数量是否合理，然后通过循环语句尝试不同的组合，找到符合条件的解。
+ **代码**
```python
def solve_chichen_rabbit_problem(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            return chickens, rabbits
    return None, None


# 输入头和脚的数量
heads_input = int(input('Enter the number of heads: '))
legs_input = int(input('Enter the number of legs: '))

# 解决问题并输出结果

result_chichens, result_rabbits = solve_chichen_rabbit_problem(heads_input, legs_input)
if result_chichens is not None:
    print(f"Number of chichens: {result_chichens}")
    print(f"Number of rebbits: {result_rabbits}")
else:
    print("No solut found.")
```