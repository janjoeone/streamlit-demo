"""
算术运算符
"""
# 整除
print(9 // 2)
# 取余
print(17 % 2)
# 指数
print(2 ** 3)
print(pow(8, 1/3))
print(pow(2, 4))

"""
赋值运算符
"""
a = 100

"""
复合赋值运算符
"""
x = 13
x += 2 * 8
print(x)

"""
比较运算符
== 
!=
>
<
>=
<=
"""
num1 = 65536
num2 = 65536
print(num1 is num2)
print(id(num1))
print(id(num2))

"""
逻辑运算符
and
or
not
"""
print(True and False)
print(True or False)
print(not True)