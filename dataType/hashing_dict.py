"""
dict 字典
1.无序
2.可变
3.value可以为任何数据类型
"""
dict1 = {'name': 'Ray', 'age': 32, 'height': 180.00}
dict2 = {}
dict3 = dict([('name', 'Ray'), ('age', 32)])
dict4 = dict(name='Ray', age=32, height=180.00)
print(dict4)

# 新增/修改
dict1['address'] = 'DaLian'
print(dict1)
dict1['name'] = 'Ray Zhang'
print(dict1)

# 删除
dict1.pop('address')
del dict1['name']
# dict1.clear()

# 查找
if 'address' in dict1:
    print(dict1['address'])
elif 'name' in dict1:
    print(dict1.get('name'))
print(dict1.keys())
print(dict1.values())

new_dict = dict.fromkeys(['name', 'age', 'height'])
print(new_dict)

# 遍历
for k, v in new_dict.items():
    print(f"key: {k}, value: {v}")

for key in new_dict.keys():
    print(key)

for value in new_dict.values():
    print(value)
