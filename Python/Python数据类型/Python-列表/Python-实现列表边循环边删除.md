# Python中实现列表边循环边删除的详细指南

在Python中，有时需要在遍历列表的同时对其进行修改，即边循环边删除元素，这可能涉及到一些注意是想，以确保不会导致意外结果

## 1. 基本方法

最简单的方法是用过`for`循环和索引来遍历列表，并通过条件语句来删除元素，以下是一个基本示例

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % 2 == 0:
        del my_list[i]
print(my_list)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
[1, 3, 5, 7, 9]
```

</details>

> [!NOTE]
> 以上示例中，倒序遍历列表并删除偶数元素

## 2. 使用列表解析

列表解析是一种更简洁的方法，可以一行代码实现遍历和删除

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [x for x in my_list if x % 2 != 0]
print(my_list)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
[1, 3, 5, 7, 9]
```

</details>

> [!NOTE]
> 这种方法使用列表解析的筛选机制，保留满足条件的元素

## 3. 使用迭代器

利用迭代器和`itertools`模块，可以在遍历时安全地删除元素

```python
import itertools

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in itertools.chain(my_list):
    if i % 2 == 0:
        my_list.remove(i)
print(my_list)

str_list = ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
for i in itertools.chain(str_list):
    if i == "h":
        str_list.remove(i)
print(str_list)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
[1, 3, 5, 7, 9]
['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
```

</details>

## 4. 切片操作

使用切片操作也是一种避免问题的方式

```python
my_list = [1, 2, 3, 4, 45, 7, 6]
for i in my_list[::-1]:
    if i % 2 == 0:
        my_list.remove(i)
print(my_list)

str_list = ['h', 'e', 'l', 'l', 'o']
for i in str_list[::-1]:
    if i == 'l':
        str_list.remove(i)
print(str_list)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
[1, 3, 45, 7]
['h', 'e', 'o']
```

</details>

## 5. 使用`while`循环

另一种方法是使用`while`循环，不断地删除符合条件的元素知道列表为空

```python
mysql_list = [1, 2, 4, 5, 6, 7, 3, 8]
while mysql_list:
    if mysql_list[0] % 2 == 0:
        mysql_list.pop(0)
print(mysql_list)
str_list = ['h', 'e', 'l', 'l', 'o']
while mysql_list:
    if mysql_list[0] == 'e':
        mysql_list.pop(0)
print(str_list)
```

