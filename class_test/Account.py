#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

"""
面向对象展示类
如果属性或者方法以_开头，则为protected，其他类不建议访问，因为是内部属性随时可能删除
如果属性或者方法以__开头，则调用会报错
"""


class Account(object):

    def __init__(self, name, balance=0):
        """
        初始化对象
        :param name:  姓名
        :param balance: 余额
        """
        self._name = name
        self._balance = balance
        self._trans_record = [('init', balance)]  # 交易记录
        print('create account for {} balance {}'.format(name, balance))

    def combine(self, amount):
        if amount > 0:
            self._balance += amount
            print('deposite balance {}'.format(amount))
            self._trans_record.append(('deposite', amount))
        else:
            self._balance += amount
            print('withdraw balance {}'.format(amount))
            self._trans_record.append(('withdraw', amount))

    def show_trans_record(self):
        for trans_type, amount in self._trans_record:
            print('时间{:>27} 交易类型{:>10}，金额{:>5}'.format(Account._current_time(), trans_type, amount))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        print('deposite balance {}'.format(amount))

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        print('withdraw balance {}'.format(amount))

    def show_balance(self):
        print('balance is {}'.format(self._balance))


    @staticmethod
    def _current_time():
        """
        静态方法，返回当前时间
        :return: 当前时间
        """
        return str(datetime.today())


if __name__ == '__main__':
    fw_account = Account('fw')
    fw_account.combine(10)
    fw_account.combine(-20)

    fw_account.show_trans_record()

    tim_account = Account('tim', 800)
    tim_account.show_balance()
    #   tim_account.__balance = 200  # 这里的修改是起作用的，但是不建议 如果是__则无效

    #  tim_account._Account__balance = 200    #黑科技，可以强制修改
    tim_account.deposit(100)
    tim_account.withdraw(200)
    tim_account.show_balance()

    print(tim_account.__dict__)        #{'_name': 'tim', '_balance': 700, '_trans_record': [('init', 800)]}