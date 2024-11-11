"""
if  条件语句
"""
age = int(input("您的年龄是："))
if 0 <= age < 18:
    print("未成年")
elif 18 <= age < 60:
    print("打工仔")
elif 60 <= age:
    print("老年人")
else:
    print("输入有误")

# 三目运算
num = int(input("请输入一个整数："))
print(f"{num}为偶数" if num % 2 == 0 else f"{num}为奇数")