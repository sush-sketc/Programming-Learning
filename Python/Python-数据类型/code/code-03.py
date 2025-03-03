# -*- coding: UTF-8 -*-
'''
@File           : code-03.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/14 8:31 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

text = 'Hello,World,Python'
words = text.split(",")
print(f"使用符号\',\'作为分隔符", words)

text = 'apple,banana,grape,orange'
fruits = text.split(",", 2)
print(f"text字符串使用maxsplit指定分割次数 {fruits}")

test1 = 'apple;banana;grape;orange'
fruits1 = test1.split(";")
print(f"test1原始内容[{test1}],使用\';\'作为分隔符 {fruits1}")
test2 = 'apple-banana-grape-orange'
fruits2 = test2.split("-")
print(f"test2原属内容[{test2}],使用\'-\'作为分隔符 {fruits2}")

text = "Line 1\nLine 2\nLine 3"
lines = text.split("\n")
print(f"test原始内容 [{text}],使用换行符 {lines}")

text = 'apple,,banana,,grape,,orange'
fruits = text.split(",")
print(f"test原始内容 {text},使用\'.\'逗号作为分隔符 {fruits}")

test = 'apple,banana,grape,orange'
fruits = test.split(",", 2)
print(f"test原始内容 {test},指定maxsplit=2 {fruits}")

csv_ling = 'John,Doe,30,New York'
csv_data = csv_ling.split(",")
print(csv_data)
first_name, last_name, age, city = csv_data
print(f"First Name: {first_name},Last Name: {last_name},Age: {age},City: {city}")

url = "https://www.example.com/page?param1=value1&param2=value2"
parts1 = url.split("://")
print(parts1)
parts2 = url.split("://")[1].split("/")
print(parts2)
domain = parts2[0]
print(f"parts2 切片 {parts2[1:]}")
path = "/".join(parts2[1:])
print(f"parts1 {parts2[1]}")
print(f"Domain: {domain}\nPath: {path}")

print("-----------------------------------------------")
test = "Hello, how are you?"
words = test.split()
b = "+".join(words)
print(b)

config_str = 'username=amdin\npassword=secret\ndatabase=appdb'
config_data = {}
for line in config_str.split("\n"):
    key, value = line.split("=")
    config_data[key] = value
print(config_data)

log_entry = "2022-01-15 10:30:15 [INFO] This is an informational message."
log_parts = log_entry.split(" ")
log_data = log_parts[0]
log_time = log_parts[1]
log_level = log_parts[2]
log_message = ".".join(log_parts[3:])
print(f"Date: {log_data},Time: {log_time},Level: {log_level},Message: {log_message}")



data = '10,20,30,40,50'
values = [int(x) for x in data.split(",")]
average = sum(values) / len(values)
print(f"Average: {average}")


file_path = "/path/to/some/file.txt"
parts = file_path.split("/")
print(f"Parts: {parts}")
directory = "/".join(parts[:-1])
print(f"Directory: {directory}")
file_name = parts[-1]
print(f"File_Name: {file_name}")