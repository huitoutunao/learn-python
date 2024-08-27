# 循环迭代 while
def list_while_func():
    my_list = ['h', 'o', 'p']

    # 定义一个变量用来标记列表的下标
    index = 0
    while index < len(my_list):
        item = my_list[index]
        print(f"{item}")
        index += 1

list_while_func()

# 循环迭代 for
def list_for_func():
    my_list = ['1', '2', '3']
    for item in my_list:
        print(f"{item}")

list_for_func()

# 循环迭代 for 索引 + 索引值
def list_for_index_func():
    my_list = ['1a', '2a', '3a']
    for idx,val in enumerate(my_list):
        print(f"{idx}--{val}")

list_for_index_func()
