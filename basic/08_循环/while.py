# while 循环基础使用

"""
i = 0
while i < 100:
    print("哈哈哈")
    i += 1
"""

# 1-100 累加值

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print(f"1-100累加的和：{sum}")

# 获取范围在 1-100 的随机数字
"""
import random
num = random.randint(1, 100)
count = 0
flag = True

while flag:
    guess_num = int(input("输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"总共猜了{count}次")
"""

# while 循环嵌套

i = 1
while i <= 100:
    print(f"今天第{i}天，准备表白...")

    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("哈哈哈")
    i += 1

print(f"坚持了第{i - 1}天")

# while 循环 9*9 乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end="")
        j += 1

    i += 1
    print() # 输出一个换行
