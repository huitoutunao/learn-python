# 容器通用操作方法
# len max min

lists = (1, 2, 3)

# 类型转换：容器转列表 list
print(f"{list(lists)}")

# 类型转换：容器转元组 tuple
# 类型转换：容器转字符串 str
# 类型转换：容器转集合 set

# sorted 排序
# sorted(容器, [reverse=True])
# reverse True 倒序 False 顺序
print(f"{sorted(lists, reverse=True)}")
