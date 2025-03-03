# -*- coding: UTF-8 -*-
'''
@File           : code-02.py
@Lisense        : (C)Copyright 2024-2025
@Modify Time    : 2025/2/13 6:06 PM 
@Author         : None
@Version        : None
@Desciption     : None
'''

s = '   Hello   '
s = s[:]
print(s)
s1 = s[2:8:2]
print(s1)
s = '   hello    '.strip()
print(s)
s = '####hello****'.strip()
print(s)
s = ' \n \t hello\n'.strip("\n")
print(s)
s = '####hello$$$$$'.strip('#')
print(s)
s = 'www.bamidu.com'.strip('w.com')
print(s)
s = '      hello     '.lstrip()
print(s)
s = 'Arthur: three!'.lstrip('Arthur: ')
print(s)
print("----------字符串查找-----------")
str = 'Welcome to DateScience'
print('查找字符\'Da\'是否存在于str中', str.find('Da'))
print('查找字符\'wc\'是否存在于str中', str.find('wc'))
print(f'检查字符串str中是否包含\'come\'字符 返回索引起始 index: %d' % str.index('come'))
print(f'检查字符串\'str\'中是否包含\'Date\'字符，返回索引起始 index: %d' % str.index('Date'))
try:
    print(f'检查字符串\'str\'中是否包含\'Java\'字符，返回索引起始 index: %s' % str.index('Java'))
except:
    ValueError
print('字符串\'str\'中没有包含\'Ja\'')


print("----------字符出现次数计数-----------")
print(f'字符\'e\'出现次数 count: %d' % str.count('e'))
print(f'字符\'Da\'出现次数 count: %d' % str.count('Da'))
print(f'字符\'Ja\'出现次数 count: %s' % str.count('Ja'))

print("----------字符串替换-----------")
s = 'Welcome to Data Science'
print(f'替换\'str\'字符串中\'Data\'为\'data\': {s.replace("Data","data")}')
print(f'替换\'s\'字符串中\'e\'为\'E\'并且不超过2次: {s.replace("e","E",2)}')



str = 'Welcome to Data Science'
print(f'不使用参数默认输出: {str.split()}')
print(f"用空格作为分界符: {str.split(' ')}")
print(f"使用\'e\'作为分界符，并且maxsplit为2(分为3组): {str.split('e',2)}")

str = 'welcome to Data Science'
print(str.capitalize())


seq = 'Welcome to Data Science'
str = ' '
strs = '-'
print(f"源字符串:'{seq}'\n使用空格作为连接符: {str.join(seq)}")
print(f"使用\'-\'作为连接符: {strs.join(seq)}")


print("---------title函数-----------")
str ='welcome to data science'
print(f"所有单词首字母大写: {str.title()}")
str1 = 'welcome to data-science.'
print(f"添加标点符号: {str1.title()}")

print("---------lower函数-----------")
str = 'WELCOME TO DATA SCIENCE'
print(f"将\'{str}\'所有字符串转换为小写: {str.lower()}")

print("---------upper函数-----------")
str = 'welcome to data science'
print(f"将\'{str}\'字符串中的字母转换为大写: {str.upper()}")


print("---------ljust函数-----------")
str = 'Welcome to data science'
print('str源长度为%d' % len(str))
print('str 处理后的长度为: %d' % (len(str.ljust(30))))
print(len(str.ljust(40)))

print("---------rjust函数-----------")
str ='Welcome to data science'
print(f'{str}的原始长度为 %d' % len(str))
print(f'{str}处理后的长度为 %d' %len(str.rjust(30)))
print(str.rjust(30))

print("---------center函数-----------")
str = 'Welcome to Data science'
print(f'\'{str}\'的原始长度为 %d' % len(str))
print(f'\'{str}\' 处理后的长度为 %d' % len(str.center(30)))

print("---------lstrip函数-----------")
str ='    Welcome to Data Science'
print(f"str原始内容[{str}]，长度为：{len(str)}")
new_str = str.lstrip()
print(f'str去掉左边空格后，内容为[{new_str}],长度为[{len(new_str)}]')

print("---------rstrip函数-----------")
str = 'Welcome to Data Science      '
print(f"str原始内容[{str}],长度为[{len(str)}]")
new_str = str.rstrip()
print(f"str去掉右边空格后,内容为[{new_str}],长度为[{len(new_str)}]")

print("---------strip函数-----------")
str ='    Welcome to Data Science    '
print(f"str原始内容[{str}],长度为[{len(str)}]")
new_str = str.strip()
print(f"str去掉两边空白字符后，内容为[{new_str}],长度为[{len(new_str)}]")

print("---------startswhith函数-----------")
str='Welcome to Data Science'
print(f"str原始内容为[{str}],判断是否以字符大写[\'W\']开头",str.startswith('W'))
print(f"str原始内容为[{str}],判断是否以字符小写[\'W\']开头",str.startswith('w'))

print("---------endswhith函数-----------")
str ='Welcome to Data Science'
print(f"str原始内容为[{str}],判断是否以字符大写[\'E\']结尾",str.endswith('E'))
print(f"str原始内容为[{str}],判断是否以字符小写[\'e\']结尾",str.endswith('e'))

print("---------isdigit函数-----------")
str ='Welcome to Data Science'
print(f"str原始内容为[{str}],是否只包含数字 {str.isdigit()}")
int_str ='1234'
print(f"int_str原始内容为[{int_str}],是否只包含数字 {int_str.isdigit()}")

print("---------isalnum函数-----------")
str1='Welcome to Data Science'
print(f"str1原始内容[{str1}],是否由数字字母组成 {str1.isalnum()}")
str2='123adfc'
print(f"str2原始内容{str2},是否由数字字母组成 {str2.isalnum()}")

print("---------isspace函数-----------")
str1 ='Welcome to Data Science'
print(f"str原始内容[{str}],是否包含空格 [{str.isspace()}]")
str2 =' '
print(f"str2原始内容[{str2}],是否包含空格 [{str2.isspace()}]")