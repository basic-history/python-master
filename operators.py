a = 16;
b = 4;

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # float类 4.0
print(a // b)  # 4
print(a % b)  # 0

for i in range(1, a // b):  # 1 2 3 4
    print(i)

print(a + a / b)  # 20.0
print(a + a // b)  # 20

print(a + b / a)  # 16.25
print(a + b // a)  # 16  会丢失精度
