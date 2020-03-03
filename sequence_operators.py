string1 = "hello "
string2 = "world! "
string3 = "pleuvoir"

print(string1 + string2)
print(len(string1 + string2))  # 13
print("hello " "world! ")
print(len("hello " "world! "))  # 13

print("he" in string1)  # True

print(" " in string1)  # True

print("" in string3)  # 永远是True

print(string1 * 5)  # 打印5次
