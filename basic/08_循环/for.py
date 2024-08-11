# for 循环基础使用

name = "iloveyou"

for item in name:
    print(item)

"""
练习：数一数有几个a
"""
name = "itehea is a brand of itcast"

count = 0

for x in name:
    if x == "a":
        count += 1

print(f"被统计的字符串有{count}个a")

# for 循环嵌套
i = 0
for i in range(1, 101):
    print(f"今天是坚持的第{i}天")

    for j in range(1, 11):
        print(f"给人送玫瑰花第{j}朵")

print(f"第{i}天成功")

# for 循环打印9*9乘法表
# 通过外层循环控制行数
for i in range(1, 10):
    # 通过内层循环控制每一行数据
    for j in range(1, i + 1):
        # 在内层循环中输出每一行的内容
        print(f"{j} * {i} = {j * i}\t", end="")

    # 外层循环可以通过print输出一个回车符
    print()


# for 循环断句 continue 只作用当前循环
for x in range(1, 5):
    print("语句1")
    continue
    print("语句2")

# for 循环跳出 break 只作用当前循环
for x in range(1, 5):
    print("语句11")
    break
    print("语句22")

print("语句33")
