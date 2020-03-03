# 写二进制文件的多种方法

with open("binary", 'bw') as binary_file:
    for i in range(16):
        binary_file.write(bytes([i]))  # 注意这个 （） 括号不能丢

with open('binary', 'br') as binary_file2:
    for b in binary_file2:
        print(b)

print()
with open("binary2", 'bw') as binary_file:
    binary_file.write(bytes(range(16)))  # 注意这个 （） 括号不能丢

with open('binary2', 'br') as binary_file2:
    for b in binary_file2:
        print(b)

### 可以先不看
# 必须把这个参数拎出来写
a = 65534
with open("binary3", 'bw') as binary_file3:
    binary_file3.write(a.to_bytes(2, 'big'))

with open("binary3", 'br') as binary_file3:
    for i in binary_file3:
        print(i)

print()
# 返回表示整数的字节数组
to_bytes = a.to_bytes(5, 'big')  # byteorder must be either 'little' or 'big'
print(to_bytes)
