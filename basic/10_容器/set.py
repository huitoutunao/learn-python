# 定义集合，不允许重复元素且无序
my_set = {"hello", "world", "it", "hello", "world"}
my_set_empty = set()
print(f"{my_set}，类型是{type(my_set)}")
print(f"{my_set_empty}，类型是{type(my_set_empty)}")

# 添加新元素
my_set.add("hhh")
print(f"{my_set}")

# 移除元素
my_set.remove("it")
print(f"{my_set}")

# 随机取一个数
ele = my_set.pop()
print(f"{ele}")

# 清空集合
my_set.clear()
print(f"{my_set}")

# 取2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3)

# 消除差集：在集合1内，删除和集合2相同的元素
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1)
print(set2)

# 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set3)

# 统计集合元素数量
num = len(set3)
print(num)

# 集合遍历
set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(f"集合的元素有：{item}")

# 练习案例
my_list = ["it", "hello", "it", "hello", "world", "uu", "pp"]
my_set = set()

for item in my_list:
    my_set.add(item)

print(f"列表内容是：{my_set}")
