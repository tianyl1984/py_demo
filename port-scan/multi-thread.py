# -*- coding: utf-8 -*-

import socket
import threading
import time


class ScanThread(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        tcp_scan(self.host, self.port)


def tcp_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    ret = sock.connect_ex((host, port))
    sock.close()
    if ret == 0:
        print(f"{host}:{port} open")
    else:
        pass


def main():
    start = time.time()
    port_list = range(1, 65536)
    host = '127.0.0.1'
    thread_task = [ScanThread(host, port) for port in port_list]
    for t in thread_task:
        t.start()
    for t in thread_task:
        t.join()
    end = time.time()
    print(f"total time:\t{(end - start)}")


if __name__ == '__main__':
    main()
