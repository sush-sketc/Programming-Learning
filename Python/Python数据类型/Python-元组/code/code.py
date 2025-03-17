
"""
+ 连接两个元素
"""
def_tuple1=("name","beijing")
def_tuple2=("name","shanghai")
relust = def_tuple1+def_tuple2
print(f'使用+符号连接两个元组: {relust}')


"""
* 重复元素
"""
def_tuple1 = ("上海","浦东新区")
print(f"重复元素: {def_tuple1 *3}")

"""
in,not in 判断元素
"""
def_tuple1 = ("apple","banana","orange")
print(f"in {"apple" in def_tuple1}")
print(f"in {"beijing" in def_tuple1}")
print(f"in {"orange" in def_tuple1}")
print(f"not in {"orange" not in def_tuple1}")
print(f"not in {"beijing" not in def_tuple1}")

"""
[:]对元组进行切片
"""
def_tuple1 = ("北京","上海","江苏","南京","兰州")
#截取1-3的元素，（不包含第3个元素）
print(f"截取1-3的元素(不包含第3个元素): {def_tuple1[:2]}")
#指定步长，截取列表
print(f"指定步长为2,每两个元素取一个元素: {def_tuple1[0::2]}")
#反转元组
print(f"反转元组: {def_tuple1[::-1]}")

"""
判断list列表中有无重复元素
"""
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


"""
列表的反转
"""
def reverse(lst):
    #根据切片一步实现反转列表
    return lst[::-1]

if __name__ == '__main__':
    lis = [1,2,3,4,5,6,7]
    print(f"正向列表: {lis}")
    print(f"反向列表: {reverse(lis)}")


"""
找出列表中的所有重复元素
"""
def find_duplicated(lis):
    new_lis=[]
    for item in lis:
        if lis.count(item) >1 and item not in new_lis:
            new_lis.append(item)
    return new_lis

if __name__ == "__main__":
    lis = [45,23,445,76,776,34,23,34,54]
    print(f"重复元素: {find_duplicated(lis)}")


"""
生成器生成斐波那契数列
"""
def fibonacci(n):
    a,b= 1,1
    for x in range(n):
        yield a
        a,b = b,a +b

if __name__ == '__main__':
    print(list(fibonacci(11)))

"""
位置参数 求众多列表中元素最多的一个
"""
def max_len(*lists):
    #key 函数定义怎么比较大小: lambda的参数v是lists中的一个元素
    return max(*lists,key=lambda v: len(v))

if __name__ == '__main__':
    print(f"最长列表是: {max_len([1,2,3],[4,5,6,7,8],[1,2,3,4,5,6,7,8,9])}")

"""
求表头
"""
def head(lst):
    return lst[0] if len(lst) > 0 else None

if __name__ == '__main__':
    print(f"列表头元素: {head(['h','e','l','l','o'])}")
    print(f"列表头元素: ",head([-9,8,9,10]))

"""
求表尾
"""
def tail(lstt):
    return lstt[-1] if len(lstt)>0 else None

if __name__ == '__main__':
    print(f"列表头元素: {tail(['h','e','l','l','o'])}")
    print(f"列表头元素: ",tail([-9,8,9,10]))

"""
打印乘法表
"""
def mul_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}x{i}={i*j}\t",end='')
        print() #打印换行

if __name__ == '__main__':
    mul_table()

"""
拼接元素
"""
a = [1,11,111]
b = [2,22,222]
print(list(zip(a,b)))
