# 字典

my_dict = {
    "王": 99,
    "周": 90,
    "林": 80
}

empty = dict()
print(f"{my_dict},{type(empty)}")

# 获取字典值
score = my_dict['王']
print(f"{score}")

# 字典嵌套
my_new_dict = {
    "王": {
        "语文": 90,
        "数学": 99
    },
    "周": {
        "语文": 91,
        "数学": 98
    },
    "林": {
        "语文": 88,
        "数学": 89
    },
}
print(f"{my_new_dict}")

score2 = my_new_dict["林"]["语文"]
print(f"嵌套字典取值{score2}")

# 新增元素
my_dist2 = {
    "z": 90,
    "l": 80,
    "t": 89
}
my_dist2["q"] = 70
print(f"{my_dist2}")

# 更新元素
my_dist2["z"] = 99
print(f"{my_dist2}")

# 删除元素
value = my_dist2.pop("l")
print(f"{value}, {my_dist2}")

# 清空元素
my_dist2_clear = {"hh": 11, "gg": 22}
my_dist2_clear.clear()
print(f"字典被清空了{my_dist2_clear}")

# 获取全部key
my_dist2_keys = my_dist2.keys()
print(f"{my_dist2_keys}")

# 遍历字典
for key in my_dist2_keys:
    print(f"遍历{my_dist2[key]}")

# 统计字典内的元素数量
num = len(my_dist2)
print(f"字典元素数量{num}")

# 练习案例
info_dist = {
    "王": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周": {
        "部门": "科技部",
        "工资": 5000,
        "级别": 2
    },
    "林": {
        "部门": "科技部",
        "工资": 7000,
        "级别": 3
    },
    "刘": {
        "部门": "科技部",
        "工资": 6000,
        "级别": 1
    }
}
for key in info_dist:
    item = info_dist[key]
    if item["级别"] == 1:
        item["级别"] = 2
        item["工资"] += 1000

print(f"案例结果{info_dist}")
