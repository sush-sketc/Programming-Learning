## Python 字符串格式化
在`Python`中格式化字符串输出用于将变量，表达式和文本组合成一个可读性强的字符串。
1. 百分号格式化: 这是`Python`中最古老的的字符串格式化方式之一，它使用百分号`(%)`作为占位符，允许你插入变量或表达式，这种方式以及存在很长时间，在`Python3`中不推荐使用
2. `str.format()`方法: 这是一种更现代的字符串格式化方式，它使用大括号`{}`作为占位符,支持更多的格式化选项，如对齐，精度和类型转换。
3. `f-字符串`: 这是Python3.6以及更高版本引入的一种新的字符串格式化方式，它使用前缀`f`,允许在大括号`{}`内插入变量或表达式，非常直观和简洁。
4. 字符串模版`(string.Template)`: 字符串模版使用`$`,作为占位符,通过`substitute()方法来替换占位符，适用于一些特定的场景。
5. `join()`方法: `join()` 方法是一种将多个字符串连接成一个字符串的方式，通常用于将列表中的字符串元素合并。

### 1. 百分号格式化
百分号格式化是Python中最老的字符串格式化方式，它使用百分号`(%)`作为占位符
> <span style="color: #8968CD">示例：</span>
```python
name = "Alice"
age =10
print("My name is %s and I am %d years old." % (name,age))
```
>> <span style="color: #FF6EB4"> 百分号格式化的格式说明符指定了要插入的类型变量和格式，以下是一些常用的格式说明符: </span>
+ `%s`: 字符串
+ `%d`: 整数
+ `%f`: 浮点数
> <span style="color: #8968CD">示例：</span>
```python
#使用%号格式化
quantity=3
price = 9.99
total = quantity * price
print("You ordered %d items for a total of $%.2f." % (quantity,total))

# output
# You ordered 3 items for a total of $29.97.
```
### 2. 使用`str.format()`方法
`str.format()`方法是一种更现代和强大的字符串格式化方式，它使用大括号`{}`作为占位符,并允许在大括号内添加格式说明符.
> <span style="color: #8968CD">示例：</span>
```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

# output
# My name is Bob and I am 25 years old.
```
`str.format()`方法支持更多的格式化选项，如对齐、精度和类型转换
> <span style="color: #8968CD">示例：</span>
```python
# 使用str.format()
name = "John"
greeting = "Hello, {}!"
formatted_greeting = greeting.format(name)
print(formatted_greeting)

# 格式化说明符
radius = 5
area = 3.14159 * radius ** 2
print("The area of a circle with radius {} is {:.2f} square units. ".format(radius,area))

# output
# The area of a circle with radius 5 is 78.54 square units.
```

### 3. 使用f-字符串
f-字符串是`Python3.6`更高版本引入的一种新的字符串格式化方法它非常直观和简洁
> <span style="color: #8968CD">示例：</span>
```python
name = "Charlie"
age =15
print(f"My name is {name} and I am {age} years old.")

# f-字符串在字符串前加上 f 前缀，然后使用大括号 {} 插入变量或表达式。这种方式使代码更易读和维护
# output
# My name is Charlie and I am 15 years old.

print("----------------")

# 使用f-字符串
radius = 5
area = 3.14159 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f} square units.")

# output
# f-字符串是一种非常方便的方式，尤其在需要在字符串中嵌入变量时。
# The area of a circle with radius 5 is 78.54 square units.
```

### 4. 使用字符串模版(string.Template)
Python的`string.Template`类提供了另一种格式化字符串的方式,使用`$`作为占位符
> <span style="color: #8968CD">示例：</span>
```python
from string import Template

name = "David"
age = 40
template = Template("My name is $name and I an $age years old.}")
message = template.substitute(name=name, age=age)
print(message)

# 字符串模板使用 $ 符号作为占位符，然后使用 substitute() 方法来替换占位符。
# output 
# My name is David and I an 40 years old.
```
> <span style="color: #8968CD">示例：</span>
```python
from string import Template
# 使用字符串模版
product ="book"
price = 19.99
template = Template("The price of  the $product is $price.")
message = template.substitute(product=product,price=price)
print(message)

# 字符串模板在一些特殊情况下非常有用，例如需要在模板中转义某些字符。
# output
# The price of  the book is 19.22.
```
### 5.使用`join()`方法连接字符串
`join()`方法允许你将多个字符串连接成一个字符串
> <span style="color: #8968CD">示例：</span>
```python
words = ["Hello","World","Python"]
sentence = " ".join(words)
print(sentence)
print(f"sentenct: {' '.join(words)}")
#指定分隔符
print(f"指定分隔符: {','.join(words)}")

# output
# Hello World Python
# sentenct: Hello World Python
# 指定分隔符: Hello,World,Python
```
join()方法非常适用于构建包含多个项目的字符串，例如CSV数据。


###  `%`格式化

+ 语法

```plantuml
"%[(name)][flags][width][.precison]type" %待格式化数据
```

+ 参数
  |格式化符|说明|备注|
  |-------|---|---|
  |`%`|占位符||
  |`(name)`|命名占位符||
  |`(flags)`|可选|`+`: 右对齐,正数加正号,负数加负号;<br>`-`: 左对齐,正数无符号,负数加负号;<br>`空格`: 右对齐(
  默认的对齐方式),正数前加空格,负数前加负号;<br>`0`: 右对齐,以0填充,正数无符号,负数加负号,并将符号放置在0最左侧;
  |`width`|占位符宽度|若指定宽度小于原数据长度则按原长度数据输出;|
  |`,precison`|小数点后保留位数|在字符串中则表示截取/字符串切片|
  |`type`|详见如下||
+ `type`
  |名称|类型|描述|
  |---|----|---|
  |`s`|string|字符串|
  |`d`|decimal integer|十进制数|
  |`i`|integer|用法同`%d`|
  |`u`|unsigned integer|无符号十进制数|
  |`f`|flout|浮点数|默认保留小数点后6位|
  |`F`|Flout|浮点数|默认保留小数点后6位|
  |`e`|exponent|将数字表示位可选计数法(小写e,默认保留小数点后6位)|
  |`E`| Exponent|将数字表示为科学计数法(大写E，默认保留小数点后6位)|
  |`o`|octal|八进制数(即0-7)|
  |`x`|hexdecimal|十六进制数(即0-9a-f)|
  |`X`|Hexdecimal|十六进进制数(0-9A-F)|
  |`g`|general format｜通用格式，详见如下...｜
  |`G`|General format|通用格式，详见如下...|
  |`%c`|character|将十进制数转换为所对应的unicode值|
  |`%r`|representation|调用__repr__魔法方法输出|
  |`%%`|转义%|输出百分号|

### 2. 补充


  
  