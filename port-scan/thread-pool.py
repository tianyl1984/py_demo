# -*- coding: utf-8 -*-

import socket
import concurrent.futures
import time


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
    max_threads = 5000
    port_list = range(1, 65536)
    host = '127.0.0.1'
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(tcp_scan, host, port) for port in port_list]
        for future in concurrent.futures.as_completed(futures):
            pass
    end = time.time()
    print(f"total time:\t{(end - start)}")


if __name__ == "__main__":
    main()
