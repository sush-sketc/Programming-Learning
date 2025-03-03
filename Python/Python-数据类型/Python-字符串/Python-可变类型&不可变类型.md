## Python 可变类型与不可变类型详解及实际应用场景 <a name="Python_if_003"></a>

### 1. 可变类型
可变类型指的是在创建后可以被修改的数据类型。常见的可变类型包括列表`（list）`、字典`（dictionary）`和集合`（set）`。
> <span style="color: #8968CD">示例</span>
```python
# 可变类型示例 - 列表
mutable_list = [1, 2, 3]
mutable_list.append(4)
print(mutable_list)  # 输出: [1, 2, 3, 4]

# 可变类型示例 - 字典
mutable_dict = {'key': 'value'}
mutable_dict['new_key'] = 'new_value'
print(mutable_dict)  # 输出: {'key': 'value', 'new_key': 'new_value'}
```
### 2. 不可变类型
不可变类型指的是创建后不能被修改的数据类型。常见的不可变类型包括整数（int）、浮点数（float）、字符串（str）和元组（tuple）。
> <span style="color: #8968CD">示例</span>
```python
# 不可变类型示例 - 整数
immutable_int = 42
# 试图修改会引发错误: 'int' object does not support item assignment
# immutable_int[0] = 1

# 不可变类型示例 - 字符串
immutable_str = "Hello"
# 试图修改会引发错误: 'str' object does not support item assignment
# immutable_str[0] = 'h'
```
### 3. 区别及应用场景
1. 内存中的表现： 可变类型在内存中有一个地址，如果修改了值，地址不会变化；而不可变类型修改值时，会生成一个新的对象，地址会改变。
2. 线程安全： 不可变类型是线程安全的，因为无法在原地修改值；而可变类型在多线程环境下需要考虑同步问题。
3. 哈希值： 不可变类型具有哈希值，可以作为字典的键；可变类型没有哈希值，不能作为字典的键。
#### 3.1 应用场景
+ 可变类型： 适用于需要频繁改变值的情况，如动态数组、键值对的动态更新等。
+ 不可变类型： 适用于需要保持数据不变性的场景，如在哈希表中使用作为键、在多线程环境下提高线程安全性等。

### 4. 可变类型的注意事项
虽然可变类型灵活且功能强大，但在使用时需要注意一些陷阱。下面通过示例代码展示一些常见的注意事项:
> <span style="color: #8968CD">示例</span>
```python
# 注意事项1: 函数默认参数为可变类型
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# 输出：[1]
print(append_to_list(1))

# 输出：[1, 2]
print(append_to_list(2))
```
>> 在上述代码中，默认参数`my_list`是一个可变类型的列表。由于默认参数在函数定义时只计算一次，如果在多次调用中对默认参数进行了修改，它将在后续调用中保持修改后的状态。为避免此类问题，应将可变类型设为不可变类型或在函数内部进行处理。

### 4. 不可变类型的优势
不可变类型的不变性使其在一些特定场景下表现出来，
>  <span style="color: #8968CD">使用元组作为字典键</span>
```python
#使用元组作为字典键
coordinates = {[1,2]:'point A',[3,4]:'poing B'}
#输出:point A
print(coordinates[(1,2)])
```
>> 由于元组是不可变类型，它可以安全的用作字典键，这在需要保持数据不变性的情况下非常有用。

### 5. 高效的使用可变类型
尽管可变类型需要谨慎使用，但在某些情况下，高效的利用其特性可以带来便利，一下是一个使用字典的典型示例，展示了如何通过`setdefault`方法避免不必要的键检查
```python
# 高效使用可变类型 - 字典
word_count = {}
text = "apple orange banana apple oranage"
words = text.split()
for word in words:
    #使用setdefault一行代码实现计数
    word_count[word] = word_count.setdefault(word,0)+1
#输出：{'apple': 2, 'orange': 1, 'banana': 1, 'oranage': 1}
print(word_count)
```
>> 上面代码中使用字典记录单词出现的次数，通过`setdefault`方法,能够在一行代码总实现对字典键对计数,避免了显示对键检查和初始化
### 6. 深拷贝和浅拷贝
在处理可变类型时深拷贝`(copy.deepcopy)`和浅拷贝`(copy.copy)`也是需要注意的问题，深拷贝会创建原始对象及所有嵌套对象的完整副本。而浅拷贝只会复制对象本身及其顶层元素。
>  <span style="color: #8968CD">示例:</span>
```python
import copy
 #深拷贝
original_list = [1,2,3,4]
deep_copy_list = copy.deepcopy(original_list)
deep_copy_list[1][0] = 99
#输出
print(original_list)
print(deep_copy_list)

#output
[1, [2, 3], 4]
[1, [99, 3], 4]
```
>> 通过深拷贝，确保了嵌套列表的独立性。如果使用浅拷贝，对嵌套列表的修改将会影响原始列表。