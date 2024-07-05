""" 数据类型定义 """
# 方式1
print(type("hello"))
print(type(666))
print(type(13.14))

# 方式2
string_type = type("hello")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 方式3
name = "张三"
name_type = type(name)
print(name_type)

""" 数据类型转换 """
# 将数字转换成字符串
num_str = str(11)
print(type(num_str), num_str)

# 将字符串转换成数字
str_num = int("12")
print(type(str_num), str_num)

"""
错误示例，想要将字符串转换成数字，必须要求字符串内的内容是数字

num2 = int("你好")
print(type(num2), num2)
"""

# 整数转浮点数
float_num = float(13)
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(13.14)
print(type(int_num), int_num)
