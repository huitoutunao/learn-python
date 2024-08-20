# ATM

# 定义全局变量
money = 50000
name = None

# 要求客户输入姓名
name = input("请输入你的姓名")

# 定义查询函数
def query(showHeader):
    if showHeader:
        print("-------查询余额-------")

    print(f"{name}，您好，您的查询余额剩余：{money}")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name}，您存款{num}元成功")

    # 调用query函数查询余额
    query(False)

# 定义取款函数
def getMoney(num):
    global money
    money -= num

    print("-------取款-------")
    print(f"{name}，您取款{num}元成功")

    # 调用query函数查询余额
    query(False)

# 定义主菜单函数
def main():
    print("-------主菜单-------")
    print(f"{name}，您好，欢迎来到ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]") # 通过\t制表符对齐输出
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(True)
        continue # 通过 continue 进入下一轮循环
    elif keyboard_input == '2':
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == '3':
        num = int(input("您想要取多少钱？请输入："))
        getMoney(num)
        continue
    else:
        print('程序退出')
        break
