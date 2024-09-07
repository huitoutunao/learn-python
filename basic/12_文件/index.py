# 文件编码 UTF-8
# 文件读取 r w a
# fs = open("E:/python-projects/测试.txt", "r", encoding="UTF-8")
# w 模式，新建文件或者覆盖原本内容
# fs = open("E:/python-projects/测试.txt", "w", encoding="UTF-8")
# a 模式 追加内容
fs = open("E:/python-projects/测试.txt", "a", encoding="UTF-8")

# 连续调用读取，会在上次读取标记开始
# print(f"读取文件内容：{fs.read()}")
# print(f"读取文件内容：{fs.readlines()}")

# print(f"读取文件内容一行：{fs.readline()}")
# print(f"读取文件内容二行：{fs.readline()}")
# print(f"读取文件内容三行：{fs.readline()}")

# 循环读取文件行
# for line in fs:
#     print(f"读取文件内容三行：{line}")

# with open 语句，执行完成后自动关闭文件占用
# with open("E:/python-projects/测试.txt", "r", encoding="UTF-8") as fs:
#     print(f"读取文件内容：{fs.read()}")

fs.write("\n666")
# fs.flush()




# 文件关闭 内置 flush 功能
fs.close()
