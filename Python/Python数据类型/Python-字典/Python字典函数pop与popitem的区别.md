# Python`pop`与`popitem`的区别

## 1. `pop`方法

- 基本用法
  `pop` 方式用于删除字典中指定键的对应值，并返回该删除的值，如果键不存在，可以提供默认值作为参数

```python
my_dict = {'apple': 3, 'banana': 5, 'cherry': 7}
# 删除'banana'键对应的值
value = my_dict.pop('banana')
print(f"Before Delete my_dict = {my_dict},After deletion my_dict = {my_dict},返回删除对应的值: {value}")

# 删除pear键
value = my_dict.pop('pear', "没有")
print(value)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
Before Delete my_dict = {'apple': 3, 'cherry': 7},After deletion my_dict = {'apple': 3, 'cherry': 7},返回删除对应的值: 5
没有
```

</details>

> [!WARNING]
> 异常处理,在删除不存在的键时，如果没有提供默认值，会引发`KeyError`异常，因此，使用`pop`时需要注意异常处理

## 2. `popitem`方法

`popitem`方法用于随机删除字典中的一项(键值对)，并以元组形式返回被删除的键值对，由于字典是无序的，实际上是删除最后一项

```python
my_dict = {'apple': 3, 'banana': 6, 'cherry': 9}
# 随机删除一项
item = my_dict.popitem()
print(item)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
('cherry', 9)
```

</details>

## 3. 空字典处理

在空字典上使用`popitem`会引发`KeyError`异常，因此需要合理处理异常

```python
if my_dict:
    item = my_dict.popitem()
    print(item)
else:
    print("Dictionary is empty")
```

## 4. 区别与场景

- 区别
    - `pop` 是根据指定键删除对应的键值对，并返回该值，它需要提供键，并且如果该键不存在，可以提供默认值。
    - `popitem` 则是随机删除字典中国呢的一项，以元组形式返回被删除的键值对，它不需要提供键，但在空字典上使用时可能引发异常

## 5. 应用场景

- 使用`pop`当需要精确指定要删除的键，并希望在键不存在时有一个默认值
- 使用`popitem`当需要无序精确指定要删除的键，而知识想删除任意一项。

## 5. 扩展

### 1. `pop`方法从字典中提取值并计算

```python
inventory = {'apple': 2, 'banana': 5, 'charry': 3}
# 使用pop方法从库存中取出并计算苹果的数量
apple_cont = inventory.pop('apple', 0)
total_cost = apple_cont * 2.5
print(f"Apple Count: {apple_cont},Total Cost: {total_cost}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font></summary>

```plantuml
Apple Count: 2,Total Cost: 5.0
```

</details>

### 2. 动态更新字典中的值

```python
user_data = {"name": "John", "age": 35, 'poinst': 50}
# 使用pop更新用户的积分并添加新的值
points = user_data.pop('poinst', 0)
user_data['leve'] = 'Silver' if points >= 50 else 'Bronze'
print(user_data)
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
{'name': 'John', 'age': 35, 'leve': 'Silver'}
```

</details>

### 3. `popitem`方法实现一个简单的缓存

```python
def get_data_from_server(key):
    # 模拟从服务器获取数据的操作
    return f"Data for {key}"


from collections import OrderedDict

cache = OrderedDict()


# 使用popitem实现一个简单的缓存，最多存储5个数据
def update_cache(key, data):
    if len(cache) >= 5:
        cache.popitem(last=False)  # 删除最早加入的数据
    cache[key] = data


# 测试缓存更新
for i in range(1, 6):
    key = f"key-{i}"
    data = get_data_from_server(key)
    update_cache(key, data)
    # print(key,data)

# print(cache)
for key, value in cache.items():
    print(f"key=[{key}],value=[{value}]")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plantuml
key=[key-1],value=[Data for key-1]
key=[key-2],value=[Data for key-2]
key=[key-3],value=[Data for key-3]
key=[key-4],value=[Data for key-4]
key=[key-5],value=[Data for key-5]
```

</details>

### 4. 随机删除元素

```python
import random

my_list = [1, 2, 3, 4, 5, 6, 7]
# 使用popitem随机删除列表中的一个元素
while my_list:
    index = random.randint(0, len(my_list) - 1)
    element = my_list.pop(index)
    print(f"Removed: {element},Remaining: {my_list}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font></summary>

```plantuml
Removed: 1,Remaining: [2, 3, 4, 5, 6, 7]
Removed: 3,Remaining: [2, 4, 5, 6, 7]
Removed: 5,Remaining: [2, 4, 6, 7]
Removed: 7,Remaining: [2, 4, 6]
Removed: 2,Remaining: [4, 6]
Removed: 6,Remaining: [4]
Removed: 4,Remaining: []
```

</details>

## 6. 性能考虑

在实际应用中，性能通常时一个关键考虑因素，对于字典操作而言，在选择`pop`还是`popitem`时，性能差异时需要仔细考虑的

- `pop`方法的性能
    - 适用于需要明确指定要删除的键的场景，
    - 在具体指定键的情况下，`pop`方法的性能时非常高的，因为它直接通过键来进行删除操作。
    - 不会涉及字典的遍历或随机访问，因此在大多数情况下性能较好。
- `popitem`方法的性能
    - 适用于无序精确指定键，而是虚妄随机删除的一项的场景.
    - `popitem`方法的性能通常比`pop`更为优越，因为它不需要指定键，可以更加均匀地分配删除操作。
    - 但在空字典上的性能性对较差，因为它需要检查字典是否为空

## 7. 综合考虑

- 在具体应用中可以根据需求综合考虑字典的大小，删除操作的频率以及是否需要精确指定键等因素。
- 如果字典规模较大且删除操作频繁，`popitem`可能更适合，因为它有助于更均匀地分布删除压力。
- 如果需要明确指定要删除的键，或者字典规模较小，`pop`是一个更直观，高效的选择。


- 在具体应用中，可以根据需求