# -*- coding: UTF-8 -*-
'''
@File           : code-01.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/12 6:24 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

# 高效使用可变类型 - 字典
word_count = {}
text = "apple orange banana apple oranage"
words = text.split()
for word in words:
    # 使用setdefault一行代码实现计数
    word_count[word] = word_count.setdefault(word, 0) + 1
# 输出：
print(word_count)

print("--------深拷贝和浅拷贝----------")

import copy

# 深拷贝
original_list = [1, [2, 3], 4]
deep_copy_list = copy.deepcopy(original_list)
deep_copy_list[1][0] = 99
# 输出
print(original_list)
print(deep_copy_list)

print("--------字符串拼接----------")
# 使用+运算符
first_name = 'Johb'
last_name = 'Doe'
full_name = first_name + '' + last_name
print(full_name)

# 使用+=运算符
greeting = 'Hello'
greeting += 'World'

# 使用join()方法
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)

# 使用格式化字符串
name = 'Alice'
age = 18
info = f'{name} is {age}'
print(info)

# 使用str,format()方法
template = '{} is {}'
info = template.format(name, age)
print(info)

print("--------字符串索引和切片----------")

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

print("--------大小写转换----------")
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

print("--------字符串查找----------")

s = 'Python is amazing and Python is powerful'

# 查找
print(s.find('Python'))
print('从索引10开始查找：', s.find('Python', 10))
print(f'从右侧开始查找: ', s.rfind('Python'))
try:
    print(s.index('Java'))
except ValueError:
    print("'Jave' not found in the string")

print('统计\'Python\'总共出现几次', s.count('Python'))

# 替换
print('Python 替换为 Java(全部替换)', s.replace('Python', 'Java'))
print('Pythaon 替换为 Java(替换第一次出现的)', s.replace('Python', 'Java', 1))

print("--------分割和连接----------")

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

print("--------去除空白和其他字符----------")

s = '    Hello, World!   '

print('去除全部空白字符：', s.strip())
print('去除开头空白字符:', s.lstrip())
print('去除结尾空白字符:', s.rstrip())

# 去除指定字符
ss = '----Ptyhon...---'
print('去除所有以\'.\'的字符', ss.strip('.'))
print('去除开头以\'.\'的字符', ss.lstrip('.'))
print('去除结尾以\'.\'的字符', ss.rstrip('.'))

print("--------填充和对齐----------")

s = 'Python'
print('字符串结尾添加空白字符:', s.ljust(10))
print('字符串开头添加空白字符:', s.rjust(10))
print('字符串前后添加空白字符:', s.center(10))

# 使用指定字符填充
print('使用\'-\'填充10个', s.ljust(10, '-'))
print('使用\'-\'填充10个', s.ljust(10, '*'))
print('使用\'-\'填充10个', s.ljust(10, '='))
intzfi = '43'
print('数字字符串左边填充5个0', intzfi.zfill(5))

print("--------字符串格式化----------")

name = 'Alice'
age = 70
print('My name is %s and I am %d years old.' % (name, age))

# 使用字典
print('%(name)s is %(age)d years old. ' % {'name': 'Bob', 'age': 58})

print("--------格式化选项----------")

name = 'Shanghai'
age = 710

print('Name is {} and I am {} years old.'.format(name, age))
# 使用索引
print('The {1} {0} {2}'.format('brown', 'quick', 'fox'))

# 使用命名参数
print('The {adj} {noun}.'.format(adj='北京', noun='上海'))

# 格式化选项
pi = 3.14159
print('Pi is approximately {:.2f}'.format(pi))

print("--------字符串的成员资格测试----------")
text = 'Python is amazing'
print('Python' in text)  # True
print('Java' not in text)  # True

filename = 'document.txt'
print(filename.startswith('doc'))  # True
print(filename.endswith('.txt'))  # True

print("--------字符串的转换和编码----------")
# 转换为字节
s = 'Hello,World'
b = s.encode('utf-8')
print('转换为字节', b)

# 从字节转换为字符串
s2 = b.decode('utf-8')
print('字节转换为字符串', s2)

# 处理不同编码
s_unicode = '您好，世界！'
b_gbk = s_unicode.encode('gbk')
s_from_gbk = b_gbk.decode('gbk')
print('处理不同编码:', s_from_gbk)

print("--------正则表达式----------")

import re

text = 'The quick brown fox jumps over the lazy dog'

# 查找所有单词
words = re.findall(r'\w+', text)
print("查找所有单词:", words)

# 替换
new_text = re.sub(r'fox', 'cat', text)
print('替换\'fox\'为\'cat\'', new_text)

# 分割
parts = re.split(r'\s+', text)
print('使用\'\s\'进行分割', parts)
