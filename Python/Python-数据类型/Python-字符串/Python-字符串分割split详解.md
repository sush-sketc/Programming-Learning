## Python 中的字符串分割函数`split()` 详解

在`Python`处理字符串是一项常见的任务，字符串分割是其中的一个常见操作，而`Python`提供了强大的`split()`函数，用于将字符串拆分成多个部分。
### 1. 基本用法
`split()`函数是`Python`字符串的内置方法，用于将一个字符串按照指定的分隔符拆分成多个子字符串，并将这些子字符串存储在列表中。函数的基本语法如下：
```plantuml
str.split([separator[,maxsplit]])
```
+ `sepatator` (可选参数): 指定用于分隔符，默认为所有空白字符(包括空格，制表符，换行符等)可以是字符串或字符
+ `maxsplit`  (可选参数): 指定最大分割次数，如果提供了此参数，函数将执行最多`maxsplit`次分割。

> <span style="color: #8968CD">示例：使用`split()`函数将字符串分割成列表</span>
```python
text ='Hello,World,Python'
words=text.split(",")
print(f"使用符号\',\'作为分隔符",words)
```
> output
```plantuml
使用符号','作为分隔符 ['Hello', 'World', 'Python']
```
>>  <span style="color: #FF6EB4"> 上述代码中，字符串中的多个连续空白字符被视为一个分隔符。</span>

### 2. 使用`maxsplit`参数
可以使用`maxsplit`参数来限制分割的次数，这对于只想分割字符串的前几部分很有用。
> <span style="color: #8968CD">示例：使用`split()`函数的`maxsplit`参数</span>
```python
text='apple,banana,grape,orange'
fruits = text.split(",",2)
print(f"text字符串使用maxsplit指定分割次数 {fruits}")
```
> output
```plantuml
text字符串使用maxsplit指定分割次数 ['apple', 'banana', 'grape,orange']
```
>> <span style="color: #FF6EB4"> 上述代码中使用`maxsplit=2`,将字符串`text`最多分割为两部分，结果列表中共有三个元素 </span>

### 3. 使用自定义分隔符
除了`,`作为分隔符，`split()`函数还可以使用任何其他字符或字符串作为分隔符。
> <span style="color: #8968CD">示例：自定义分隔符 </span>
```python
test1 ='apple;banana;grape;orange'
fruits1 = test1.split(";")
print(f"test1原始内容[{test1}],使用\';\'作为分隔符 {fruits1}")
test2 ='apple-banana-grape-orange'
fruits2 = test2.split("-")
print(f"test2原属内容[{test2}],使用\'-\'作为分隔符 {fruits2}")
```
```python
test ="Hello, how are you?"
words = test.split()
b = "+".join(words)
print(b)
```
> outputs
```plantuml
test1原始内容[apple;banana;grape;orange],使用';'作为分隔符 ['apple', 'banana', 'grape', 'orange']
test2原属内容[apple-banana-grape-orange],使用'-'作为分隔符 ['apple', 'banana', 'grape', 'orange']
----------------------
Hello,+how+are+you?
```
### 4. 分割换行符
处理文本文件时，需要根据换行符来分割文本的不同行，`split()`函数可以轻松因为这中情况。
> <span style="color: #8968CD">示例：使用换行符分割文本 </span>
```python
text="Line 1\nLine 2\nLine 3"
lines = text.split("\n")
print(f"test原始内容 [{text}],使用换行符 {lines}")
```
> output
```plantuml
test原始内容 [Line 1
Line 2
Line 3],使用换行符 ['Line 1', 'Line 2', 'Line 3']
```
### 5. 处理连续分隔符
字符串中可能包含连续的分隔符，默认情况下，`split()`函数会将连续的分隔符视为一个分隔符并忽略总监的空字符串
> <span style="color: #8968CD">示例: 处理连续分隔符 </span>
```python
text ='apple,,banana,,grape,,orange'
fruits = text.split(",")
print(f"test原始内容 {text},使用\'.\'逗号作为分隔符 {fruits}")
```
> output
```plantuml
test原始内容 apple,,banana,,grape,,orange,使用'.'逗号作为分隔符 ['apple', '', 'banana', '', 'grape', '', 'orange']
```
>> <span style="color: #FF6EB4"> 上述代码中由于字符串存在连续的逗号`,,`,`split()`函数将视为一个分隔符，并在结果列表中包含了空字符串 </span>

### 6. 分割指定次数
如果只希望分割字符串的前几部分，可以使用`maxsplit`参数来限制分割次数
```python
test='apple,banana,grape,orange'
fruits = test.split(",",2)
print(f"test原始内容 {test},指定maxsplit=2 {fruits}")
```
> output
```plantuml
test原始内容 apple,banana,grape,orange,指定maxsplit=2 ['apple', 'banana', 'grape,orange']
```
>> <span style="color:  #FF6EB4"> 上述代码中使用`maxsplit=2`，将字符串`text`最多分割为两部分，结果列表中有三个元素 </span>

### <span style="color: #FF3030"> **注意事项** </span>
在使用`split()`函数时，需要注意以下几个方面：
1. 分隔符可以是任何字符串，包括多个字符的字符串。
2. 如果不提供分隔符，则默认使用所有空白字符，包括空格，制表符，换行符等。
3. 默认情况下，连续的分隔符会被视为一个分隔符，并且中间的空字符串会包含在结果列表中。
4. 使用`maxsplit`参数可以限制分割的次数，但不能指定从字符串的末尾开始分割。

### 7. 示例应用场景
> 7.1. `CSV`文件解析
`CSV`文件通常由逗号`,`分隔的值组成，使用`split()`函数可以轻松解析`CSV`行并提取数据
```python
csv_ling='John,Doe,30,New York'
csv_data= csv_ling.split(",")
print(csv_data)
first_name ,last_name,age,city = csv_data
print(f"First Name: {first_name},Last Name: {last_name},Age: {age},City: {city}")
```
> output
```plantuml
['John', 'Doe', '30', 'New York']
First Name: John,Last Name: Doe,Age: 30,City: New York
```
> 7.2. `URL`解析
从`URL`中提取域名，路径，查询参数等信息
```python
url="https://www.example.com/page?param1=value1&param2=value2"
parts = url.split("://")[1].split("/")
domain = parts[0]
print(f"parts切片输出 pa")
path = "/".join(parts[1:])
print(f"Domain: {domain},Path: {path}")
```
> 7.3. `配置文件解析`
解析配置文件中键值对
```python
config_str = 'username=amdin\npassword=secret\ndatabase=appdb'
config_data = {}
for line in config_str.split("\n"):
    key, value = line.split("=")
config_data[key] = value
print(config_data)
```
> output 
```plantuml
{'username': 'amdin', 'password': 'secret', 'database': 'appdb'}
```
> 7.4. 日志文件处理
从日志文件中提取日期，时间，日志级别信息。
```python
log_entry = "2022-01-15 10:30:15 [INFO] This is an informational message."
log_parts = log_entry.split(" ")
log_data = log_parts[0]
log_time = log_parts[1]
log_level = log_parts[2]
log_message = ".".join(log_parts[3])
print(f"Date: {log_data},Time: {log_time},Level: {log_level},Message: {log_message}")
```
> output
```plantuml
Date: 2022-01-15,Time: 10:30:15,Level: [INFO],Message: This.is.an.informational.message.
```
> 7.5. 数据清洗和处理
在数据处理中，分割字符串是一种常见的方式，特别是在清洗和准备数据时
```python
data = '10,20,30,40,50'
values = [int(x) for x in data.split(",")]
average = sum(values) / len(values)
print(f"Average: {average}")
```
> output
```plantuml
Average: 30.0
```

> 7.6. 文件路径解析
从文件路径中提取目录和文件名
```python
file_path = "/path/to/some/file.txt"
parts = file_path.split("/")
print(f"Parts: {parts}")
directory = "/".join(parts[:-1])
print(f"Directory: {directory}")
file_name = parts[-1]
print(f"File_Name: {file_name}")
```