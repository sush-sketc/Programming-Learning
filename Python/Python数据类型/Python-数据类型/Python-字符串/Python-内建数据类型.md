## Python 内建数据类型 <a name="Python_if_003"></a>

### 1. 数字类型
Python支持多种数字类型，包括整数（int）、浮点数（float）和复数（complex）。
#### 1.1. <span style="color: #8968CD">**整数(int)**</span>
整数类型用于表示没有小数部分的数字。
```python
a = 10
b = -5
c = 0

print(a, type(a))  # 输出：10 <class 'int'>
print(b, type(b))  # 输出：-5 <class 'int'>
print(c, type(c))  # 输出：0 <class 'int'>
```
#### 1.2. <span style="color: #8968CD">**浮点数(float)**</span>
浮点数类型用于表示带有小数部分的数字
```python
x = 3.14
y = -0.001
z = 2.0

print(x, type(x))  # 输出：3.14 <class 'float'>
print(y, type(y))  # 输出：-0.001 <class 'float'>
print(z, type(z))  # 输出：2.0 <class 'float'>
```
#### 1.3. <span style="color: #8968CD">**复数(complex)**</span>
复数类型用于表示包含实部和虚部的数字。
```python
p = 1 + 2j
q = -3j
r = 4 + 0j

print(p, type(p))  # 输出：(1+2j) <class 'complex'>
print(q, type(q))  # 输出：-3j <class 'complex'>
print(r, type(r))  # 输出：(4+0j) <class 'complex'>
```

### 2. 序列类型
序列类型包括字符串（str）、列表（list）和元组（tuple）。它们都是有序的集合。
#### 2.1. <span style="color: #8968CD">**字符串(str)**</span>
字符串用于表示文本数据。可以用单引号、双引号或三引号包围。
```python
s1 = 'Hello'
s2 = "World"
s3 = """Python is fun!"""

print(s1, type(s1))  # 输出：Hello <class 'str'>
print(s2, type(s2))  # 输出：World <class 'str'>
print(s3, type(s3))  # 输出：Python is fun! <class 'str'>
```

#### 2.2. <span style="color: #8968CD">**列表(list)**</span>
列表是一种可变的序列类型，用于存储多个元素
```python
lst = [1, 2, 3, 4, 5]
print(lst, type(lst))  # 输出：[1, 2, 3, 4, 5] <class 'list'>

# 访问列表元素
print(lst[0])  # 输出：1

# 修改列表元素
lst[1] = 10
print(lst)  # 输出：[1, 10, 3, 4, 5]

# 列表切片
lst_slice = lst[1:4]
print(lst_slice)  # 输出：[10, 3, 4]

# 列表方法
lst.append(6)
print(lst)  # 输出：[1, 10, 3, 4, 5, 6]
```
#### 2.3. <span style="color: #8968CD">**元组(tuple)**</span>
元组是一种不可变的序列类型，一旦创建就不能修改。
```python
tpl = (1, 2, 3, 4, 5)
print(tpl, type(tpl))  # 输出：(1, 2, 3, 4, 5) <class 'tuple'>

# 访问元组元素
print(tpl[0])  # 输出：1

# 元组切片
tpl_slice = tpl[1:4]
print(tpl_slice)  # 输出：(2, 3, 4)
```

### 3. 映射类型
映射类型包括字典（dict），它是一种键值对的集合。
#### 3.1. <span style="color: #8968CD">**字典(dict)**</span>
字典用于存储键值对，键必须是唯一的。
```python
d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(d, type(d))  # 输出：{'name': 'Alice', 'age': 25, 'city': 'New York'} <class 'dict'>

# 访问字典元素
print(d['name'])  # 输出：Alice

# 修改字典元素
d['age'] = 26
print(d)  # 输出：{'name': 'Alice', 'age': 26, 'city': 'New York'}

# 添加字典元素
d['country'] = 'USA'
print(d)  # 输出：{'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
```

### 4. 集合类型
集合类型包括集合（set）和冻结集合（frozenset）。集合是一种无序的不重复元素的集合。
#### 4.1. <span style="color: #8968CD">**集合(set)**</span>
集合用于存储唯一元素。
```python
s = {1, 2, 3, 4, 5}
print(s, type(s))  # 输出：{1, 2, 3, 4, 5} <class 'set'>

# 添加集合元素
s.add(6)
print(s)  # 输出：{1, 2, 3, 4, 5, 6}

# 移除集合元素
s.remove(3)
print(s)  # 输出：{1, 2, 4, 5, 6}
```
#### 4.2. <span style="color: #8968CD">**冻结集合(frozenset)**</span>
冻结集合是一种不可变的集合
```python
fs = frozenset([1, 2, 3, 4, 5])
print(fs, type(fs))  # 输出：frozenset({1, 2, 3, 4, 5}) <class 'frozenset'>
```
### 5. 其他内建数据类型
#### 5.1. <span style="color: #8968CD">**布尔类型(bool)**</span>
布尔类型用于表示真（True）和假（False）。
```python
a = True
b = False

print(a, type(a))  # 输出：True <class 'bool'>
print(b, type(b))  # 输出：False <class 'bool'>
```
#### 5.2. <span style="color: #8968CD">**空类型(NoneType)**</span>
空类型用于表示空值，即None
```python
n = None
print(n, type(n))  # 输出：None <class 'NoneType'>
```


