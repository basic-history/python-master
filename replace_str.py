text = "i am {0},my age is {1}"

print(text.format('pleuvoir', 18))

print("i am", 'pleuvoir', ",my age is", 18)  # 中间会自动加空格
print("i am " + "pleuvoir " + "my age is " + str(18))

print("1:{0},2:{1},3:{2}".format(1, 2, 3))

print("""
1月有{0}天
2月有{1}天
3月有{0}天""".format(31, 28))

# 1月有31天
# 2月有28天
# 3月有31天

sum = 10
print(f"这个月有{sum}天")
