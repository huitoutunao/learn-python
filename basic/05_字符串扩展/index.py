""" 字符串的三种定义方式 """

# 单引号定义法
name = 'hello'
print(type(name))

# 双引号定义法
name = "hello"
print(type(name))

# 三引号定义法
name = """ hello """
print(type(name))

# 在字符串内 包含双引号
name = '"hello1"'
print(name)
# 在字符串内 包含单引号
name = "'hello2'"
print(name)
# 使用转义字符 \ 解除引号的效用
name = "\"hello3\""
print(name)

""" 字符串的拼接 """
myName = "张三"
address = "我的地址"
# tel = 130987231 # 类型不是字符串，拼接会报错
print("我是" + myName + "，地址" + address)

"""
字符串格式化

%s 将内容转换成字符串，放入占位位置
%d 将内容转换成整数，放入占位位置
%f 将内容转换成浮点数，放入占位位置
"""
name2 = "李四"
message = "我是：%s" % name2
print(message)

class_num = 66
avg_salary = 10
message = "哈哈哈，测试1的%s，测试2的%s" % (class_num, avg_salary)
print(message)

year = 2000
price = 12.32
message = "%s，成立于%d，价格是%f" % (name2, year, price)
print(message)

"""
字符串格式化-数字精度

m 控制宽度，要求是数字（很少使用），设置的宽度小于数字自身，不生效，是在前面补足空格
.n 控制小数点精度，要求是数字，会进行小数的四舍五入
"""

fNum = 12.345
message = "测试的%.2f" % fNum
print(message)

# 快速字符串格式化-f标记

name = "张三"
set_up_year = 2000
stock_price = 12.32
message = f"你好{name}，成立与{set_up_year}，价格是{stock_price}"
print(message)

"""
表达式进行字符串格式化

f"{表达式}"
"%s\%d\%f" % (表达式, 表达式, 表达式)
"""

print("结果：%d" % (1 + 1))
print(f"结果：{1 * 3}")
print("字符串在Python中的类型名称是：%s" % type("字符串"))

# 小练习

name = "科技公司"
stock_price = 19.99
stock_code = "008979"
stock_price_daily_growth_factor = 1.2
growth_days = 7
message1 = f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}"
message2 = "每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** 7))
print(message1)
print(message2)
