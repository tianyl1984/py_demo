# -*- coding: utf-8 -*-

import socket


def tcp_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    ret = sock.connect_ex((host, port))
    sock.close()
    if ret == 0:
        print(f"{host}:{port} open")
    else:
        pass


tcp_scan("127.0.0.1", 6767)
