# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_1变量的内容是：{bool_2}，类型是：{type(bool_2)}")

# 比较运算符的使用
# == != >= <= > <
num1 = 10
num2 = 10
print(f"10 == 10 结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 10 结果是：{num1 != num2}")

name1 = 'itcast'
name2 = 'itethem'
print(f"itcast == itethem 结果是：{name1 == name2}")

# if 判断语句
age = 30
if age > 18:
    print("我已经成年了")

print("时间过得真快呀")

# 练习题
print("欢迎来到儿童游乐园，儿童免费，成人收费。")
age = input("请输入你的年龄：")
age = int(age)
if age > 18:
    print("您已成年，游玩需要补票10元")

print("祝你游玩愉快")

# if else 语句
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元")
elif age >= 30:
    print("else if")
else:
    print("未成年免费")
