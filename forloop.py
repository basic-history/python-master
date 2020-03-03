text = "1,2;3"

newWord = ""

for char in text:
    if not char.isnumeric():
        newWord = newWord + char;

print(newWord)  # 结果 ,;

# 字符串可以通过join和迭代器连接，左边的语法永远是这样的只有else，可以认为就是用来格式化数据的
newWord2 = "".join(char if char.isnumeric() else "?" for char in text)
print(newWord2)  # 结果 1?2?3

for i in range(1, 5):  # 1-4
    print("now is {}".format(i))

print("*" * 8)

for i in range(1, 5, 2):  # 1 3
    print("now is {}".format(i))

print("*" * 8)
for i in range(10, 5, -2):  # 10 8 6
    print("now is {}".format(i))

for i in range(0, 5):
    for j in range(4, 10):
        if j == 6:
            print()
            continue
        elif j == 7:
            break
        print("{},{}".format(i, j))

i = 0

while i < 10:
    print("now i is {}".format(i))
    i += 1

list = ["java", "c"]

inputValue = ""
while inputValue not in list:
    inputValue = input("请输入")
    if inputValue == "quit":
        print("*" * 8)
        break
print("88")

for i in range(5):
    pass
else:
    print("over")

# 正常退出的时候会执行  break 不执行
c = 0
while c > 5:
    c += 1
else:
    print("over2")
