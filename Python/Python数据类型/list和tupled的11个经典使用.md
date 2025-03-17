# Python list 和tuple的11个经典使用案例

# 1 . 判断`list`内有无重复元素

可以实现一个判断是否重复的`is_duplicated`方法，使用list封装的`count()`方法，依次判断每个元素`x`在`list`内的出现次数
如果大于`1`，则立即返回`True`，表示有重复的元素，如果完成遍历后，函数没有返回，表示`list`中没有重复的元素。
```python
def is_duplicated(list):
    for item in list:
        #判断item在list中出现的次数
        if list.count(item) >1:
            print(item)
            return True
    return False

if __name__ == '__main__':
    lis = [43,65,76,87,256,121,86,42,12,54,98,95,87,60]
    print(is_duplicated(lis))
```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
87
True
```
</details>

- 方法二： 判断`list`内有无重复元素

`set()`函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集，并集，差集等，上面方法实现不够简洁，借助`set()`判断更方便

```python
def is_duplicated(list):
    for item in list:
        #判断item在list中出现的次数
        if list.count(item) >1:
            print(item)
            return True
    return False


def is_duplicateds(lis):
    return len(lis) != len(set(lis))

if __name__ == '__main__':
    lis = [43,65,76,87,256,121,86,42,12,54,98,95,87,60]
    print(is_duplicated(lis))   #True
    print(is_duplicateds(lis))  #True
```

# 2. 列表的反转
一行代码实现列表的反转，非常简洁，可以解组Python切片`[::-1]`生成逆向索引(`-`表示逆向)，步长为1的切片

```python
def reverse(lst):
    #根据切片一步实现反转列表
    return lst[::-1]

if __name__ == '__main__':
    lis = [1,2,3,4,5,6,7]
    print(f"正向列表: {lis}")
    print(f"反向列表: {reverse(lis)}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

'''plain
正向列表: [1, 2, 3, 4, 5, 6, 7]
反向列表: [7, 6, 5, 4, 3, 2, 1]
'''
</details>

# 3. 找出列表中的所有重复元素

遍历列表，如果出现次数大于 1，且不在返回列表 ret 中，则添加到 ret 中,

```python
def find_duplicated(lis):
    new_lis=[]
    for item in lis:
        if lis.count(item) >1 and item not in new_lis:
            new_lis.append(item)
    return new_lis

if __name__ == "__main__":
    lis = [45,23,445,76,776,34,23,34,54]
    print(f"重复元素: {find_duplicated(lis)}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
重复元素: [23, 34]
```
</details>


# 4. 生成器生成斐波那契数列
斐波那契数列(Fibonacci sequence)；又称黄金分割数列。使用Python的生成器生成斐波那契数列，保证代码简洁的同时还能节省内存

```python
def fibonacci(n):
    a,b= 1,1
    for x in range(n):
        yield a
        a,b = b,a +b

if __name__ == '__main__':
    print(list(fibonacci(11)))
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
</details>

# 5. 跟多参数
带有一个`*`的参数为可变的位置参数，意味着能传入任何多个位置参数
求众多列表中元素最多的一个：

```python
def max_len(*lists):
    #key 函数定义怎么比较大小: lambda的参数v是lists中的一个元素
    return max(*lists,key=lambda v: len(v))

if __name__ == '__main__':
    print(f"最长列表是: {max_len([1,2,3],[4,5,6,7,8],[1,2,3,4,5,6,7,8,9])}")
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
最长列表是: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
</details>

# 6. 求表头
返回列表的第一个元素，注意列表为空时，返回None

```python
def head(lst):
    return lst[0] if len(lst) > 0 else None

if __name__ == '__main__':
    print(f"列表头元素: {head(['h','e','l','l','o'])}")
    print(f"列表头元素: ",head([-9,8,9,10]))
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
列表头元素: h
列表头元素:  -9
```
</details>

# 7. 求表尾
有头就有尾，在Python中，可以使用索引-1来获取列表的最后一个元素

```python
def tail(lstt):
    return lstt[-1] if len(lstt)>0 else None

if __name__ == '__main__':
    print(f"列表头元素: {tail(['h','e','l','l','o'])}")
    print(f"列表头元素: ",tail([-9,8,9,10]))
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
列表头元素: o
列表头元素:  10
```
</details>

# 8. 打印乘法表
`for-for`外层循环一次，`print()`，换行，内层循环一次，打印一个等式。
```python
def mul_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}x{i}={i*j}\t",end='')
        print() #打印换行

if __name__ == '__main__':
    mul_table()
```

<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
1x1=1
1x2=2   2x2=4
1x3=3   2x3=6   3x3=9
1x4=4   2x4=8   3x4=12  4x4=16
1x5=5   2x5=10  3x5=15  4x5=20  5x5=25
1x6=6   2x6=12  3x6=18  4x6=24  5x6=30  6x6=36
1x7=7   2x7=14  3x7=21  4x7=28  5x7=35  6x7=42  7x7=49
1x8=8   2x8=16  3x8=24  4x8=32  5x8=40  6x8=48  7x8=56  8x8=64
1x9=9   2x9=18  3x9=27  4x9=36  5x9=45  6x9=54  7x9=63  8x9=72  9x9=81
```
</details>

# 9. 拼接元素
`zip()`函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

```python
a = [1,11,111]
b = [2,22,222]
print(list(zip(a,b)))

```
<details>
<summary><font style="font-size: initial;color: bisque">output</font> </summary>

```plain
[(1, 2), (11, 22), (111, 222)]
```
</details>