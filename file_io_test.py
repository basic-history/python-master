# 1.需要手动关闭流
# text_io = open("sample.txt.txt", 'r')
#
# for line in text_io:
#     if 'JAB' in line.upper():
#         print(line, end='')  # 不会换行，默认是\n
#
# text_io.close()

# 2.自动关闭，推荐

# with open('sample.txt.txt', 'r') as txt:
#     for t in txt:
#         print(t, end='')

# with open('sample.txt.txt', 'r') as txt:
#     l = txt.readlines()  # 可以在这里读取并转换为list，退出这里后流会关闭不能再操作txt
# #
# # for la in l:
# #     print(la, end='')
#
# for la in l[::-1]:  # 这种是翻转list的内容
#     print(la, end='')


# with open("sample.txt.txt") as sample:
#     sample_read = sample.read()  # 这种返回的是<class 'str'>
#     print(type(sample_read))
#
# for sr in sample_read[::-1]:  # 如果翻转的话是字符串都反了
#     print(sr, end='')

# 3.写文件
# list_language = ['java', 'c', 'php']
# with open('text.txt','w') as write_text:
#     for language in list_language:
#         print(language, file=write_text)

# 4.再读取写入的文件 这种得自己转换 不如我们自己拼list把\n去掉
# with open('text.txt', 'r') as reads:
#     read_readlines = reads.readlines()
#
# for readline in read_readlines:
#     print(readline, end='')

need_read = []
with open('text.txt', 'r') as reads:
    for r in reads:
        need_read.append(r.strip('\n'))

print(need_read)  # ['java', 'c', 'php']

for n in need_read:
    print(n)

# 5.追加文件   注意这个a
with open('append_file.txt', 'a') as append_file:
    for index in range(5):
        print('i am {}'.format(index), file=append_file)
    print("-" * 16, file=append_file)
