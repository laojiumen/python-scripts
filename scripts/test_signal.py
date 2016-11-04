# -*- coding: utf-8 -*-
"""
signal信号和linux信号一致，通过 man 7 signal 查询
程序自身只能发送alarm信号
无法注册SIGKILL信号
详情参考python signal或者 man 7 signal
"""

# # # ==========================SIGTSTP===================================
import signal
# # Define signal handler function
# def myHandler(signum, frame):
#     print('I received: ', signum)
#
# # 接收到停止输入信号，就回调。 control-z
# signal.signal(signal.SIGTSTP, myHandler)
# signal.pause()
# print('End of Signal Demo')


# # # ==========================SIGALRM===================================
# import signal
# import time
# # Define signal handler function
# def myHandler(signum, frame):
#     print("Now, it's the time: ", time.time() - old_time)
#     exit()
#
# # register signal.SIGALRM's handler
# signal.signal(signal.SIGALRM, myHandler)
# # 5秒后发送SIGALRM信号，非阻塞
# signal.alarm(5)
# old_time = time.time()
# while True:
#     print('not yet')
