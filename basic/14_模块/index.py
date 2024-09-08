# 模块
# 导入内置的 time 模块
"""
import time
time.sleep(5)
print("你好")
time.sleep(5)
print("测试")
"""

# 使用 from 导入 time 的 sleep 方法
"""
from time import sleep
sleep(5)
print("你好")
sleep(5)
print("测试")
"""

# 使用 * 导入 time 模块的全部功能
"""
from time import *
print("你好")
sleep(5)
print("测试")
"""

# 使用 as 给特定功能加别名
"""
import time as t
print("你好")
t.sleep(5)
print("测试")
"""

# 使用自定义 module
# import my_module
# my_module.test(1, 3)

# __all__ 变量 对引入的 星号 * 才有作用
# from my_module import *
# test2("哈哈哈")

# 使用自定义包
# 注意：my_package 要在当前文件目录下，不然运行当前文件，会报找不到自定义包名
# import my_package.my_module1
# import my_package.my_module2

# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# 建议使用这种
from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

