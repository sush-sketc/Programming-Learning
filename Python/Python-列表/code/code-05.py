# -*- coding: UTF-8 -*-
'''
@File           : code-05.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025-03-07 12:54 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

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