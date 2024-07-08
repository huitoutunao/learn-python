# 获取键盘输入信息
name = input("请告诉我你是谁？")
print("我知道了，你是：%s" % name)

# 输入数字类型
num = input("请告诉我你的银行卡密码：")
num = int(num)
print("你的银行卡密码：", type(num))

# 练习题

user_name = input("请输入用户名")
user_type = input("请输入用户类型")
print("您好：%s，您是尊贵的：%s 用户，欢迎您的光临" % (user_name, user_type))
