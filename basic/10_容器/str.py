# 字符串下标索引
my_str = "hello world"
value = my_str[4]
value2 = my_str[-7]
print(f"{value}={value2}")

# 字符串是不可直接修改操作

# index 小标索引值
value3 = my_str.index('w')
print(f"下标{value3}")

# 字符串替换方法 replace
new_my_str = my_str.replace('w', 'W')
print(f"替换{new_my_str}")

# split 方法
my_str2 = "hello it world"
my_str_list = my_str2.split(" ")
print(f"{my_str_list}")

# strip 方法，去掉头尾的空格或指定字符串
my_str3 = " hello world "
new_my_str3 = my_str3.strip()
print(f"strip无传参后{new_my_str3}")

my_str4 = "12hello12world21"
new_my_str4 = my_str4.strip('12')
print(f"strip传参后{new_my_str4}")

# count 统计字符串中某个字符串出现的次数
# len 统计字符串的长度

# 练习案例
demo = "ithey ite boxblock"
num = demo.count("it")
print(f"练习案例，统计it字符{num}")

new_demo = demo.replace(" ", "|")
print(f"练习案例，替换空格字符{new_demo}")

new_demo2 = new_demo.split("|")
print(f"练习案例，分割字符{new_demo2}")
