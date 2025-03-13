# Python字典操作指南，掌握编程中必备的数据结构

字典`(Dictionary)`是Python中一种非常重要和常用的数据结构，它用于存储键-值对的数据，在Python中，字典是可变`(Mutable)`
的，无序`(Unordered)`的，可哈希`(Hshable)`的数据结构
可以通过关键子来访问值。

---
> [!TIP]
> [示例代码](code/code-05.py)

## 1. 字典的创建和基本基本操作

创建字典以及进行基本的操作

## 2. 创建字典

在Pythonzhong ，可以使用大括号`{}`来创建一个字典，或这使用`dict()`构造函数。以下为一个示例:

```python
# 使用大括号创建字典
my_dict = {"name": "Alice", "age": 23, "city": "New york"}
# 使用dict()函数来创建字典
another_dict = dict(name="Bob", age=23, city="San Francisco")
```

## 3. 访问字典的值

可以通过键来访问字典中的值，使用方括号`[]`看来获取键对应的值，或者使用`get()`方法。

```python
my_dict = {"name": "Alice", "age": 23, "city": "New york"}
# 使用方括号获取值
name = my_dict["name"]
age = my_dict["age"]
# 使用get()方法获取值
city = my_dict.get("city")
```

## 4. 添加和修改字典的元素

可以通过指定键来添加或修改字典中的元素，如果键已经存在，将会更新对应的值，如果键不存在，将会创建新的键值对。示例如下：

```python
my_dict = {"name": "Alice", "age": 23, "city": "New york"}
# 添加新的键值对
my_dict["email"] = "alice@example.com"

# 修改已有键的值
my_dict["age"] = 21
```

## 5. 删除字典的元素

可以使用该`del`语句来删除字典中的元素，可以使用`pop()`方法删除指定键的元素。示例如下

```python
my_dict = {"name": "Alice", "age": 23, "city": "New york"}
# 使用del语句删除元素
del my_dict["age"]
# 使用pop()方法删除元素
my_dict.pop("city")
```

## 6. 字典的遍历

字典中的元素是无序的，但可以通过不同的方式进行比那里，以下是一些常见的遍历方法

- 遍历键
  可以使用`keys()`方法获取字典中的所有键，并进行遍历。示例如下：

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for k in my_dict.keys():
    print(f"key=[{k}]")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
key=[name]
key=[age]
key=[email]
key=[city]
```

</details>

- 遍历值
  可以使用`values()`方法获取字典中的所有值，并进行遍历，示例如下:

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for value in my_dict.values():
    print(f"value{value}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font></summary>

```plantuml
valueAlice
value23
valueAlice@example.com
valueNew York
```

</details>

## 7. 遍历键值对

可以使用`items()`方法获取字典中的所有键值对，并进行遍历，示例如下:

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
for key, value in my_dict.items():
    print(f"key[{key}],value{value}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font></summary>

```plantuml
key:[name],value:Alice
key:[age],value:23
key:[email],value:Alice@example.com
key:[city],value:New York
```

</details>

## 8. 字典的常见操作

处理基本的创建，访问和遍历操作，字典还支持许多其他的常见操作，例如判断键是否存在，获取字典长度等

### 8.1. 判断键是否存在

可以使用`in`关键字来判断键是否存在与字典中，示例如下：

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
if "name" in my_dict:
    print("Name is in the dictionary.")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font>

```plantuml
Name is in the dictionary.
```

</summary>
</details>

### 8.2. 获取字典的长度

可以使用`len()`函数获取字典中的键值对的数量，示例如下：

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
print(f"The dictionary contains {len(my_dict)} key-value pairs.")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
The dictionary contains 4 key-value pairs.
```

</details>

### 8.3. 清空字典

可以使用`clear()`方法清空字典中的所有键值对
``
my_dict.clear()
``

### 8.4. 字典的嵌套

字典中的值可以是任何数据类型，包括另一个字典，这种嵌套字典的方式可以创建复杂的数据结构。示例:

```python
person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
```

通过嵌套字典，可以更好的组织和表示复杂的数据关系。

### 8.5. 字典的默认值

有时候需要访问字典总不存在的键时，不抛出KeyError异常，而是返回一个默认值，可以使用`get()`方法来实现这一点。示例:

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
value = my_dict.get("nonexistent_key", "default_value")
```

> [!WARNINGal
> 如果字典中不存在键`nonexistent_key`,则上述代码将返回`default_value`.

### 8.6. 字典推导式

类似于列表推导式，Python还支持字典推导式，用于创建字典。示例如下：

```python
numbers = [1, 2, 3, 4]
square_dict = {num: numbers ** 2 for num in numbers}
```

上述代码将创建一个包含数字和它们的平方的字典

## 9. 字典的排序

字典本身是无序的，但可以根据键或值对字典进行排序，

- 按键排序
  可以使用`sorted()`函数按照键对字典进行排序

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print(sorted_dict)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'age': 23, 'city': 'New York', 'email': 'Alice@example.com', 'name': 'Alice'}
```

</details>

- 按值排序
  可以使用`sirted()`函数和自定义的排序函数来按值对字典进行排序

```python
my_dict = {"name": "Alice", "age": 23, "email": "Alice@example.com", "city": "New York"}
sorted_dict = {key: value for key, value in sorted(my_dict.items(), key ==
lambda itme: itme[1])}
print(sorted_dict)
```