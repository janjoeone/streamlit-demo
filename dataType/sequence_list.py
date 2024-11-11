"""
list 列表
1.有序
2.可变
3.数据类型可以不同
4.数据可重复
"""
list1 = []
list2 = [12, 'ab', 12, 12, 3.14, [1, 'a', 2.8, True]]

# 列表修改操作
list2[1] = 'abc'
print(list2.index(12))
print(list2.count(12))
print(len(list2))

# 列表结尾追加数据
list2.append(319)
print(list2)

# 列表结尾追加序列
list2.extend(['312321', 1, 213.2, [1, 2, 3]])
print(list2)

# 指定位置插入数据
list2.insert(0, 100)
print(list2)

# 删除数据
# pop -> 删除并返回
# 默认删除最后一个数据
print(list2.pop())
print(list2)
# 删除指定下标数据
print(list2.pop(0))
print(list2)
# del
del list2[2]
print(list2)
# remove -> 根据数据内容删除匹配到的第一个元素
list2.remove(12)
print(list2)

# 逆序
print(list2[::-1])
print(list2.reverse())

# 排序
list3 = [4, 1, 3, 4, 9, 1, 0, 100]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

# 遍历
for element in list3:
    print(element)