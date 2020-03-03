def print2():
    print('我是你爹')


def print3(text):
    print('我是你爹', text)


def print4(text, name='fw'):
    print('我是你爹', text, name)


def print5(*args):
    for arg in args:
        print(arg)
    print('我是你爹', args)
    print('最后的join'.join(args))


print2()
print3('sb')
print4('sb')
print5('dp', 'ple')


# 记住这个基本就没问题了，看下面的还可以反哦
def test(*args, first='', name='fw', age=18, init=True):
    print(type(args))  # <class 'tuple'>
    print(args)
    print(first)
    print(name)


test('a', 'b', name='hehe', first='second')
