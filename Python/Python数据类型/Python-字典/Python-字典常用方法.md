## Python 字典常用方法

字典`(Dictionary)`是`Python`提供的一种常用的数据结构，它用于存放具有映射关系的数据。
字典由键(key)和值`(value)`成对组成，键和值中间以冒号`:`隔开，项之间用逗号`,`隔开
字典也被称作关联数组或哈希表。下面是几种常见的字典创建方式：

>> [示例代码](code/code-02.py)
```python
# 方法1
dict1 = {'Author': 'Python', 'age': 20, 'sex': 'man'}
# 方法2
lst = [("Author", "Python"), ("age", 20), ("sex", "man")]
dic2 = dict(lst)
# 方法3
dic3 = dict(Author='Python', age=99, sex="man")
# 方法4
list1 = ['Author', 'age', 'sex']
list2 = ["Python", 121, "man"]
dict4 = dict(zip(list1, list2))
```

字典创建的方式还有很多种。
字典由 dict 类代表，可以使用 dir(dict) 来查看该类包含哪些方法，输入命令，可以看到如下输出结果：

```python
methods = dir(dict)
print('methods = ', methods)
# output
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

字典的方法和属性有很多种，一下介绍常用的方法

### 1. `dict.clear()`

`clear()`用于清空字典中所有元素(键-值对)，对一个字典执行`clear()`方法之后，该字典就会变成一个空字典

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', 99, '男']
dic1 = dict(zip(list1, list2))
dic1.clear()
```
> **output**
```plantuml
dic1 = {'Author': 'Python', 'age': 99, 'sex': '男'}
dic1 = {}
```

### 2. `dict.copy()`

`copy()`用于返回一个字典的浅拷贝

```python 
list1 = ['Author', 'age', 'sex']
list2 = ['Python', 99, '男']
dic1 = dict(zip(list1, list2))
dic2 = dic1  # 浅拷贝: 引用对象
dic3 = dic1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dic1['age'] = 18
# dic1 = {'Author': 'Python', 'age': 18, 'sex': '男'}
# dic2 = {'Author': 'Python', 'age': 18, 'sex': '男'}
# dic3 = {'Author': 'Python', 'age': 99, 'sex': '男'}
```

> >  <span style="color: #FF6EB4">  其中 dic2 是 dic1 的引用，所以输出结果是一致的，dic3 父对象进行了深拷贝，不会随dic1 修改而修改，子对象是浅拷贝所以随 dic1 的修改而修改，注意父子关系。</span>
> 拓展深拷贝`copy.deepcopy()

```python  
import copy

list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
dic2 = dic1
dic3 = dic1.copy()
dic4 = copy.deepcopy(dic1)
dic1['age'].remove(18)
dic1['age'] = 20
```
> **output**
```plantuml
dic1 = {'Author': 'Python', 'age': 20, 'sex': '男'}
dic2 = {'Author': 'Python', 'age': 20, 'sex': '男'}
dic3 = {'Author': 'Python', 'age': [99], 'sex': '男'}
dic4 = {'Author': 'Python', 'age': [18, 99], 'sex': '男'}
```

> > <span style="color: #FF6EB4"> dic2 是 dic1 的引用，所以输出结果是一致的；dic3 父对象进行了深拷贝，不会随dic1 修改而修改，子对象是浅拷贝所以随 dic1 的修改而修改.
>> dic4 进行了深拷贝，递归拷贝所有数据，相当于完全在另外内存中新建原字典，所以修改dic1不会影响dic4的数据 </span>

### 3.`dict.fromkeys()`

`fromkeys()`使用给定的多个键创建一个新字典，值默认都是`None`,也可以传入一个参数作为默认的值。

```python
list1 = ['Author', 'age', 'sex']
dic1 = dict.fromkeys(list1)
dic2 = dict.fromkeys(list1, 'Python')
```
> **output**
```plantuml
dic1 = {'Author': None, 'age': None, 'sex': None}
dic2 = {'Author': 'Python', 'age': 'Python', 'sex': 'Python'}
```

### 4. `dict.get()`
`get()`用于返回指定键的值，也就是根据键来获取值，在键不存在的情况下，返回`None`,也可以指定返回值。
```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18,99], '男']
dic1 = dict(zip(list1, list2))
Author = dic1.get('Author')
# Author = Python
phone = dic1.get('phone')
# phone = None
phone = dic1.get('phone','12345678')
# phone = 12345678
```
### 4. `dict.items()`

`items()` 获取字典中的所有键-值对，一般情况下可以将结果转化为列表在进行后续处理。

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 19], '男']

items = dict(zip(list1, list2))
items = dict.items(items)
print(f"items= ${items}")
print('items = ', items)
print(type(items))
print('items = ', list(items))
```

> **output**

```plantuml
items= $dict_items([('Author', 'Python'), ('age', [18, 19]), ('sex', '男')])
<class 'dict_items'>
items =  [('Author', 'Python'), ('age', [18, 19]), ('sex', '男')]
```

### 5. `dict.keys()`

`keys()`返回一个字典的所有键

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 88], '男']
dic1 = dict(zip(list1, list2))
keys = dic1.keys()
print('Keys = ', keys)
print(type(keys))
print('keys = ', list(keys))
```

> **output**

```plantuml
Keys =  dict_keys(['Author', 'age', 'sex'])
<class 'dict_keys'>
keys =  ['Author', 'age', 'sex']
```

### 6. `dict.pop()`

`pop()`返回制定键对应的值，并在原字典中删除这个键-值对

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 88], '男']
dic1 = dict(zip(list1, list2))
print('dic1 = ', dic1)

sex = dict.pop('sex')
print('sex = ', sex)
print('dict1 = ', dic1)
```

> **output**

```plantuml
dic1 =  {'Author': 'Python', 'age': [18, 88], 'sex': '男'}
sex =  男
dict1 =  {'Author': 'Python', 'age': [18, 88]}
```

### 7.`dict.popitem()`

`popitem()` 删除字典中的最后一个键和值

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [189.19], '男']
dic1 = dict(zip(list1, list2))
dic1.popitem()
print('dic1 = ', dic1)
```

> **output**

```plantuml
dic1 =  {'Author': 'Python', 'age': [189.19]}
```

### 8. `dict.setdefault()`

`setdefault()`和`get()`类似，但如果键不存在于字典中，将会添加键并将值设置为default

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
dic1.setdefault('Author', '')
print('dic1 = ', dic1)
dic1.setdefault('name', 'Hello')
print('dic1 = ', dic1)
```

> **output**

```plantuml
dic1 =  {'Author': 'Python', 'age': [18, 99], 'sex': '男'}
dic1 =  {'Author': 'Python', 'age': [18, 99], 'sex': '男', 'name': 'Hello'}
```

### 9. `dict.update(dict1)`

`update()`字典更新，将字典`dict1`的键-值对更新到dict里，如果被更新的字典中已包含对应的键-值对，那么原键-值对会被覆盖，如果被更新的字典中不包含对应的键-值对，则添加该键-值对

```python
list1 = ['Author', 'age', 'sex']
list2 = ['Python', [18, 99], '男']
dic1 = dict(zip(list1, list2))
print("dic1 = ", dic1)
list3 = ['Author', 'phone']
list4 = ['Gello', 12343]
dic2 = dict(zip(list3, list4))
print("dic2 = ", dic2)
dic1.update(dic2)
print("dic1 = ", dic1)
```

> **output**

```plantuml
dic1 =  {'Author': 'Python', 'age': [18, 99], 'sex': '男'}
dic2 =  {'Author': 'Gello', 'phone': 12343}
dic1 =  {'Author': 'Gello', 'age': [18, 99], 'sex': '男', 'phone': 12343}
```

### 10. `dict.values()`

`values()`返回字典所有的值

```python
list1 = ['author', 'age', 'sex']
list2 = ['Python', [12, 234], '男']
dic1 = dict(zip(list1, list2))
values = dic1.values()
print('values = ', values)
print(type(values))
print('values = ', list(values))
```

> **output**

```plantuml
values =  dict_values(['Python', [12, 234], '男'])
<class 'dict_values'>
values =  ['Python', [12, 234], '男']
```