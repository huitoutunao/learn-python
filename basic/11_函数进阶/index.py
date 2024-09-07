# 函数返回多个值
def test_return():
    return 1, 2, True

x, y, z = test_return()
print(f"{x, y, z}")

# 函数参数种类
def user_info(name, age, gender):
    print(f"{name, age, gender}")

# 1 位置参数
user_info("小明", 18, "男")

# 2 关键字参数
# 关键字参数可以不考虑顺序传递
# 混用时位置参数必须放置前面
user_info("小红", gender="女", age=16)

# 3 缺省参数（默认值且只能放置最后）
def user_info2(name, age, gender="男"):
    print(f"{name, age, gender}")

user_info2("小天", 13)

# 4 不定长-位置不定长，*号
def user_info3(*args):
    print(f"{args}")

user_info3("小美", "美术生")

# 5 不定长-关键字不定长，**号
def user_info4(**kargs):
    print(f"{kargs}")

user_info4(name="小周", age=12, gender="男")

# 函数作为参数传递
def test_func(computed):
    result = computed(1, 2)
    print(result)

def computed(x, y):
    return x + y

test_func(computed)

# 匿名函数 lambda 参数: 函数体(一行代码)
def test_func2(computed):
    result = computed(1, 2)
    print(result)

test_func2(lambda x, y: x + y)
