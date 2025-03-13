## Python 列表基础
在Python中，列表是一种有序的，可变的数据结构。用于存储多个值，列表可以包含各种类型的元素，包括数字，字符串，其他列表等，列表是非常灵活和常用的
### 1. 列表的定义
可以使用方括号`[]`来定义一个列表，将多个元素用逗号`,`分隔开。
> <span style="color: #8968CD">示例：</span>
```python
fruits = ["apple","banana","cherry"]
numbers = [1,2,3,4]
mixed_list = [1,"apple",3.14,True]
empty_list = []
```

### 2. 列表的索引与切片
列表中的元素是有序的，并且可以通过索引来访问，列表的索引从0开始，可以使用方括号`[]`和索引来获取元素，此外还可以使用切片来获取列表的子集
```python
fruits = ["apple", "banana", "bcherry"]
print(f"获取列表fruits的第一个元素: {fruits[0]} 索引为0")
print(f"获取列表fruits的第二个元素: {fruits[1]} 索引为1")
print(f"获取列表fruits的第三个元素: {fruits[2]} 索引为2")

# output
# 获取列表fruits的第一个元素: apple 索引为0
# 获取列表fruits的第二个元素: banana 索引为1
# 获取列表fruits的第三个元素: bcherry 索引为2
```
### 3. 创建列表的技巧
#### 3.1 直接创建
最简单的创建列表的方法是直接使用方括号`[]`将元素包围起来
```python
#创建一个包含多个元素的列表
my_list =[1,2,3,4]
print(my_list)

#创建一个空列表
empty_list = []
print(empty_list)

# output
# [1, 2, 3, 4, 5]
# []
```
#### 3.2. 使用`list()`函数创建
`list()`函数可以将其他数据类型转换为列表
```python
str_list = list("hello")
print(str_list)

#使用list()函数将元组转换为列表
tuple_list = list((1,2,3))
print(tuple_list)

# output
# ['h', 'e', 'l', 'l', 'o']
# [1, 2, 3]
```
#### 3.3. 列表推导式
+ 基本列表推导式
```python
#使用列表推导式创建一个包含0到9的列表
squares = [x**2 for x in range(10)]
print(squares)

# output
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
+ 带条件的列表推导式
```python
#创建一个包含0到9中所有偶数的列表
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# output
# [0, 2, 4, 6, 8]
```
+ 嵌套列表推导式
```python
# 创建一个嵌套列表，每个子列表包含0到2的平方
nesten_list = [[x ** 2 for x in range(3)]for _ in range(3)]
print(nesten_list)

# output
# [[0, 1, 4], [0, 1, 4], [0, 1, 4]]
```
#### 3.4. 使用内置函数创建列表
+ 使用`range()`函数创建
`range()`函数生成一个整数序列，常用于创建数字列表
```python
# 使用range()函数创建一个包含0到9的列表
range_list = list(range(10))
print(range_list)

# output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
+ 使用`map()`函数创建
`map()`函数将一个函数应用到所有列表元素上，生成一个新的列表
```python
# 使用map()函数将字符串列表转换为大写
words = ["hello","world"]
upper_words = list(map(str.upper,words))
print(upper_words)

# output
# ['HELLO', 'WORLD']
```

### 4. 高级列表创建技巧
+ 使用`itertools`模块创建,`itertools`模块提供了生成器函数，用于高效的创建和操作列表
```python
import  itertools
# 使用itertools.cycle()创建一个无限循环的列表生成器
cycle_gen = itertools.cycle([1,2,3])
for _ in range(12):
    print(next(cycle_gen),end=' ')
print()

# output
# 1 2 3 1 2 3 1 2 3 1 2 3

# 使用itertools.repeat()创建一个重复元素的列表生成器
print(f"重复元素的列表: {list(itertools.repeat(5,4))}")

# output
# 重复元素的列表: [5, 5, 5, 5]
```
+ 使用生成器表达式创建
生成表达式类似与列表推导式，但返回的是一个生成器对象，可以节省内存
```python
# 创建一个生成器表达式
gen_exp = (x**2 for x in range(10))
print(list(gen_exp))

# output
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
+ 创建为列表
二维列表可以看作列表的列表，用于存储矩阵或表格数据
```python
# 创建一个3x3的二维列表
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)

# output
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 5. 列表操作和常用技巧
+ 5.1. 列表元素访问与修改
可以通过索引访问和修改列表元素
```python
my_list = [1,2,3,4,5]
print(f"获取下标为0的元素: {my_list[0]}")

# 修改列表元素
my_list[0] = 10
print(f"修改下标索引为0的元素内容为10, value: {my_list[0]}")

# output
# 获取下标为0的元素: 1
# 修改下标索引为0的元素内容为10, value: 10
```
+ 5.2. 列表切片
列表切片用于获取子列表
```python
my_list = [1,2,3,4,5]
print(my_list[1:4])

#切片赋值
my_list[1:4] = [90,54,76]
print(my_list)

# output
# [2, 3, 4]
# [1, 90, 54, 76, 5]
```
+ 5.3. 列表合并与复制
可以使用`+`运算符合并列表,使用`*`运算符复制列表。
```python
list1 = [1,2,3]
list2 = [4,5,6]

#合并列表
# merged_list = list+list2
print(f"合并两个列表: {list1+list2}")
#复制列表
print(f"list1复制一份: {list1 *2}")

# output
# 合并两个列表: [1, 2, 3, 4, 5, 6]
# list1复制一份: [1, 2, 3, 1, 2, 3]
```

+ 5.4. 列表推导式的常见应用
列表推导式不仅用于创建列表，还可以用于转换和过滤列表
> <span style="color: #8968CD">示例: 过滤和转换</span>
```python
# 过滤掉负数并将剩余元素平方
number = [-2,-1,0,1,2]
print(f"{[x**2 for x in number if x >=0]}")  

# output
# [0, 1, 4]
```

> <span style="color: #8968CD">示例: 嵌套列表展开</span>
```python
# 将嵌套列表展开为一维列表
nested_list = [[1,2,3],[4,5],[6,7,8,9]]
print(f"{[item for sublist in nested_list for item in sublist]}")

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### 6. 处理大数据的技巧
在处理大数据时生成器表达式和`itertools`模块非常好用
> <span style="color: #8968CD">示例: 使用生成器处理大数据</span>
```python
# 创建一个大数据生成器
largn_gen = (x for x in range(100000))

#逐个处理数据
for x in largn_gen:
    if x % 100000:
        print(x)
```

> <span style="color: #8968CD">示例: 使用`itertools`处理大数据</span>
```python
import itertools

# 创建一个大数据生成器并进行切片
large_gen = ( x for x in range(100000))
sliced_gen = itertools.islice(large_gen,1000,1010)
print(list(sliced_gen))

# output
# [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
```