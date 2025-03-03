## Python 列表合并

### 1. 使用`+`运算法
通过 + 运算符直接将两个列表合并，简单直观。适用于小型列表的合并。
```python
list1 = [1,2,3]
list2 = [4,5,6]
print(f"列表合并list1={list1},list2={list2},合并后{list1+list2}")

#output: 列表合并list1=[1, 2, 3],list2=[4, 5, 6],合并后[1, 2, 3, 4, 5, 6]
```
### 2. 使用`extend()`方法
`extend()`方法用于将一个可迭代对象的元素添加到列表中，就地修改原列表，适用于需要在原列表上进行操作的场景
```python
list1 =[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(f"列表{list2}添加到列表{list1}中,添加后list1: {list1}")

# output
# 列表[4, 5, 6]添加到列表[1, 2, 3, 4, 5, 6]中,添加后list1: [1, 2, 3, 4, 5, 6]
```

### 3. 使用`append()`和循环
通过`append()`方法和循环逐一添加元素，适用于需要逐一处理元素的情况，但在大型数据上可能效率较低。
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print(list1)

# output
# [1, 2, 3, 4, 5, 6]
```

### 4. 使用`*`运算符
在Python 3.5及以上版本，* 运算符可以用于解压列表，将元素直接扩展到新列表。简洁且适用于合并多个小型列表
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)

# output
# [1, 2, 3, 4, 5, 6]
```

### 5. 使用`itertools.chain()`
`itertools.chain()` 函数连接多个可迭代对象，返回一个迭代器。通过将其结果转换为列表，实现多个列表的合并。在处理大量数据时更为高效。
```python
from itertools import chain
list1 =[1,2,3]
list2=[4,5,6]
print(f"实现多个列表的合并:{list(chain(list1,list2))}")

# output
# 实现多个列表的合并:[1, 2, 3, 4, 5, 6]
```

### 6. 实用案例
+ 合并数字列表
假设有两个包含数字的列表，分别表示两个不同月份的销售数量
```python
sales_january =[100,150,120,200]
sales_february =[180,210,150,220]
```
通过使用`+`运算符可以轻松的合并这两个列表，得到整个季度的销售数据。
```python
sales_january =[100,150,120,200]
sales_february =[180,210,150,220]
quarterly_sales = sales_january +sales_february
print(quarterly_sales)
```
+ 合并字符串列表
假设有两个包含字符串的列表，分别表示两个不同部门的员工名单，通过使用`extend()`方法，可以将it部门的员工添加到人力资源部门，实现整体员工名单的合并
```python
hr_department = ['Alice','Bob','Charlie']
it_department = ['David','Eva','Frank']
hr_department.extend(it_department)
print(f"使用extend()方法合并: {hr_department}")
#output: 使用extend()方法合并: ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
```
+ 合并字典列表
两个包含字典的列表，表示学生和老师信息，通过使用`*`运算符，可以将学生和老师的信息合并成一个包含所有人员的信息列表。
```python
students=[{'name':'Alice','age':13},{'name':'Bob','age':15}]
teachers = [{'name':'Eva','subject':"Math"},{'name':'Mike','subject':'English'}]
all_personnel = [*students,*teachers]
print(all_personnel)
#output
[{'name': 'Alice', 'age': 13}, {'name': 'Bob', 'age': 15}, {'name': 'Eva', 'subject': 'Math'}, {'name': 'Mike', 'subject': 'English'}]
```
