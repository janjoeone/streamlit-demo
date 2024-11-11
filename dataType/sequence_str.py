"""
str 字符串
1.有序
2.不可变
"""
str1 = "python"
print(str1[1])
print(str1[-1])

# 切片
print(str1[2:5:1])
print(str1[2:5])
print(str1[::-1])

# 字符串查询
print(str1.find('py'))
print(str1.find('asdkda'))
print(str1.index('py'))

print(str1.rfind('py'))
print(str1.rfind('asdkda'))
print(str1.rindex('py'))

# 大小写转换
str2 = 'hello world'
print(str2.upper())
print(str2.capitalize())
print(str2.title())

# 字符串对齐
str3 = 'hello world'
print(str3.center(30, 'a'))
print(str3.ljust(30, 'a'))
print(str3.rjust(30, 'a'))
print(str3.zfill(30))

# 分割字符串
str4 = 'I am a developer'
# 分隔符不会在结果中出现
print(str4.split(' '))
# 分区，分隔符单独一个区
print(str4.partition(' '))
print(str4.rpartition(' '))

# 合并与替换
str5 = 'hello world'
print(str5.replace('world', 'python'))
str6 = 'hello world world'
print(str5.replace('world', 'python', 1))

# 去除多余字符
str7 = ' hello world '
print(str7.strip())
print(str7.lstrip())
print(str7.rstrip())