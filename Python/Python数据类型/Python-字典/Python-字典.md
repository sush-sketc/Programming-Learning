## Python 字典
在Python中，字典是一种无序的,可变的数据结构,用于存储键值对`(key-value pairs)`,字典中的每个键都与一个值相关联，键和值之间用冒号`:`分隔，键值对之间用逗号`,`分隔
整个字典用花括号`{}`包围，字典提供了一种快速查找和检索值的方式，通常用于表示映射关系。
字典（Dictionary）是Python中一种非常重要和常用的数据结构，它用于存储键-值对的数据。在Python中，字典是可变（Mutable）的、无序（Unordered）的、可哈希（Hashable）的数据结构，可以通过键来访问值。

### 1. 字典创建和基本操作
#### 1.1. 创建字典
> <span style="color: #8968CD"> 示例: person 字典包含了姓名、年龄和城市的信息，fruits 字典包含了水果和它们的数量，empty_dict 是一个空字典。</span>
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
fruits = {"apple": 2, "banana": 3, "cherry": 1}
empty_dict = {}
# 使用 dict() 构造函数创建字典
another_dict = dict(name="Bob", age=25, city="San Francisco")
```
#### 1.2. 访问字典值
可以通过键来访问字典中的值,使用方括号[]来获取键对应的值,或者使用`get()`方法
```python
# 使用方括号获取值
another_dict = dict(name="Bob", age=25, city="San Francisco")
name = another_dict["name"]
age = another_dict["age"]
print(f"name: {name}, age: {age}")

# 使用 get() 方法获取值
city = another_dict.get("city")
print(f"city: {city}")
```
> output
```plantuml
name: Bob, age: 25
city: San Francisco
```
#### 1.3. 添加和修改字典的元素
可以通过指定键来添加或修改字典中的元素，如果键已经存在，将会更新对应的值，如果键不存在，将会创建新的键值对
```python
my_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
# 添加新的键值对
my_dict["email"] = "alice@example.com"
# 修改已有的键值
my_dict["age"] = 90
print(my_dict)

# output
# {'name': 'Bob', 'age': 90, 'city': 'San Francisco', 'email': 'alice@example.com'}
```
#### 1.4. 删除字典元素
可以使用`del`语句删除字典中的元素，也可以使用`pop()`方法删除指定键的元素
```python
my_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"my_dict原值{[my_dict]}")
# 使用del语句删除元素
del my_dict["age"]
print(f"删除键为\'age\'的元素,结果为: {my_dict}")

# 使用del语句删除元素
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"New_dict原值{New_dict}")
new = New_dict.pop("name")
print(f"pop函数返回被删除指定键的值{new}")
print(f"删除键为\'name\'的元素,结果为: {New_dict}")
```
> output
```plantuml
my_dict原值: {'name': 'Bob', 'age': '25', 'city': 'San Francisco'}
删除键为'age'的元素,结果为: {'name': 'Bob', 'city': 'San Francisco'}
-----------------------------
New_dict原值{'name': 'Bob', 'age': '25', 'city': 'San Francisco'}
pop函数返回被删除指定键的值Bob
删除键为'name'的元素,结果为: {'age': '25', 'city': 'San Francisco'}
```
#### 1.5. 字典的遍历
字典中的元素是无序的，但可以通过不同的方式进行遍历
+ 遍历键
可以使用`key()`方法获取字典中的所有键，并进行遍历。
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
for key in New_dict.keys():
    print(f"字典New_dict的key: {key}")
```
> output
```plantuml
字典New_dict的key: name
字典New_dict的key: age
字典New_dict的key: city
```
+ 遍历值
可以使用values()方法获取字典中的所有值，并进行遍历
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
for value in New_dict.values():
    print(f"字典New_dict的value: {value}")
```
> output
```plantuml
字典New_dict的value: Bob
字典New_dict的value: 25
字典New_dict的value: San Francisc
```
+ 遍历键值对
可以使用`items()`方法获取字典中的所有键值对，并进行遍历
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
for key,value in New_dict.items():
    print(f"字典New_dict: key[{key}],value: [{value}]")
```
> output
```plantuml
字典New_dict: key[name],value: [Bob]
字典New_dict: key[age],value: [25]
字典New_dict: key[city],value: [San Francisco]
```
#### 2. 字典的常见操作
除了基本的创建，访问和遍历操作，字典还支持许多其他常见的操作，例如判断键是否存在，获取字典长度等
+ 2.1. 判断键值是否存在
可以使用`in`关键字来判断键值是否存在与字典中
```python
# 使用in
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
if "name" in New_dict:
    print(f"字典New_dict中存在\'name\'键，值为:{New_dict['name']}")
else:
    print(f"字典New_dict中不存在\'name\'键")
print("-----------------------------")
# 使用 not in
if "age" not in New_dict:
    print(f"字典New_dict中不存在\'name\'键")
else:
    print(f"字典New_dict中存在\'age\'键，值为:{New_dict['age']}")
```
> output
```plantuml
字典New_dict中存在'name'键，值为:Bob
-----------------------------
字典New_dict中存在'age'键，值为:25
```
+ 2.2. 获取字典长度
使用`len()`函数获取字典的长度
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
print(f"字典New_dict的长度为:{len(New_dict)}")
```
> output
```plantuml
字典New_dict的长度为:3
```
+ 2.3 清空字典
使用`clear()`方法清空字典中所有的键值对
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}.clear()
print(New_dict)  #返回None
```
#### 3. 字典的默认值
有时候需要访问字典中不存在的键时，不抛出 KeyError 异常，而是返回一个默认值。可以使用get()方法来实现这一点。
如果字典中不存在键"nonexistent_key"，则上述代码将返回"default_value"。
> <span style="color: #8968CD">示例 </span>
```plantuml
value = my_dict.get("nonexistent_key","default_value")
```
#### 4. 字典推导式
类似于列表推导式，Python还支持字典推导式，用于创建字典。
> <span style="color: #8968CD">示例 </span>
```python
numbers = [1, 2, 3, 4, 5]
square_dict = {num: num ** 2 for num in numbers}
```
> output
```plantuml
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
#### 5. 字典的排序
字典本身就是无序的，但可以根据键或值对字典进行排序
+ 按键排序
使用`sorted()`函数按照键对字典进行排序
> <span style="color: #8968CD">示例 </span>
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
sorted_dict = {key: New_dict[key] for key in sorted(New_dict)}
print(sorted_dict)
```
> output
```plantuml
{'age': '25', 'city': 'San Francisco', 'name': 'Bob'}
```
+ 按值排序
使用`sorted()`函数和自定义的排序函数来按值对字典进行排序
> <span style="color: #8968CD">示例 </span>
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
sorted_dict = {key: value for key, value in sorted(New_dict.items(), key=lambda item: item[1])}
print(sorted_dict)
```
> output
```plantuml
{'age': '25', 'name': 'Bob', 'city': 'San Francisco'}
```
#### 6. 字典的复制
在Python中，字典的赋值是浅拷贝，如果需要创建一个新的独立字典，可以使用copy()方法或字典构造函数
> <span style="color: #8968CD">示例 </span>
```python
New_dict = {"name":"Bob", "age":"25","city":"San Francisco"}
new_dict = New_dict.copy()  # 使用 copy()
print(f"使用copy方法复制字典 {new_dict}")
another_dict = dict(New_dict)  # 使用字典构造函数
print(f"使用字典构造函数进行字典的复制 {another_dict}")
```
> output
```plantuml
使用copy方法复制字典 {'name': 'Bob', 'age': '25', 'city': 'San Francisco'}
使用字典构造函数进行字典的复制 {'name': 'Bob', 'age': '25', 'city': 'San Francisco'}
```
#### 7. 字典的嵌套
字典可以包含另一个字典作为值，实现更复杂的数据结构
```python
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 22, "city": "Los Angeles"}
}
print(f"students的类型: {type(students)}获取嵌套字典students中Alice的年龄{students['Alice']['age']}")
```
> output
```plantuml
students的类型: <class 'dict'>获取嵌套字典students中Alice的年龄25
```
#### 7. 从键值对列表创建字典
使用`dict()`方法将列表转换为字典(dict)
```python
pairs =[("name","Alice"),("age",12)]
person = dict(pairs)
print(person)
```
> output
```plantuml
{'name': 'Alice', 'age': 12}
```
#### 8. 使用`zip()`创建字典
```python
keys=["name","age","city"]
values =["Alice",12,"New York"]
preson = dict(zip(keys,values))
```
> output
```plantuml
使用zip创建字典: {'name': 'Alice', 'age': 12, 'city': 'New York'}
```
#### 9. 使用`collections.Counter`计数
`Counter`是一个字典子类，用于计数。
```python
counts = Counter(["apple", "banana", "apple", "orange", "banana", "banana"])
print(f"类型: {type(counts)},计数: {counts}")
```
> output
```plantuml
类型: <class 'collections.Counter'>,计数: Counter({'banana': 3, 'apple': 2, 'orange': 1})
```
#### 10. 字典的合并
+ 使用`update`方法
```python
person1={"name":"Alice","age":12}
person2={"name":"Bob","age":13}
info = {"email":"alice@example.com","city":"New York"}
person1.update(info)
print(f"字典info合并到字典person1中，{person1}")
person2.update(info)
print(f"字典info合并到字典person2中，{person2}")
```
> output
```plantuml
字典info合并到字典person1中，{'name': 'Alice', 'age': 12, 'email': 'alice@example.com', 'city': 'New York'}
字典info合并到字典person2中，{'name': 'Bob', 'age': 13, 'email': 'alice@example.com', 'city': 'New York'}
```
+ 使用字典推导式
```python

```
### 5. 字典的键值对
字典中的每个元素都是一个键值对，其中键(key)是唯一的，用于查找和访问值(value),键和值之间使用冒号`:` 分隔
> <span style="color: #8968CD"> 示例: 字典 person 包含了三个键值对，分别是 "name": "Alice"、"age": 30 和 "city": "New York"。</span>
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
```
