"""
输出的格式化
"""
# 1. %s %d %f 占位符
my_name = 'Ray'
my_age = 32
my_city = 'DaLian'
my_height = 180.00

print('我的名字是%s，我的年龄是%06d，我的身高是%.1f厘米' % (my_name, my_age, my_height))

# 精确的四舍五入
from decimal import Decimal
print(Decimal('22.345').quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))

# 2. f-str
print(f'我的名字是{my_name}，我的年龄是{my_age}，我的身高是{my_height}厘米')
