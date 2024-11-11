"""
序列通用操作
"""
# 数学运算
# + -> 拼接
str1 = 'hello' + 'world'
print(str1)

list1 = [100, 3.14, 'abc']
list2 = list1 + [3.6, 'hello', 'world']
print(list2)

tuple1 = ('hello',)
tuple2 = ('world',)
print(tuple1 + tuple2)

# * -> 重复
print("-" * 10)
print([1] * 10)
print((1,) * 10)

# > < >= <=
print([1, 2, 'a'] > [1, 2, 'b'])

# 成员判断
t1 = (100, 200)
print(10 in t1)
print(10 not in t1)

# 下标、切片

# 内置函数
lst = [1, 2, 4]
print(len(lst))
print(max(lst))
print(max('hello'))
print(min(lst))
print(min('hello'))
print(sum(lst))