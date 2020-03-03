#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):

    def __index__(self):
        pass

    def run(self):
        print('animal is running')

    def name(self):
        return 'animal'


class Dog(Animal):
    arg1 = None

    def eat(self):
        print('eat meat..')

    """
    重写父类方法
    """

    def name(self):
        return 'dog'


def run_twice(animal):
    print(animal.name(), 'is running')
    print(animal.name(), 'is running')


if __name__ == '__main__':
    animal = Animal()
    animal.run()
    print(animal.name())

    print("animal是不是Animal {}".format(isinstance(animal, Animal)))

    dog = Dog()
    dog.run()
    dog.eat()
    print(dog.name())
    print("dog 是不是Dog {}".format(isinstance(dog, Dog)))  # true
    print("dog 是不是Animal {}".format(isinstance(dog, Animal)))  # true

    run_twice(animal)
    print('*' * 8)
    run_twice(dog)

    # 获得一个对象的所有属性和方法
    print(dog.__dir__())

    # hasattr 可以判断是否存在这个属性或者方法
    print('狗有{}属性吗?{}'.format('name', hasattr(dog, 'name')))
    print('狗有{}属性吗?{}'.format('eat', hasattr(dog, 'eat')))
    print('狗有{}属性吗?{}'.format('arg1', hasattr(dog, 'arg1')))
    print('狗有{}属性吗?{}'.format('arg2', hasattr(dog, 'arg2')))

    attr = getattr(dog, 'arg1')
    print(attr)  #None
