## Python 列表排序: 从基础到高级

## 1.基础排序

> [!TIP]
> [示例代码](./code/code-04.py)

### 1.1. 使用`sorted()`函数

> [!NOTE]
> Python 提供了内置的`sorted()`函数，用于对可迭代对象进行排序，该函数返回一个新的已排序列表，不会修改原始列表。

```python
# 按照字母排序
str_string = ["The", "is", "python", "happy"]
# 按照数字排序
int_sorted = [4, 9, 12, 5, 21, 1]
sorted_list = sorted(str_string)
int_sorted_list = sorted(int_sorted)
print(int_sorted_list)
print(sorted_list)
```

<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
[1, 4, 5, 9, 12, 21]
['The', 'happy', 'is', 'python']
```

</details>

### 1.2. 使用`sort()`方法

> [!NOTE]
> 列表对象本身也提供了`sort()`方法，可以直接直接对列表进行排序 与`sorted()`不同，`sort()`会直接修改原始列表

```python
fruits = ['apple', 'orange', 'banana', 'grage']
int_sorted = [43, 1, 0, 54, 21, 43]
fruits.sort()
int_sorted.sort()
print(f"{fruits}\n{int_sorted}")
```

<datalist>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```puml
['apple', 'banana', 'grage', 'orange']
[0, 1, 21, 43, 43, 54]
```

</datalist>

## 2. 高级排序方法

### 2.1. 自定义排序规则

> [!NOTE]
> 可以使用`key`参数来指定排序时的自定义规则，例如，按字符串长度进行操作

```python
words = ['python', 'is', 'awesome', 'language']
sorted_words = sorted(words, key=len)
print(sorted_words)
```

<datalist>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>
```puml
['is', 'python', 'awesome', 'language']
```
</datalist>

### 2.2. 逆序排序

> [!NOTE]
> 通过`reverse`参数，可以轻松实现逆序排序

```python
# 字符串逆序排序
words = ['python', 'is', 'awesome', 'language']
# 数字逆序排序
int_reversed = [3, 4, 42, 32, 0, 88, 99]
sorted_desc = sorted(words, reverse=True)
sorted_int = sorted(int_reversed, reverse=True)
print(f"{sorted_desc}\n{sorted_int}")
```

<details>
<summary><font style="font-size: larger;color: bisque"> output </font> </summary>

```plantuml
['python', 'language', 'is', 'awesome']
[99, 88, 42, 32, 4, 3, 0]
```

</details>

### 2.3. 利用`Lambda`表达式定制排序

> [!NOTE]
> 使用`key`参数时，还可以结合`Lambda`表达式定义更复杂的排序规则

```python
"""
利用Lambda表达式定制排序
"""
students = [('Alice', 12), ('Bob', 20), ('Charlie', 30)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
```

<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
[('Charlie', 30), ('Bob', 20), ('Alice', 12)]
```

</details>

### 2.4. 稳定排序与不稳定排序

> [!NOTE]
> 在`Python`中，排序算法是稳定的，即对于具有相同排序键的元素，它们在排序后的相对位置保持不变

```python
pairs = [(91, 2), (0, 43), (32, 13), (4, 343)]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)
```

<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```puml
[(0, 43), (4, 343), (32, 13), (91, 2)]
```

</details>

## 3 Python列表排序（深入探讨sort()和sorted()）

> [!NOTE]
> 在Python中，列表排序是一项常见而重要的一下案例解释了`sort()`方法和`sorted()`函数，高效的利用这两种方式进行列表的排序

### `sort()` 方法的基本用法

`sort()`方法默认按照升序排序，同时也支持降序排序
`sort()`方法是列表对象的一个内置方法，能够直接的对原始列表进行排序，一下是一个简单的示例

```python
numbers = [4, 6, 1, 0, 7, 4]
numbers.sort()
print(numbers)
```

<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```puml
[0, 1, 4, 4, 6, 7]
```

</details>

```python
numbers = [4, 0, 23, 65, 1, 43, 78]
numbers.sort(reverse=True)
print(numbers)
```

<details>
<summary> <font style="color: bisque;font-size: larger"> output  </font></summary>

```plantuml
[78, 65, 43, 23, 4, 1, 0]
```

</details>

## 4. `sort()`方法的高级用法

### 4.1 自定义排序关键字

`sourt()`方法允许通过关键子参数`key`指定一个自定义的排序函数，以下是一个按字符串长度排序的示例

```python
words = ["apple", "banana", "orange", "kiwi"]
# 从下标为1的元素开始排序
words.sort(key=lambda x: x[1])
print(words)
# 从下标为2的元素排序，
words.sort(key=lambda x: x[2])
print(words)
# 从末尾元素进行排序
words.sort(key=lambda x: x[-1])
print(words)
```

<details >
<summary> <font style="color: bisque;font-size: larger"> output  </font></summary>

```
['banana', 'kiwi', 'apple', 'orange']
['orange', 'banana', 'apple', 'kiwi']
['banana', 'orange', 'apple', 'kiwi']
```

</details>

### 4.2. 使用`lambda`函数
通过`lambda`函数可以更灵活地低音排序规则，例如按单词的最后一个字母进行排序
```python
words = ["apple","banana","orange","kiwi"]
words.sort(key=lambda x: x[-1])
print(words)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
['banana', 'apple', 'orange', 'kiwi']
```
</details>

## 5. `sorted()`函数基本用法
与`sort()`方法不同`sorted()`函数不会修改原始列表，而是返回一个新的排序列表，以下是`sorted()`函数基本示例
```python
numbers =[4,6,3,1,99,23,45,27]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
[1, 3, 4, 6, 23, 27, 45, 99]
[4, 6, 3, 1, 99, 23, 45, 27]
```
</details>

## 6.`sorted()`高级用法
### 6.1 反向排序
与`sort()`方法类似,`sorted()`方法也支持`reverse`参数，用于进行降序排序
```python
numbers = [1,34,6,87,3,0,9]
sorted_number_desc = sorted(numbers,reverse=True)
print(sorted_number_desc)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
[87, 34, 9, 6, 3, 1, 0]
```
</details>

### 6.2. 自定义排序
利用`key`参数，可以实现与`sort()`方法相似的自定义排序
```python
words =["apple","banana","orange","kiwi"]
sorted_words = sorted(words,key=len)
print(sorted_words)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
['kiwi', 'apple', 'banana', 'orange']
```
</details>

## 7. 使用`operato`模块
`operato`模块提供了一些方便的函数，可用于更负载的排序操作，例如，按元组的第二个元素进行排序
```python
import operator
data = [(1,5),(3,2),(7,8),(4,1)]
sourted_data =[sorted(data,key=operator.itemgetter(1))]
print(sourted_data)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
[[(4, 1), (3, 2), (1, 5), (7, 8)]]
```
</details>

## 8. 新比较和选择
新能比较在选择使用`sort()`方法还是`sorted()`函数时至关重要，尤其在不同场景中
### 8.1. `sort()`方法性能
`sort()`方法时一个原地排序方法，直接修改原始列表，因此在内存使用方面更为高效，它采用`Timsort`算法，结合了归并排序和插入排序的优点，对于大型数据集`sort()`方法
通常表现得更出色，这是因为它避免了创建新的数据结构，直接在原有列表上进行排序，节省了额外的内存开销。
### 8.2. `sorted()`函数的性能
`sorted()`函数创建一个新的已排序列表，不修改原始列表，因此在某些情况下更安全，但是，由于它需要额外的内存来存储新的列表，对于大型数据集可能会引起哪次开销较大的问题，特别时当
原始数据集很大时，`sorted()`可能不如`sort()`方法效率高
