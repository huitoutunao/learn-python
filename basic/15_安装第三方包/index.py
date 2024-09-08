# 安装镜像
# 如何在当前工程目录安装不要安装在全局：pipenv
# 了解下通义灵码AI插件

# 1、pipenv install
# 2、pipenv install <package-name>
# 3、pipenv install <package-name> --dev（开发依赖）
# 4、pipenv shell（可激活虚拟环境）
# 5、exit（退出虚拟环境境）
# 6、pipenv clean（清理未使用的包）
# 7、pipenv uninstall <package-name>（卸载包）
# 8、pipenv update <package-name>（更新包）
# 9、pipenv update（更新所有包到最新版本）
# 10、pipenv --help（查看帮助）

# 切换 python 解释器，因为我是通过 pipenv 安装在当前工程目录下的依赖，不是安装在全局的，所以只有当前解释器才有这个依赖
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

def print_yang_hui(n):
    # 边界条件处理：如果输入的行数小于等于0，则直接返回空列表
    if n <= 0:
        return []

    # 初始化结果列表，开始时包含第一行
    result = [[1]]

    # 通过迭代生成杨辉三角的后续行
    for i in range(1, n):
        # 获取上一行的数据
        prev_row = result[-1]
        # 生成新行的数据：首尾添加1，中间元素通过上一行相邻元素之和计算
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        # 将新行添加到结果列表中
        result.append(new_row)

    # 打印最终生成的杨辉三角
    for row in result:
        print(row)

# 调用函数打印前10行
print_yang_hui(10)

