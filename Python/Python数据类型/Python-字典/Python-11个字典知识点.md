# Python 11个字典知识点

## 1. 字典是否时无序的

关于这个概念，在Python2.7中，字典是无序结构，字典项目的顺序是混乱的，这意味这项目的顺序是确定性和可重复的,在Python3.5中，字典仍然是无序的，但这次是随机的数据结构，
这意味这每次重新运行字典时们都会得到不同的项目顺序。在Python3.6及更高版本中，字典时有序的数据结构，这意味着它们保持元素的顺序与它们被引入时的顺序相同

## 2. 键值互换

假设有一本字典，由于某种原因需要将键转换为值，值转换为键，因该怎么做？

```python
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```python
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
```

</details>

## 3. 依据某种条件，过滤字典

有时候，需要根据某种条件来过滤子弟啊你，那么配合`if`条件语句，是一个很好的选择

```python
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 3:
        new_dict[key] = value
print(new_dict)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'one': 1, 'two': 2, 'thee': 3}
```
</details>

## 4. 利用字典中的值做计算
在Python中遍历字典时，需要进行一些计算也是很常见的，假设已将公司销售额的数据存储在字典中，想再想知道一年的总收入。
```python
incomes = {'apple':5600.00,'orange':3500.00,'banana':5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value
print(total_income)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
14100.0
```
</details>

## 5. 字典推导式
字典推导式，是一个和列表推导式一样，具有很强大功能的知识点，假如，假设有两个数据列表，需要根据它们创建i一个新字典。
```python
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
```
</details>

## 6. 利用字典推导式，实现键值转换
可以发现，使用字典推导式，时一个更简单，高效的操作
```python
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}
```
</details>

## 7. 利用字典推导式，过滤字典
```python
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'one': 1, 'two': 2}
```
</details>

## 8. 利用字典推导式，做一些计算
```python
incomes = {'apple':5600.00,'orange':4500.00,'banana':4000}
total_icome = sum(value for value in incomes.values())
total_icome_new = sum(incomes.values())
print(total_icome,total_icome_new)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
14100.0 14100.0
```
</details>

## 9. 字典排序
从Python 3.6开始，字典是有序的数据结构，因此如果使用Python 3.6(更高版本),能够通过使用`sorted()`并借助字典理解对任何字典的键，进行排序

```python
incoms = {'apple':5600.00,'orange':4500.00,'banana':4000}
sorted_incom = {k: incoms[k] for k in sorted(incoms)}
print(sorted_incom)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'apple': 5600.0, 'banana': 4000, 'orange': 4500.0}
```
</details>

## 10. 内置函数，与字典配合使用
Python提供了一些内置函数，这些函数在处理集合(如字典)时可能会很有用
- `map()`函数
假设有一个包含一堆产品价格的字典，并且需要对它们应用折扣
```python
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount,prices.items()))
print(new_prices)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'apple': 0.38, 'orange': 0.33, 'banana': 0.24}
```
</details>

- `filter()`函数
假设要知道单价低于0.40的产品
```python
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def has_low_price(price):
    return prices[price] < 0.4


low_price = list(filter(has_low_price, prices.keys()))
print(low_price)
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
['orange', 'banana']
```
</details>

## 11. 字典解包运算符
这是很多人不清楚的概念，Python3.5之后的一个新特性。可以使用字典解包运算符`(**)`将两个字典合并为一个新字典。
```python
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': 0.25}
print({**vegetable_prices, **fruit_prices})
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'pepper': 0.25, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
```

</details>