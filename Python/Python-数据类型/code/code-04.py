# -*- coding: UTF-8 -*-
'''
@File           : code-04.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/17 2:18 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

quantity = 3
price = 9.99
total = quantity * price
print("You ordered %d items for a total of $%.2f." % (quantity, total))

name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
radius = 5
area = 3.14159 * radius ** 2
print("The area of a circle with radius {} is {:.2f} square units. ".format(radius, area))

radius = 5
area = 3.14159 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f} square units.")

from string import Template

name = "David"
age = 40
template = Template("My name is $name and I an $age years old.")
message = template.substitute(name=name, age=age)
print(message)

print("------------------")
from string import Template

product = "book"
price = 19.22
template = Template("The price of  the $product is $price.")
message = template.substitute(product=product, price=price)
print(message)

words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)
print(f"sentenct: {' '.join(words)}")
print(f"指定分隔符: {','.join(words)}")
