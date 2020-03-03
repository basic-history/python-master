for i in range(1, 13):
    print("{0}的平方={1}，{0}的立方={2}".format(i, i ** 2, i ** 3))

print()
print("文本{0}，文本{1}".format("a", "b"))
# 文本a，文本b
print("文本{0:<3}，文本{1}".format("a", "b"))  # 连接后再空格
# 文本a  ，文本b
print("文本{0:>3}，文本{1}".format("a", "b"))  # 空格后再连接
# 文本  a，文本b
