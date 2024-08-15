"""
函数学习
"""

# 需求：统计字符串的长度，不使用内置函数len()
str1 = "helloa"
str2 = "itcarcv"
str3 = "worldasd"

# 定义一个计数变量
count = 0
for i in str1:
    count += 1

print(f"字符串{str1}的长度是：{count}")

# 定义函数
def my_len(data):
    count = 0
    for i in data:
        count += 1

    print(f"字符串{data}的长度是：{count}")

my_len(str1)
my_len(str2)
my_len(str3)


# 定义一个函数，输出相关信息
def say_hi():
    print("hello world")

say_hi()

# 定义一个函数的返回值
