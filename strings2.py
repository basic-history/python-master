text = 'abcdefg'

print(text[0])
print(text[1])
print(text[2])

print(text[0 - 7])
print(text[1 - 7])
print(text[2 - 7])

print(text[6 - 7])

print(text[-1])

print()

# abcdefg

print(text[:])  # 截取全部字符串 abcdefg
print(text[0:1])  # 第一位不包含右边 a

print(text[:6])  # abcdef
print(text[:7])  # abcdefg
print(text[0:])  # 从第一位到最后一位  text[0:7]

print(text[:2])  # 从第一位到下标为2的

print(text[-1:])  # g  从最后一位到结尾
print(text[-2:])  # fg  从倒数第二位到结尾
print(text[-3:-1])  # ef

print(text[-3:6])  # ef
print(text[-3:])  # efg

# 必须是从左到右截取的，包左不包右

print()
number = '12,345;789,145'

# 取出所有符号
print(number[2:])  # ,345;789,145

seperstors = number[2:14:4]
print(seperstors)  # 上面的结果按照索引取4的倍数,;,

# list元素用！连接起来成为一个新的字符串
join = "!".join(['1', '2', '3'])
print(join)  # 1!2!3

print(''.join(['4', '5', '3']))  # 453

# 转换为list
print(join.split('!'))  # ['1', '2', '3']
print()
print("join.split()===", join.split())  # ['1!2!3']

# 这句话的意思是 通过join将迭代器里的东西拼起来，然后再转为List
# 如果这个元素不在分隔符里什么也不做，否则就就把它搞成?   元素是12,345;789,145
values = "".join(char if char not in seperstors else "?" for char in number).split('?')

# 上面看不懂看这里这个a只是个声明
# values = "".join(a if a not in seperstors else "?" for a in number).split('?')


print(type(values))  # list
print(values)  # ['12', '345', '789', '145']

# 类型转换
print([str(val) for val in values])  # ['12', '345', '789', '145']
print([int(val) for val in values])  # [12, 345, 789, 145]
