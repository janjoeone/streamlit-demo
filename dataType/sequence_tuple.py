"""
tuple 元祖
1.有序
2.不可变
3.数据类型可以不同
4.数据可重复
"""
tuple1 = ()
tuple2 = ('abc',)
tuple3 = ('abc', 12, 3.14, [1, 2], (1, 'abc'), 12, [1, 2])

# 下标和切片
print(tuple3[0])
print(tuple3[::-1])

# index
print(tuple3.index(12))

# count
print(tuple3.count(12))
print(tuple3.count([1, 2]))

# len
print(len(tuple3))

# for循环
for element in tuple3:
    print(element)