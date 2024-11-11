"""
set 集合
1.无序
2.可变
3.数据类型只能为不可变
4.不重复
"""
set1 = set()
set2 = {'a', 1, 3.14, (1, 2)}
print(type(set2))

print(len(set2))

# 添加数据
set2.add(99)
set2.add('hello')
print(set2)

# 添加一个或多个元素
set2.update({8, 'world', 9})
print(set2)
set2.update({99, 'python'}, [1024, 'developer'], (2048, '你好'), 'today', {'name': 'Ray', 'age': 32})
print(set2)

# 删除数据
set2.remove('hello')
print(set2)

set2.pop()
print(set2)

# 遍历
for element in set2:
    print(element)