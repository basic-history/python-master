#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class User(object):
    const = '常量'

    def __init__(self, name, age, hobby, arg1, arg2):
        self.name = name
        self.age = age
        self.hobby = hobby
        self._arg1 = arg1
        self.__arg2 = arg2
        self.on = False

    def switch_on(self):
        self.on = True

    @staticmethod
    def _change_const(arg):
        User.const = arg

    def print_show(self):
        print(self.const)
        random_randint = random.randint(0, 5)
        print("变为{}".format(random_randint))
        User._change_const(random_randint)
        print(self.const)


if __name__ == '__main__':
    user = User('fw', 18, '打游戏', '参数1', '参数2')
    print('_arg1一个下划线的可以访问 类似于protected的，python建议把它搞成@property，如果直接辅助的话没提示', user._arg1)

    try:
        print(user.__arg2)
    except AttributeError:
        print('__arg2 这个参数有两个下划线不能访问')
    print(user.on)

    user.on = True
    print(user.on)  # True

    # 重新创建一个
    user2 = User('fw2', 18, '打游戏', '参数1', '参数2')
    print(user2.on)
    user2.switch_on()
    print(user2.on)
    user2.on = False

    print(user.const)
    print(user2.const)
    user2.const = 3
    print(user2.const)

    # 静态方法只能在类里面调用？？
    user.print_show()

    print(user.__dict__)
