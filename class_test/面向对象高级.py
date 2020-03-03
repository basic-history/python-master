#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
原始的版本，自己提供 类似 get_ set_ 一样的方法，注意，属性必须是 _开头的，这样直接操作属性就会报错
"""


class Student(object):

    def set_age(self, age):
        if not 0 < age < 100:
            raise RuntimeError
        self._age = age

    def get_age(self):
        return self._age


"""
高级版本
"""


class Student2(object):

    def __init__(self, age=0):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 0 < value < 100:
            raise RuntimeError


if __name__ == '__main__':
    # student = Student()
    # student._age = 180  # 这样不安全
    # print(student._age)  # 会有protected警告

    # student.set_age(1800)
    # print(student.get_age())

    student2 = Student2()
    # student2.age=18 #调用的是     @age.setter 这个方法  如果这个方法报错了，那么下面也获取不到这个属性会报错

    print(student2.age)
