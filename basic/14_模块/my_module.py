__all__ = ["test2"]

def test(a, b):
    print(a + b)

def test2(x):
    print(x)

# 只在当前文件运行才会输出，类似开发环境变量
if __name__ == "__main__":
    test(1, 2)
