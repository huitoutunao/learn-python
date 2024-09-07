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
def add(a, b):
    res = a + b
    return res

r = add(1, 2)
print(f"结果值：{r}")

# 无return语句的函数返回值
def say_hi():
    print('你好')

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容是：{type(result)}")

# 主动返回 None
def say_hi2():
    print('你好')
    return None

result = say_hi2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容是：{type(result)}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(5)
if not result:
    print("未成年人不能进入网吧")

# None用于声明无初始内容的变量

name = None

# 函数说明文档
def add(x, y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x: 形参x表示相加的其中一个参数
    :param y: 形参y表示相加的其中一个参数
    :return: 返回值是2数相加的结果
    """
    result = x + y
    return result

add(1, 2)

# 函数局部变量
def testA():
    num = 100
    print(num)

testA()
# print(num)

# global关键字
num = 100

def test_a():
    print("test_a")

def test_b():
    global num
    num = 200

test_a()
test_b()
print(f"全局变量 {num}")
