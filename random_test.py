import random

answer = random.randint(0, 10)

text = 0

print("请输入0-10的数字：")

while text != answer:
    text = int(input())
    if text > answer:
        print("太大了")
    else:
        print("太小了")

print("答对了，答案是{}".format(answer))
