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
