# 二分查找


low = 1
high = 100

print("心里想一个{}-{}之间的数字，然后按照提示操作：".format(low, high))

while True:
    guess = (low + high) // 2
    print("是不是{}?，高了输入h，低了输入l，一样输入c".format(guess))
    high_low = input().casefold()
    if high_low == "h":
        high = guess
    elif high_low == "l":
        low = guess
    else:
        print("我就知道猜对了")
        break
