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
