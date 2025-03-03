## Python 字符串常用方法

### 1. `Slicing`
`Slicing` 切片，按照一定条件从列表或元组中取出部分元素(比如特定范围,索引,分割值)
```python
s= '   Hello   '
s = s[:]
print(s)
```

### 2. `strip()`
`strip()`方法用于移除字符串头尾指定的字符，(默认为空格或换行符)或字符序列
```python
s = '   hello    '.strip()
print(s)

s = '####hello****'.strip()
print(s)
```
**output**
```plantuml
hello
####hello****
```
>> 在使用`strip()`方法时，默认去除空格或换行符，所以`#`好并没有去除。可以给你`strip()`方法添加指定字符
```python
s = ' \n \t hello\n'.strip("\n")
print(s)

s= '####hello$$$$$'.strip('#')
print(s)
```
**outout**
```plantuml
 	 hello
hello$$$$$
```
> <span style="color: #8968CD">示例：</span>
```python
s ='www.baidu.com'.strip('cmow.')
print(s)    # output: bamidu
```

### 3. `lstrip()`
移除字符串左侧指定的字符(默认为空格或换行符)或字符序列
```python
#移除左侧空格(右侧空格是存在的)
s ='      hello     '.lstrip()
print(s)   #output: hello

#移除左侧所有包含在字符集中的字符串
s='Arthur: three!'.lstrip('Arthur: ')
print(s)    #outout: ee!
```
### 4. `rstrip()`
移除字符串右侧指定的字符(默认为空格和换行符)或字符序列
```python
s = '    hello     '.rstrip()
print(s)    #outout:   hello  
```
### 5.  `removeprefix()`
Python3.9中移除前缀的函数
```python
#Python 3.9
s ='Arthur: three!'.removeprefix('Arthur: ')
print(s)    #output: three!
```
>> 和`strip()`相比，并不会吧字符集中的字符串进行逐个匹配
### 6. `removesuffix()`
Python3.9中移除后缀的函数
```python
s ='HelloPython'.removesuffix('Python')
print(s)    #output: Hello
```
