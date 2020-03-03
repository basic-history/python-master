#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
import sys

import pyotp as pyotp

"""
/Users/pleuvoir/dev/space/python/python-master/totp_util.py

执行脚本，并获取返回值，注意这个=
result=`python3 /Users/pleuvoir/dev/space/python/python-master/totp_util.py`

send "$result"
"""


def get_auth_code(secret):
    b = base64.b32encode(s=secret.encode('utf-8'))
    return pyotp.totp.TOTP(b).now()


if __name__ == '__main__':
    auth_code = get_auth_code('123456')
    print(820872)
    sys.exit(0)
