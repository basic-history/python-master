#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import pexpect

"""
python3 /Users/pleuvoir/dev/space/python/python-master/pexpect_test.py
"""
from totp_util import get_auth_code


if __name__ == '__main__':
    code = get_auth_code('1')
    print(code)
    child = pexpect.spawnu('ssh -i ~/dev/support/djs/fuwei.pem fuwei@djs.djdns.cn')
    print(1)
    expect = child.expect('auth',pexpect.TIMEOUT)
    print(2)
    if expect != 0:
        print('请连接VPN后再试。。。')
        exit(-1)

    print("准备输入谷歌口令。")
    time.sleep(0.1)

    child.sendline('123')
    print('已发送')

    child.interact()
