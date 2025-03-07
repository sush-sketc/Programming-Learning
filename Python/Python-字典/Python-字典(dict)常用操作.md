## Python字典（dict）常用操作

在Python中，字典是一种非常强大且常用的数据结构。它提供了一种键值对（key-value pair）的存储方式，使得数据的存取变得既快速又方便，字典的键可以是任何
不可变类型，如字符串，数字或元组，而值则可以是任何数据类型。

> > **[示例代码](./code/code-03.py)**

### 1. 创建字典

创建字典的基本方法是使用花括号`{}`，在其中放置以逗号`,`分隔的简直对，例如:

```python
my_dict = {'name': '北京', 'age': 12, 'city': "海淀区"}
```

此外，也可以使用`dict()`函数来创建字典,例如:

```python
my_dict = dict(name='张三', age=30, city="北京")
```

### 2. 访问字典中值

要访问字典中的值，可以使用相应的键，例如，要获取字典中的name

```python
my_dict = dict(name='张三', age=30, city="北京")
print("name = ", my_dict['name'])
```

> **output**

```plantuml
name =  张三
```

如果尝试访问字典中不存在的键，将引发`KeyError`,为了避免这种错误，可以使用`get()`方法，当键不存在时，它将返回`None`
或者指定的默认值，例如：

```python
my_dict = dict(name='张三', age=30, city="北京")
address = my_dict.get('address', '地址未知')
print(address)
```

### 3. 修改字典

可以直接通过键来修改字典中的值，如果该键存在，其值将被更新，否则将添加新的键值对，例如：

```python
my_dict = dict(name='张三', age=30, city="北京")
my_dict['age'] = 44
my_dict['address'] = "上海"
print(my_dict)
```

> **output**

```plantuml
原 my_dict =  {'name': '张三', 'age': 30, 'city': '北京'}
修改后 my_dict =  {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
```

### 4. 删除字典中的元素

可以使用`del`语句来删除字典中的特定元素，例如:

```python
my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
del my_dict['age']
print("删除字典中的元素 age = ", my_dict)
```

还可以使用`pop()`方法来删除字典中的特定元素，例如：

```python
my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
print("pop方法删除", my_dict.pop('city'))
```

> **output**

```plantuml
del 删除 {'name': '张三', 'city': '北京', 'address': '上海'}
pop方法删除 北京
```

### 5. 字典的遍历

遍历字典时，可以使用`itmes()`方法来获取键值对，`keys()`方法来获取所在键，以及`values()`方法来获取所有值，例如：
还可以使用使用`if`来判断键或值是否存在，然后执行相关操作

```python
my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
for key, value in my_dict.items():
    print("keys =%s \tvalues = %s" % (key, value))

my_dict = {'name': '张三', 'age': 44, 'city': '北京', 'address': '上海'}
for key, value in my_dict.items():
    if key == 'title':
        print(f"{key}-{value}")
        # 按值排序
        sourted_dict = {key: value for key, value in sorted(my_dict.items(), key=lambda item: item[1])}
        break
    elif key != 'title':
        # copy()拷贝
        new_dict = my_dict.copy()
        # 向新拷贝的字典中添加值
        new_dict["title"] = "alice@example.com"
        # 输出new_dict中所有元素的键
        print("Keys = ", new_dict.keys())
        # 输出new_dict中所有值
        print("values = ", new_dict.values())
        # 获取字典的长度
        print("length", len(new_dict))
        break
    else:
        print("not key")
        break
# print(my_dict)
# print(new_dict)
```