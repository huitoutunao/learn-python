# 定义元组
t1 = (1, True, 'hello')
t2 = () # 空元组
t3 = tuple() # 空元组
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")

# 定义单个元素的元组，结尾写个逗号
t4 = ('world', )
print(f"t4的类型是：{type(t4)}，内容是：{t4}")

# 元组的嵌套
t5 = ((1, 2), (3, 4))
print(f"t5的类型是：{type(t5)}，内容是：{t5}")

# 元组的下标取值
t5_1 = t5[1][1]
print(f"t5_1的内容是：{t5_1}")

# 元组的操作：index 查找方法
t6 = ('教育', '程序员', 'python')
index = t6.index('程序员')
print(f"在元组t6中查找程序员，下标是{index}")

# 元组的操作：count 统计方法
t7 = ('11', '22', '11', '44', '11')
num = t7.count('11')
print(f"在元组t7中统计11出现次数是{num}")

# 元组的操作：len 函数统计元组数量
t8 = ('22', '22', '66')
num = len(t8)
print(f"统计元组t8长度是{num}")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"while循环{t8[index]}")
    index += 1

# 元组的遍历：for
for elem in t8:
    print(f"for循环{elem}")

# 注意：如果元组嵌套了 list 那么里面的 list 元素是可以修改的
