# coding:utf-8
import select
import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', 50000))
serversocket.listen(1)
serversocket.setblocking(0)
epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)
try:
    connections = {}
    requests = {}
    responses = {}
    while True:
        # 每秒拉取已经完成的任务
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                print 'connect'
                connection, address = serversocket.accept()
                connection.setblocking(0)
                # 如果是serversocket 传过来的消息，则有新连接，那么将新连接注册到epoll里
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            # 当socket连接受到数据，会触发可读
            elif event & select.EPOLLIN:
                print 'read'
                message = connections[fileno].recv(1024)
                requests[fileno] += message
                # EOL1 和 EOL2 是结束标识
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    # client输入结束， server需要输出， 切换fileno的状态到输出
                    epoll.modify(fileno, select.EPOLLOUT)
                    connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
                    print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
                    continue
                if not message.strip():
                    print 'lost connect'
                    epoll.unregister(fileno)
                    del responses[fileno]
                    continue
            elif event & select.EPOLLOUT:
                print 'out'
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 0)
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                print 'stop'
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    print 'unregister'
    epoll.unregister(serversocket.fileno())
