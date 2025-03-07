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

> **output**

```puml
[1, 4, 5, 9, 12, 21]
['The', 'happy', 'is', 'python']
```

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

> **output**

```puml
['apple', 'banana', 'grage', 'orange']
[0, 1, 21, 43, 43, 54]
```

## 2. 高级排序方法

### 2.1. 自定义排序规则

> [!NOTE]
> 可以使用`key`参数来指定排序时的自定义规则，例如，按字符串长度进行操作

```python
words = ['python', 'is', 'awesome', 'language']
sorted_words = sorted(words, key=len)
print(sorted_words)
```

> **output**

```puml
['is', 'python', 'awesome', 'language']
```

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

> **output**

```puml
['python', 'language', 'is', 'awesome']
[99, 88, 42, 32, 4, 3, 0]
```

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

> **output**

```puml
[('Charlie', 30), ('Bob', 20), ('Alice', 12)]
```

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

- [x] sourt() #739
- [ ] https://github.com/octo-org/octo-repo/issues/740

### Add delight to the experience when all tasks are complete :tada:

### @octocat :+1: This PR looks great - it's ready to merge! :grinning:

- [x] This is a completed task.
- [ ] This is an incomplete task.

<details open>

<summary>Tips for collapsed sections</summary>

### You can add a header

You can add text within a collapsed section.

You can add an image or a code block, too.

```ruby
   puts "Hello World"
```

</details>