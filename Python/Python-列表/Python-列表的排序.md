## Python 列表排序: 从基础到高级
### 1. 使用`sorted()`函数
Python 提供了内置的`sorted()`函数，用于对可迭代对象进行排序，该函数返回一个新的已排序列表，不会修改原始列表。
```python
str_string= ["The","is","python","happy"]
sorted_list = sorted(str_string)
print(f"\'sorted\'方法返回一个新的排序列表，结果为: {sorted_list}")

# output
# 'sorted'方法返回一个新的排序列表，结果为: ['The', 'happy', 'is', 'python']
```

### 2. 使用`sort()`方法
列表对象本身也提供了`sort()`方法，可以直接直接对列表进行排序，与`sorted()`不同，`sort()`会直接修改原始列表
```python
fruits = ['apple','orange','banana','grage']
fruits.sort()
print(fruits)

# output
# ['apple', 'banana', 'grage', 'orange']
```

### 2. 高级排序方法
#### 2.1. 自定义排序规则
可以使用`key`参数来指定排序时的自定义规则，例如，按字符串长度进行操作
```python
words = ['python','is','awesome','language']
sorted_words = sorted(words,key=len)
print(sorted_words)

# output
# ['is', 'python', 'awesome', 'language']
```
#### 2.2. 逆序排序
通过`reverse`参数，可以轻松实现逆序排序
```python
words = ['python','is','awesome','language']
sorted_desc = sorted(words, reverse=True)
print(sorted_desc)

# output
# ['python', 'language', 'is', 'awesome']
```
