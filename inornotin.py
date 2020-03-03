text = "python"

print(text.casefold())  # 全转为小写
print(text.capitalize())  # 首字母大写

value = input("输入：")

if value in text.casefold():
    print("{} is in {}".format(value, text))

print("hello_world".capitalize())

game = "ABc_Def呵呵ß"  # 最后一个是德语

if "LOL" not in game.lower():
    print("我要玩LOL")

print(game.capitalize())
print(game.upper())
print(game.lower())  # 不能正确转换
print(game.casefold())  # 最后一个是德语 小写为ss
