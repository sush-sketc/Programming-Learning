# Python集合

在Python中，集合时一种无序的，可变的数据结构，用于存储唯一的元素，集合中不允许重复的元素，因此适用于存储不重复的数据，集合通常用于去重，成员检查和集合运算等场景
> [!TIP]
> [参考代码](./code/01.py) 

## 集合的定义

可以使用大括号`{}`或`set()`构造函数来定义一个集合。将元素用逗号`,`分隔开

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()
```

> [!NOTE]
> 在上述示例中，`fruits`集合包含了三个不重复的水果，`numbers`集合包含了无个不重复的数字，`empty_set`是一个空集合

## 集合的性质

集合中的元素时无序的，因此不能通过索引来访问，集合是可变的，可以添加或删除元素，集合中的元素必须是可哈希(hashable)
的，中意味这它们必须是不可变的，例如数字，字符串，元组等。

# 集合的常见操作

Python 集合支持多种常见操作，包括添加元素，删除元素，成员检查，集合运算，获取集合大小等

## 1. 添加元素

可以使用`add()`方法向集合中添加一个元素

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
```

<details>
<summary><font style="font-size: initial;color: bisque">ooutput</font> </summary>

```plantuml

```

</details>

## 2. 删除元素

可以使用`remove()`方法删除集合中的特定元素，如果元素不存在，会引发`KeyError`错误，另外，也可以使用`discard()`
方法删除元素，但如果元素不存在，不会引发错误

```python
fruits = {"apple", "banana", "cherry", "orange"}
fruits.remove("apple")
print(f"使用remove删除 {fruits}")
fruits.discard("cherry")
print(f"使用discard删除 {fruits}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
使用remove删除 {'orange', 'cherry', 'banana'}
使用discard删除 {'orange', 'banana'}
```

</details>

</br>

> [!TIP]
> 使用 remove() 时，需要确保元素存在于列表中，否则会抛出异常。
> 使用 discard() 时，不需要担心元素是否存在，因为它在元素不存在时不会抛出异常。
> remove() 适用于列表，而 discard() 适用于集合。

## 3. 成员检查

可以使用`in`运算符来检查元素是否存在于集合中

```python
fruits = {"apple", "banana", "cherry"}
contains_apple = "apple" in fruits
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
True
```

</details><br>

## 4. 获取集合大小

可以使用`len()`函数来获取集合中的元素数量

```python
fruits = {"apple", "banana", "cherry"}
print(len(fruits))
```

## 4. 集合运算

Python 集合支持一系列集合运算，包括并集，交集，差集，对称差集等
> [!NOTE]
> 并集（Union) 定义：并集是指两个集合中所有不重复的元素组成的集合
> 交集（Intersection）定义：交集是指两个集合中共有的元素组成的集合
> 差集（Difference）定义：差集是指在一个集合中存在但在另一个集合中不存在的元素组成的集合
> 对称差集（Symmetric Difference）定义：对称差集是指两个集合中不重复的元素组成的集合，即两个集合中各自独有的元素。
>> 并集：取两个集合中所有不重复的元素。
> > 交集：取两个集合中共有的元素。
> > 差集：取一个集合中存在但在另一个集合中不存在的元素，运算结果与顺序有关。
> > 对称差集：取两个集合中各自独有的元素。
> > 这些操作在处理数据时非常有用，特别是在需要去除重复元素、查找共同元素或比较两个集合的差异时

## 5. 并集

可以使用`union()`方法或`|`运算符来获取来获取两个集合的并集

```python
set1 = {1, 2, 4}
set2 = {3, 4, 7}
union_set = set1.union(set2)
print(union_set)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{1, 2, 3, 4, 7}
```

</details>

## 6. 交集

可以使用`difference()`方法或`-`运算符来获取两个集合的差集

```python
set1 = {1, 2, 3}
set2 = {6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```python
{3, 6}
```

</details>

## 7. 差集

可以使用`difference()`方法或`-`运算符来获取两个集合的差集

```python
set1 = {1, 2, 3, 4}
set2 = {1, 2, 0, 4}
print(set1.difference(set2))
print(set1 - set2)
```

## 8. 对称差集

可以使用`symmentric_difference()`方法或`^`运算符来获取两个集合的对称差集

```python
set1 = {1, 2, 3, 4}
set2 = {7, 6, 3, 5}
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{1, 2, 4, 5, 6, 7}
{1, 2, 4, 5, 6, 7}
```

</details>

## 9. 集合推导式

集合推导式是一种创建新集合的简介方法，通常基于现有的数据进行操作。

```python
numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}  # 创建一个包含数字平方的新集合
print(squared_numbers)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{1, 4, 9, 16, 25}
```

</details>

## 10. 冻结集合

Python 提供来`frozenset`类型，它是不可变的集合，一旦创建后就无法修改，冻结集合适用于需要确保数据不被修改的情况。

```python
frozen_set = frozenset({1, 2, 3, 4})
for value in frozen_set:
    print(f"value : {value},type : {type(frozen_set)}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
value : 1,type : <class 'frozenset'>
value : 2,type : <class 'frozenset'>
value : 3,type : <class 'frozenset'>
value : 4,type : <class 'frozenset'>
```

</details>

## 11. 集合的应用场景

集合在许多应用场景中国非常有用，一下是一些常见的应用场景：

- 去重： 用于去除列表或其他可迭代对象中的重复元素。
- 成员检查： 用于快速检查元素是否存在与集合中。
- 集合运算： 用于处理集合的并集，交集，差集等操作。
- 网络编程： 用于跟踪已连接的客户端，确保每个客户端只连接一次。

## 12. 总结

集合是一种强大的数据结构，用于存储不重复的元素，非常适用于去重、成员检查和集合运算等任务。希望这篇文章帮助大家更全面地了解
Python 集合，并能够在编程中灵活地应用它们。