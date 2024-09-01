# list 容器
name_list = ['h', 'o', 'p']
print(name_list)
print(type(name_list))

# list 包含不同类型
my_list = ['h', True, 1]
print(my_list)

# list 嵌套列表
my_list2 = [['1'], [True], [666]]
print(my_list2)

# 通过列表索引取值（顺序）
print(my_list[0])
print(my_list[1])

# 通过列表索引取值（逆序）
print(my_list[-1])
print(my_list[-2])

# 取出嵌套列表的元素
print(my_list2[0][0])

# 列表的常用方法操作
myList = ['w', 't', 'o']
index = myList.index('w')
print(f"列表索引值：{index}")

# 元素不存在，会报错
# index = myList.index('p')
# print(f"列表索引值：{index}")

# 修改特定下表索引值
myList[0] = 'y'
print(f"修改特定值后输出：{myList}")

# 在指定下标位置插入新元素
myList.insert(0, 'u')
print(f"插入新元素后输出：{myList}")

# 追加元素
myList.append('r')
print(f"追加新元素后输出：{myList}")

# 在列表尾部追加一批元素
myList.extend([1, 2, 3])
print(f"批量追加元素后输出：{myList}")

# 删除指定下标元素
del myList[1]
print(f"del删除元素后输出：{myList}")
ele = myList.pop(0)
print(f"pop删除元素后输出：{myList}，取出的元素是：{ele}")

# 指定元素在列表中的第一个匹配项
myList2 = [1, 2, 3]
myList2.remove(2)
print(f"remove删除元素后输出：{myList2}")

# 清空列表
myList2.clear()
print(f"clear清空列表后输出：{myList2}")

# 统计某元素在列表中出现的数量
myList3 = [1, 1, 2, 2, 2, 3]
count = myList3.count(2)
print(f"count统计元素2数量：{count}")

# 统计列表数量总数
myList3 = [1, 1, 2, 2, 2, 3]
count = len(myList3)
print(f"len统计元素数量：{count}")

# 序列切片
# 语法：序列[起始下标:结束下标:步长]
demo_list = [0, 1, 2, 3, 4, 5, 6]
result1 = demo_list[0:3]
print(f"序列切片1{result1}")
result2 = demo_list[0:3:2]
print(f"序列切片2{result2}")
