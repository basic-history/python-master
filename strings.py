print('Hello World!')
print("Hello World!")
print('hello double "" hah')  # hello double "" hah

print("hello "" hah")  # hello  hah 没有引号

print('hello' + ' world')

print('hello' + ' ' + 'nihao')

gretting = 'hello'

name = input("what's your name?")

print(gretting, name)

age = 18

print(age)

print(type(age))

age = 'hehe'
print(age)

print(type(age))

game = "ABc_Def呵呵ß"  # 最后一个是德语

print(game.capitalize())  # Abc_def呵呵ß
print(game.upper())  # ABC_DEF呵呵SS
print(game.lower())  # 不能正确转换德语为小写，所以用下面的就妥了
print(game.casefold())  # 最后一个是德语 小写为ss

# 把前面或者结尾的干掉，注意：部分也可以不一定是连续的才起作用
text = 'abcdEFa'
print(text.strip('ac'))  # bcdEF
print(text.strip('fab'))  # cdEF
