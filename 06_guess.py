# 猜数字：1-100，最多 10 次，输入非数字不崩溃、不计次数
import random

answer = random.randint(1, 100)
count = 0
won = False

while count < 10:
    try:
        guess = int(input("猜一个 1-100 的数："))
    except ValueError:
        print("请输入数字")
        continue

    count = count + 1

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print("猜对了！你用了", count, "次")
        won = True
        break

if not won:
    print("次数用完了，答案是", answer)
