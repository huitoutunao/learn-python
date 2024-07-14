# 判断语句实战案例：终极猜数字
import random

num = random.randint(1, 10)

guess_num = int(input("输入你要猜测的数字："))

if guess_num == num:
    print("恭喜，猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜，猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("第三次输入你要猜测的数字："))

        if guess_num == num:
            print("恭喜，猜中了")
        else:
            print("很遗憾，三次机会没有猜中")
