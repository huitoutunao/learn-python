# range语法1 range(num)

for x in range(10):
    print(f"语法1: {x}")

# range语法2 range(num1, num2)

for x in range(5, 10):
    # 从 5 开始，到 10 结束，不包含10本身
    print(f"语法2: {x}")

# range语法3 range(num1, num2, step)

for x in range(5, 10, 2):
    # 从 5 开始，到 10 结束，不包含10本身，数字间隔是2
    print(f"语法3: {x}")

count = 0

for x in range(1, 100):
    if x % 2 == 0:
        count += 1

print(f"1-100有{count}偶数")
