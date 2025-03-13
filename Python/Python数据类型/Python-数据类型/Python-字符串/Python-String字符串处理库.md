## Python String字符串处理库

字符串作为一种常见的类型，在日常中面临各式各样的的字符串处理问题，字符串基本需求：`find()`,`index()`,`count()`

### 1. 查找

#### 1.1. `find()`

`find()`函数用于检测字符串是否包含特定字符，如果包含，则返回开始的索引，否则，返回`-1`

```python
str = 'Welcome to DataScience'
print('查找字符\'Da\'是否存在于str中', str.find('Da'))
print('查找字符\'wc\'是否存在于str中', str.find('wc'))
```

+ **output**

```plantuml
查找字符'Da'是否存在于str中 11
查找字符'wc'是否存在于str中 -1
```

#### 1.2. `index()`

检查字符串是否包含指定字符，如果包含，则返回开始的索引值，否则，提示错误

```python
str = 'Welcome to DateScience'
print(f'检查字符串str中是否包含\'come\'字符 返回索引起始 index: %d' % str.index('come'))
print(f'检查字符串\'str\'中是否包含\'Date\'字符，返回索引起始 index: %d' % str.index('Date'))
print(f'检查字符串\'str\'中是否包含\'Java\'字符，返回索引起始 index: %s' % str.index('Java'))
```

+ **output**

```plantuml
检查字符串str中是否包含'come'字符 返回索引起始 index: 3
检查字符串'str'中是否包含'Date'字符，返回索引起始 index: 11
Traceback (most recent call last):
  File "/Users/ssh/workspace/python-workspaces/basic_learning/Python-数据类型/code/code-02.py", line 36, in <module>
    print(f'检查字符串\'str\'中是否包含\'Java\'字符，返回索引起始 index: %s' % str.index('Java'))
ValueError: substring not found
```

> > 第三个`print`报错`ValueError: substring not found`是因为`str`字符串中不包含`Java`字符串

#### 1.3. `count()`

返回`str`在`string`中指定索引范围内`[start,end]`出现的次数

```python
str = 'Welcome to DateScience'
print('字符\'e\'出现次数 count: %d' % str.count('e'))
print('字符\'Da\'出现次数 count: %d' % str.count('Da'))
print('字符\'Ja\'出现次数 count: %s' % str.count('Ja'))
```

### 2. 修改

常见的用于字符串修改函数有:

#### 2.1. `replace()`

+ 吧字符串中`old(旧字符串)`替换成`new(新字符串)`,如果指定第三个参数`max`,则替换不超过`max`次，该函数
+ 语法如下
  `str.replace(old,new[,max])`
+ 参数如下
    + old -- 将被替换的子字符串
    + new -- 新字符串，用于替换old子字符串
    + max -- 可选字符串, 替换不超过 max 次

```python
s = 'Welcome to Data Science'
print(f'替换\'s\'字符串中\'Data\'为\'data\': {s.replace("Data", "data")}')
print(f'替换\'s\'字符串中\'e\'为\'E\'并且不超过2次: {s.replace("e", "E", 2)}')
```

+ **output**

```plantuml
替换'str'字符串中'Data'为'data': Welcome to data Science
替换's'字符串中'e'为'E'并且不超过3次: WElcomE to Data Science
```

#### 2.2. `split()`

+ 如果`maxsplit`有指定值，则仅为分割,`maxsplit`个子字符串；
+ 格式
    + 语法格式
      `str.split('分界符',maxsplit)`
    + 参数
        + `maxsplit`默认值为`-1`表示根据定界符分割所有能分割的
        + 返回值为列表

```python
str = 'Welcome to Data Science'
print(f'不使用参数默认输出: {str.split()}')
print(f"用空格作为分界符: {str.split(' ')}")
print(f"使用\'e\'作为分界符，并且maxsplit为2: {str.split('e', 2)}")
```

+ **output**
```plantuml
不使用参数默认输出: ['Welcome', 'to', 'Data', 'Science']
用空格作为分界符: ['Welcome', 'to', 'Data', 'Science']
使用'e'作为分界符，并且maxsplit为2(分为3组): ['W', 'lcom', ' to Data Science']
```

#### 2.3. `capitilize()`

+ 将字符串的首字母大写，其余字母全部小写
+ 语法
    + `str.capitilize()`
+ 无参数

```python
str = 'welcome to Data Science'
print(str.capitalize())
# output: Welcome to data science
```

#### 2.4. `join()`

+ 用于将序列中的元素以指定的字符连接生成一个新的字符串
+ 语法如下：
    + `str.join(sequence)`
    + `sequence` -- 要连接的元素列表

```python
seq = 'Welcome to Data Science'
str = ' '
strs = '-'
print(f"源字符串:'{seq}'\n使用空格作为连接符: {str.join(seq)}")
print(f"使用\'-\'作为连接符: {strs.join(seq)}")
```
+ **output**
```plantuml
源字符串:'Welcome to Data Science'
使用空格作为连接符: W e l c o m e   t o   D a t a   S c i e n c e
使用'-'作为连接符: W-e-l-c-o-m-e- -t-o- -D-a-t-a- -S-c-i-e-n-c-e
```
#### 2.5. `title()`
+ 将字符串中的所有单词的首字母大写，其余字母全部小写
+ 需要注意的是，这里单词的区分是以任何标点符号区分的，即`,`标点符号的前后都是一个独立的单词，字符串最后一个标点符除外
+ 语法
  + `str.title()`
+ 无参数
```python
str ='welcome to data science'
print(f"所有单词首字母大写: {str.title()}")
str1 = 'welcome to data-science.'
print(f"添加标点符号: {str1.title()}")
```
+  **output**
```plantuml
所有单词首字母大写: Welcome To Data Science
添加标点符号: Welcome To Data-Science.
```
#### 2.6. `loewr()`
+ 将字符串的所有字母转换为小写
+ 语法
  + `str.lower()`
  + 无参数
```python
str = 'WELCOME TO DATA SCIENCE'
print(f"将\'{str}\'所有字符串转换为小写: {str.lower()}")
```
+ **output**
```plantuml
将'WELCOME TO DATA SCIENCE'所有字符串转换为小写: welcome to data science
```
#### 2.7. `upper()`
+ 将字符串的所有字母转换为大写;
+ 语法
  + `str.upper()`
  + 无参数
```python
str = 'welcome to data science'
print(f"将\'{str}\'字符串中的字母转换为大写: {str.upper()}")
```
+ **output**
```plantuml
将'welcome to data science'字符串中的字母转换为大写: WELCOME TO DATA SCIENCE
```
#### 2.8. `ljust()`
+ 将字符串左对齐，并使用空格填充至指定长度`len`
+ 语法
  + `str.ljust(len)`
```python
str = 'Welcome to data science'
print('str源长度为%d' % len(str))
print('str 处理后的长度为: %d' % (len(str.ljust(30))))
print(len(str.ljust(40)))
```
+ **output**
```plantuml
str源长度为23
str 处理后的长度为: 30
40
```
#### 2.9. `rjust()`
+ 将字符串右对齐，并使用空格填充指定长度`len`
+ 语法
  + `str.rjust(len)`
```python
str ='Welcome to data science'
print(f'{str}的原始长度为 %d' % len(str))
print(f'{str}处理后的长度为 %d' %len(str.rjust(30)))
print(str.rjust(30))
```
+ **output**
```plantuml
Welcome to data science的原始长度为 23
Welcome to data science处理后的长度为 30
       Welcome to data science
```
#### 2.9. `center()`
+ 将字符串居中，并使用空格填充值指定长度`len`
+ 语法：
  + `str.center(len)`
```python
str = 'Welcome to Data science'
print(f'{str}的原始长度为 %d' % len(str))
print(f'{str} 处理后的长度为 %d' % len(str.center(30)))
```
+ **output**
```plantuml
'Welcome to Data science'的原始长度为 23
'Welcome to Data science' 处理后的长度为 30
```

### 3. 删除

#### 3.1. `lstrip()`
+ 去掉字符串左边的空白字符；
+ 语法
  + `str.lstrip()`
```python
str ='    Welcome to Data Science'
print(f"str原始内容[{str}]，长度为：{len(str)}")
new_str = str.lstrip()
print(f'str去掉左边空格后，内容为[{new_str}],长度为[{len(new_str)}]')
```
+ **output**
```plantuml
str原始内容[    Welcome to Data Science]，长度为：27
str去掉左边空格后，内容为[Welcome to Data Science],长度为[23]
```
#### 3.2. `rstrip()`
+ 去掉字符串右边的空白字符；
+ 语法
  + `str.rstrip()`
```python
str = 'Welcome to Data Science      '
print(f"str原始内容[{str}],长度为[{len(str)}]")
new_str = str.rstrip()
print(f"str去掉右边空格后,内容为[{new_str}],长度为[{len(new_str)}]")
```
+ **output**
```plantuml
str原始内容[Welcome to Data Science      ],长度为[29]
str去掉右边空格后,内容为[Welcome to Data Science],长度为[23]
```
#### 3.3. `strip()`
+ 去掉字符串两边的空白字符
+ 语法
  + `str,strip()`
```python
str ='    Welcome to Data Science    '
print(f"str原始内容[{str}],长度为[{len(str)}]")
new_str = str.strip()
print(f"str去掉两边空白字符后，内容为[{new_str}],长度为[{len(new_str)}]")
```
+ **output**
```plantuml
str原始内容[    Welcome to Data Science    ],长度为[31]
str去掉两边空白字符后，内容为[Welcome to Data Science],长度为[23]
```

### 4. 判断

#### 4.1. `startswith()`
+ 检查字符串`str`是否以字符`str1`开头，若是，则返回`True`,否则，返回`False`
+ 语法
  + `str.startswith()`
```python
str='Welcome to Data Science'
print(f"str原始内容为[{str}],判断是否以字符大写[\'W\']开头",str.startswith('W'))
print(f"str原始内容为[{str}],判断是否以字符小写[\'W\']开头",str.startswith('w'))
```
+ **output**
```plantuml
str原始内容为[Welcome to Data Science],判断是否以字符大写['W']开头 True
str原始内容为[Welcome to Data Science],判断是否以字符小写['W']开头 False
```
#### 4.2. `endswith()`
+ 检查字符串`str`是否以字符`str1`结尾，若是，返回`True`,否则,返回`False`
+ 语法
  + `str.endswith()`
```python
str ='Welcome to Data Science'
print(f"str原始内容为[{str}],判断是否以字符大写[\'E\']结尾",str.endswith('E'))
print(f"str原始内容为[{str}],判断是否以字符小写[\'e\']结尾",str.endswith('e'))
```
+ **output**
```plantuml
str原始内容为[Welcome to Data Science],判断是否以字符大写['E']结尾 False
str原始内容为[Welcome to Data Science],判断是否以字符小写['e']结尾 True
```
#### 4.3. `isdigit()`
+ 如果字符串`str`中只包含数字，则返回`True`，否则返回`False`
+ 语法
  + `str.isdigit()`
```python
str ='Welcome to Data Science'
print(f"str原始内容为[{str}],是否只包含数字 {str.isdigit()}")
int_str ='1234'
print(f"int_str原始内容为[{int_str}],是否只包含数字 {int_str.isdigit()}")
```
+ **output**
```plantuml
str原始内容为[Welcome to Data Science],是否只包含数字 False
int_str原始内容为[1234],是否只包含数字 True
```
#### 4.4. `isalnum()`
+ 检测字符串中是否由数字和字母组成
+ 语法
  + `str.isalnum()`
```python
str1='Welcome to Data Science'
print(f"str1原始内容[{str1}],是否由数字字母组成 {str1.isalnum()}")
str2='123adfc'
print(f"str2原始内容{str2},是否由数字字母组成 {str2.isalnum()}")
```
+ **output**
```plantuml
str1原始内容[Welcome to Data Science],是否由数字字母组成 False
str2原始内容123adfc,是否由数字字母组成 True
```
#### 4.5 `isspace()`
+ 如果字符串`str`中只包含空格，则返回`True`,否则返回`False`
+ 语法
  + `str.issoace()`
```python
str1 = 'Welcome to Data Science'
print(f"str原始内容[{str}],是否包含空格 [{str.isspace()}]")
str2 = ' '
print(f"str2原始内容[{str2}],是否包含空格 [{str2.isspace()}]")
```
+ **output**
```plantuml
str原始内容[Welcome to Data Science],是否包含空格 [False]
str2原始内容[ ],是否包含空格 [True]
```