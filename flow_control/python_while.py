"""
while循环
"""
n = 1
sum_result = 0
while n <= 100:
    if n % 2 != 0:
       sum_result += n
    n += 1
print(sum_result)

row = 1
while row <= 9:
    column = 1
    while column <= row:
        print(f"{column}*{row}={column*row}", end='\t')
        column += 1
    row += 1
    print("\n")