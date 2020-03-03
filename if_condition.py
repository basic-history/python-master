# name = input("请输入姓名：")
# age = int(input("{0} 你好，请输入年龄:".format(name)))
#
# if age < 18:
#     print("再等{}年吧。".format(18 - age))
#
# elif age == 900:
#     print("呵呵")
# else:
#     print("你可以投票")


# guess = 5
#
# print("请猜测一个1-10内的数字：")
# value = int(input());

# if value > guess:
#     print("太大了")
#     value = int(input("重新输入:"))
#     if value == guess:
#         print("太棒了")
#     else:
#         print("真可惜")
# elif value < guess:
#     print("太小了")
#     value = int(input("重新输入:"))
#     if value == guess:
#         print("太棒了")
#     else:
#         print("真可惜")
# else:
#     print("答对了")

# if value != guess:
#     if value > guess:
#         print("太大了，重新输入：")
#     else:
#         print("太小了，重新输入")
#     value = int(input())
#     if value == guess:
#         print("不错")
#     else:
#         print("错误，结束")
# else:
#     print("答对了")

#
# print("输入你的年龄：")
# age = int(input())
#
# if age > 18 and age <= 65:  #18 < age <= 65
#     print("好好搬砖")
# else:
#     print("歇着")


print("输入你的年龄：")
age = int(input())
if age < 18 or age >= 65:
    print("回家歇着")
else:
    print("好好搬砖")

if 0:
    print("不会到达")
else:
    print("hehe")

name = ""

# if name != "":  和下面的是等价的，下面的记得引号中不能加空格
if name != "":
    print("不为空")
else:
    print("为空")

if age in range(0, 15):  # >=0 and <15
    print()
