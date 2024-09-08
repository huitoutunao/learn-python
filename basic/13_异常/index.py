# 异常
try:
    fs = open("E:/python-projects/哈哈哈.txt", "r", encoding="UTF-8")
except:
    print(f"出现异常了，文件不存在，我更改模式打开")
    fs = open("E:/python-projects/哈哈哈.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print(f"出现了变量未定义的异常{e}")

# 捕获多个异常
try:
    # print(name)
    1 / 0
except(NameError, ZeroDivisionError) as e:
    print(f"出现异常{e}")

# 捕获多个异常
try:
    print(name)
except Exception as e:
    print(f"捕获多个=出现异常了{e}")

# 异常 else：如果没有异常的话，就执行代码块
try:
    print("hello")
except Exception as e:
    print(f"捕获多个=出现异常了{e}")
else:
    print("没有异常")

# 异常 finally：不管是否异常都会执行代码块
try:
    # print(name)
    print("hello")
except Exception as e:
    print(f"捕获多个=出现异常了{e}")
finally:
    print("执行完成")

# 异常具有传递性
def func_1():
    print("func1")
    1 / 0

def func_2():
    print("func_2")
    func_1()

def main():
    try:
        func_2()
    except Exception as e:
        print(e)

main()
