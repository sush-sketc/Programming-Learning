# Python 集合模块，使用集合数据处理数据集合

Python中提供了非常丰富的容器型数据类型，较为熟悉的有 `list`,`tuple`,`set`,`dict`等

# 从字典中取最大
假设字典对象对应的变量名为`my_list` 
+ 取出最大值
```python
my_dict = {"name":20,"age":30}
print(max(my_dict.values()),tuple(my_dict))
```