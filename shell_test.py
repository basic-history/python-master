#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
/Users/pleuvoir/dev/space/python/python-master/shell_test.py
"""

if __name__ == '__main__':
    # 不会捕获输出
    # completed_process = subprocess.run(["ls", "-l"])
    # print(completed_process) #CompletedProcess(args=['ls', '-l'], returncode=0)

    # 和linxu下操作一样
    # subprocess_run = subprocess.run('ls -l', shell=True)  #也可以这样更符合linux下的操作，但是存在注入风险
    # print(subprocess_run)  #CompletedProcess(args='ls -l', returncode=0)

    # 捕获输出，终端没什么显示
    # ifconfig_out = subprocess.run("ifconfig", shell=True, stdout=subprocess.PIPE)  # 捕获输出，屏幕上不会输出了
    # print(ifconfig_out.stdout.decode('GBK'))

    #进入命令行模式 写入下面的内容并执行
    # s = subprocess.Popen("python3", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    # s.stdin.write(b"import os\n")
    # s.stdin.write(b"print(os.name)\n")
    #
    # print__encode = "print('你好啊')".encode('UTF-8')
    # s.stdin.write(print__encode)
    # s.stdin.close()
    #
    # out = s.stdout.read().decode("UTF-8")
    # s.stdout.close()
    # print(out)
    print()