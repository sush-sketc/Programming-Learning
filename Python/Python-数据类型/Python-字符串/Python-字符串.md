## Python 字符串基础到高级

### 1. 字符串的本质与创建

#### 1.1 字符串的创建

字符串可以使用单引号`''`和双引号`""`以及三引号`''' '''`创建
在Python中,字符串是不可变的序列类型
> <span style="color: #8968CD">示例：创建字符串的多种方式</span>

```python
single_quoted = 'Hello World'
double_quoted = "Hello World"
triple_quoted = '''Hello,
 World'''

# 使用单引号或双引号
s1 = 'Hello'
s2 = "World"

# 使用三引号创建多行字符串
s3 = '''This is a
multi-line string'''

# 使用转义字符
s4 = 'It\'s a beautiful day'

# 原始字符串，忽略转义字符
s5 = r'C:\Users\Username\Documents'

# 字节字符串
s6 = b'Hello'  # 只包含ASCII字符

# 使用str()函数
s7 = str(42)  # 将其他类型转换为字符串
```

### 2. 字符串的基本操作

#### 2.1 字符串的拼接

字符串拼接是最常见的操作之一

```python
# 使用+运算符
first_name = 'Johb'
last_name = 'Doe'
full_name = first_name + '' + last_name

# 使用+=运算符
greeting = 'Hello'
greeting += 'World'

# 使用join()方法
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)

# 使用格式化字符串
name = 'Alice'
age = 18
info = f'{name} is {age}'

# 使用str,format()方法
template = '{} is {}'
info = template.format(name, age)
```

**output**

```plantuml
JohbDoe
Python is awesome
Alice is 18
Alice is 18
```

#### 2.2. 字符串重复

使用 * 运算符可以轻松地重复字符串。

```python
laugh = 'Ha' * 3  # 'HaHaHa'
line = '-' * 20  # '--------------------'
```

#### 2.3. 字符串长度

使用内置函数 len() 可以获取字符串的长度。

```python
text = 'Hello, World!'
length = len(text)  # 13
```

### 3. 字符串索引和切片

Python的字符串支持索引和切片操作，这使得访问和提取子字符串变得非常厉害

```python
s = 'Python Programming'

# 索引(正向和反向)
print(s[0])
print(s[-1])

# 基本切片
print(s[7:18])
print(s[:6])
print(s[7:])

# 带步长的切片
print(s[::2])
print(s[::-1])

# 使用切片修改字符串
new_s = s[:6] + ' is ' + s[7:]
print(new_s)
```

**ouput**

```plantuml
P
g
Programming
Python
Programming
Pto rgamn
gnimmargorP nohtyP
Python is Programming
```

### 4. 字符串方法

Python的字符串类型提供了大量的内置方法，用于执行各种字符串操作。

#### 4.1 大小写转换

```python
s = 'Hello, World'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())

# 检查大小写
print('HELLO'.isupper())
print('hello'.islower())
print('Title Case'.istitle())

```

**output**

```plantuml
HELLO, WORLD
hello, world
Hello, world
Hello, World
hELLO, wORLD
True
True
True
```

#### 4.2. 查找和替换

```python
s = 'Python is amazing and Python is powerful'

# 查找
print(s.find('Python'))
print('从索引10开始查找：' + s.find('Python', 10))
print(f'从右侧开始查找: ' + s.rfind('Python'))

# index()方法类似与find(),但在未找到时会引发ValueError
try:
    print(s.index('Java'))
except ValueError:
    print("'Jave' not found in the string")

# 计数
print('统计\'Python\'总共出现几次', s.count('Python'))

# 替换
print('Python 替换为 Java(全部替换)', s.replace('Python', 'Java'))
print('Python 替换为 Java(替换第一次出现的)', s.replace('Python', 'Java', 1))
```

**output**

```plantuml
0
从索引10开始查找： 22
从右侧开始查找:  22
'Jave' not found in the string
统计'Python'总共出现几次 2
Python 替换为 Java(全部替换) Java is amazing and Java is powerful
Python 替换为 Java(替换第一次出现的) Java is amazing and Python is powerful
```

#### 4.3. 分割和连接

```python
# 分割
s = 'apple,banana,orange,grape'
fruits = s.split(',')
print('使用\',\'进行分割', fruits)

# 限制分割次数
print('a,b,c,d'.split(',', 2))

# 按行分割
multiline = '''Line 1
Line 2
Line 3'''
lines = multiline.splitlines()
print('按行分割：', lines)

# 连接
new_s = '-'.join(fruits)
print('连接:', new_s)

# 使用空字符串连接
letters = ['H', 'e', 'l', 'l', 'o']
word = ''.join(letters)
print('使用空字符串连接:', word)
```

**output**

```plantuml
使用','进行分割 ['apple', 'banana', 'orange', 'grape']
['a', 'b', 'c,d']
按行分割： ['Line 1', 'Line 2', 'Line 3']
连接: apple-banana-orange-grape
使用空字符串连接: Hello
```

#### 4.4. 去除空白字符和其他字符

```python
s = '    Hello, World!   '

print('去除全部空白字符：', s.strip())
print('去除开头空白字符:', s.lstrip())
print('去除结尾空白字符:', s.rstrip())

# 去除指定字符
ss = '----Ptyhon...---'
print('去除所有以\'.\'的字符', ss.strip('.'))
print('去除开头以\'.\'的字符', ss.lstrip('.'))
print('去除结尾以\'.\'的字符', ss.rstrip('.'))
```

**output**

```plantuml
去除全部空白字符： Hello, World!
去除开头空白字符: Hello, World!   
去除结尾空白字符:     Hello, World!
去除所有以'.'的字符 ----Ptyhon...---
去除开头以'.'的字符 ----Ptyhon...---
去除结尾以'.'的字符 ----Ptyhon...---
```

#### 4.5 对齐和填充

```python
s = 'Python'
print('字符串结尾添加空白字符:', s.ljust(10))
print('字符串开头添加空白字符:', s.rjust(10))
print('字符串前后添加空白字符:', s.center(10))

# 使用指定字符填充
print('使用\'-\'填充10个', s.ljust(10, '-'))
print('使用\'-\'填充10个', s.ljust(10, '*'))
print('使用\'-\'填充10个', s.ljust(10, '='))

# 使用 zfill()方法在数字字符串左边填充零
intzfi = '43'
print('数字字符串左边填充5个0', intzfi.zfill(5))
```

**output**

```plantuml
字符串结尾添加空白字符: Python    
字符串开头添加空白字符:     Python
字符串前后添加空白字符:   Python  
使用'-'填充10个 Python----
使用'-'填充10个 Python****
使用'-'填充10个 Python====
数字字符串左边填充5个0 00043
```

### 5. 字符串格式化

Python提供了多种字符串格式化的方法，每种方法都有其特定的用途和优势。

#### 5.1. `%`运算符(旧式字符串格式化)

```python
name = 'Alice'
age = 70
print('My name is %s and I am %d years old.' % (name,age))

#使用字典
print('%(name)s is %(age)d years old. '% {'name':'Bob','age':58})
```
**output**
```plantuml
My name is Alice and I am 70 years old.
Bob is 58 years old. 
```

#### 5.2. `str.format()`方法

```python
name = 'Shanghai'
age = 710

print('Name is {} and I am {} years old.'.format(name, age))
# 使用索引
print('The {1} {0} {2}'.format('brown', 'quick', 'fox'))

# 使用命名参数
print('The {adj} {noun}.'.format(adj='北京', noun='上海'))

#格式化选项
pi = 3.14159
print('Pi is approximately {:.2f}'.format(pi))
```
**output**
```plantuml
Name is Shanghai and I am 710 years old.
The quick brown fox
The 北京 上海.
Pi is approximately 3.14
```

### 6. 高级字符串操作
#### 6.1. 字符串比较
Python支持字符串的比较操作，这在排序和条件判断中非常有用。

```python
# 字典序比较
print('apple' < 'banana')  # True
print('Python' == 'python')  # False

# 忽略大小写比较
s1 = 'python'
s2 = 'PYTHON'
print(s1.lower() == s2.lower()) #True
```

#### 6.2. 字符串的成员资格测试
```python
text = 'Python is amazing'
print('Python' in text)  # True
print('Java' not in text)  # True
```
#### 6.3 字符串的开头和结尾检查
```python
filename ='document.txt'
print(filename.startswith('doc'))   #True
print(filename.endswith('.txt'))    #True
```
**output**
```plantuml
True
True
True
True
```

#### 6.4. 字符串的转换和编码
```python
#转换为字节
s ='Hello,World'
b = s.encode('utf-8')
print('转换为字节',b)

#从字节转换为字符串
s2 =b.decode('utf-8')
print('字节转换为字符串',s2)

#处理不同编码
s_unicode ='您好，世界！'
b_gbk= s_unicode.encode('gbk')
s_from_gbk = b_gbk.decode('gbk')
print('处理不同编码:',s_from_gbk)
```
**output**
```plantuml
转换为字节 b'Hello,World'
字节转换为字符串 Hello,World
处理不同编码: 您好，世界！
```
#### 6.5. 使用正则表达式
对于更复杂的字符串操作，可以使用Python的re模块进行正则表达式匹配。
```python
import re
text ='The quick brown fox jumps over the lazy dog'

#查找所有单词
words = re.findall(r'\w+',text)
print("查找所有单词:",words)

#替换
new_text = re.sub(r'fox','cat',text)
print('替换\'fox\'为\'cat\'',new_text)

#分割
parts = re.split(r'\s+',text)
print('使用\'\s\'进行分割',parts)
```
**output**
```plantuml
查找所有单词: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
替换'fox'为'cat' The quick brown cat jumps over the lazy dog
使用'\s'进行分割 ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```
### 7. 性能考虑
在处理大量字符串时，性能是一个重要因素，以下是一些提高字符串操作性能的技巧
1. 使用`join()`而不是`+`进行多个字符串的拼接
2. 对于需要多次修改的字符串，考虑使用`list`存储字符，最后在`join`
3. 使用`str.translate()`进行批量字符替换，比多次调用`replace()`更快
4. 对于大文本处理，考虑使用生成器和迭代器来减少内存使用

> <span style="color: #8968CD">示例：高效的构建大字符串</span>
```python
def build_string(n):
    parts = []
    for i in range(n):
        parts.append(f"Part {i}")
    return ' '.join(parts)

large_string = build_string(10000)
```