## Python 中判断某个元素是否包含
### 1. 成员运算符`in`和`not in`
最基本的方法是使用成员运算符`in`和`not in`,这两个运算符能够快速判定一个元素是否存在于列表中
```python
# 使用成员运算符
my_list = [1, 2, 3, 4, 5]

# 判定元素是否存在
element_to_ckeck = 3
if element_to_ckeck in my_list:
    print(f"{element_to_ckeck}存在于列表中")
else:
    print(f"{element_to_ckeck} 不存在于列表中")

# 或者使用not in 判定不存在
element_to_ckeck = 6
if element_to_ckeck not in my_list:
    print(f"{element_to_ckeck} 不存在于列表中")
else:
    print(f"{element_to_ckeck} 存在于列表中")

# output
# 3 存在于列表中
# 6 不存在于列表中
```
### 2. 使用`count()`方法
`count()`方法能够统计列表中特定元素的出现次数，通过判断次数是否大于零，能够得知元素是否存在
```python
# 使用 count() 方法
my_list =["Hello","World","Python"]
element_to_check = 'Hello'
if my_list.count(element_to_check) >0:
    print(f"{element_to_check} 存在于字符串my_list中")
else:
    print(f"{element_to_check} 不存在于字符串my_list中")
# output
# Hello 存在于字符串my_list中
```
### 3. 使用`any()`函数
`any()`函数接受一个可迭代对象，只要其中任何一个元素为真(即非零，非空，非`None`等)，就返回`True`,这个特性可以用于判定列表是否包含某个元素
```python
my_list =["Hello","World","Python"]
if any(x == "Hello" for x in my_list):
    print(f"\Hello\' 存在于列表中")
else:
    print(f"\Hello\' 不存在于列表中")

# output
# 'Hello' 存在于列表中
```
### 4. 使用`filter()`函数
`filter()`函数返回一个迭代器，其中包含使函数返回`True`的元素,可以使用`bool`函数作为过滤器，判断元素是否存在于列表中。
```python
my_list =["Hello","World","Python"]
if next(filter(lambda x: x == "Hello",my_list),None)is not None:
    print(f"\'Hello\' 存在于列表中")
else:
    print(f"\'Hello\' 不存在于列表中")

if next(filter(lambda x: x == "Helwlo",my_list),None)is not None:
    print(f"\'Helwlo\' 存在于列表中")
else:
    print(f"\'Helwlo\' 不存在于列表中")
    
# output
# 'Hello' 存在于列表中
# 'Helwlo' 不存在于列表中
```

### 5. set转换 将列表转换为集合`(set)`能够大副提高查找速度，因为集合是哈希表，查找操作的时间复杂度为`O(1)`
```python
my_list =["Hello","World","Python"]
if "Hello" in set(my_list):
    print(f"\'Hello\' 存在于列表中,其下标为{my_list.index('Hello')}")
else:
    print(f"\'Hello\' 不存在于列表中")
if "Python" in set(my_list):
    print(f"\'Python\' 存在于列表中,其下标为:{my_list.index('Python')}")
else:
    print(f"\'Hello\' 不存在于列表中")

# output
# 'Hello' 存在于列表中,其下标为0
# 'Python' 存在于列表中,其下标为:2
```
### 6. 使用`bisect`模块
如果列表是有序的,可以使用`bisect` 模块进行二分查找，进一步提高查找效率.
```python
from bisect import bisect_left
my_list =["Hello","World","Python"]
sorted_list = sorted(my_list)
if bisect_left(sorted_list,"Python"):
    print(f"排序后: {sorted_list}")
    print(f"\'Python\' 存在于列表中,其下标为:{sorted_list.index('Python')}")
else:
    print(f"\Python\' 不存在于列表中")

# output
# 排序后: ['Hello', 'Python', 'World']
# 'Python' 存在于列表中,其下标为:1
```
### 7. 使用`numpy`库
对于数值型列表，`numpy`提供了强大的数组操作，包括成员判定。
```python
import numpy as np
my_list =["Hello","World","Python"]
if np.isin("Python",my_list):
    print(f"\'Python\' 存在于列表中,其下标索引为 {my_list.index('Python')}")
else:
    print(f"\Python\' 不存在于列表中")

# output
# 'Python' 存在于列表中,其下标索引为 2
```
### 8. 使用 any()和生成器表达式
结合`any()`和生成器表达式，可以在一行代码中进行简洁的判定
```python
my_list =["Hello","World","Python"]
if any(element == "World" for element in my_list):
    print(f"\'World\' 存在于列表中,其下标索引为: {my_list.index('World')}")
else:
    print(f"\'World\' 不存在于列表中")

# output
# 'World' 存在于列表中,其下标索引为: 1
```

### 9. 使用`all()`函数
反过来，如果想要确认列表中所有元素均满足某个条件，可以使用`all()`函数
```python
my_list =[1,2,3,4]
if (all(x >3 for x in my_list)):
    print("列表中所有元素均大于3")
else:
    print("列表中所有元素有存在小于3的")

# output
# 列表中所有元素有存在小于3的
```
### 10. 使用自定义函数
有时，可能需要更复杂的条件判定，这时可以定义一个自定义函数
```python
my_list =["Hello","World","Python"]
def contains_element(lst,element):
    return any(x == element for x in lst)

if contains_element(my_list,"Python"):
    print(f"\'Python\' 存在于列表中,其下标索引为: {my_list.index('Python')}")
else:
    print(f"\'Python\' 不存在于列表中")
# output
# 'Python' 存在于列表中,其下标索引为: 2
```
