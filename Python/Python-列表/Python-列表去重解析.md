## Python列表去重最全方法解析与实战案例

>[!TIP]
> [参考代码](./code/code-05.py

在Python中，列表时非常常用的数据结构之一
### 1. 使用集合(set)
集合`(set)`是一种无序且不重复的集合类型，因此利用集合去重是最简单的方法之一
```python
def remove_duplicates(lst):
    """
    使用结合去重
    """
    return list(set(lst))
#测试代码
original_list = [1,2,2,3,3,4,5,6,6,0,0]
deduplicated = remove_duplicates(original_list)
print("原始列表:",original_list)
print("去重后列表:",deduplicated)
```
<details>
<summary><font style="font-size: larger;color: bisque">output</font> </summary>

```plantuml
原始列表: [1, 2, 2, 3, 3, 4, 5, 6, 6, 0, 0]
去重后列表: [0, 1, 2, 3, 4, 5, 6]
```
</details>

>[!NOTE]
> 代码解析
> - 定义函数：定义`remove_duplicates`函数，接收一个列表作为参数。
> - 转换集合：将列表转换为集合，去除重复元素。
> - 转换回列表：将集合转换为列表并返回

>[!WARNING]
> 结合是无序的，因此这种方法无法保证去重后的元素顺序与原始列表一致

### 2. 使用`collections.OrderedDict
`OrderedDice`是`collections`模块中的一个子类，它可以保持插入元素的顺序，利用`OrderdDict`可以实现去重且保持顺序

