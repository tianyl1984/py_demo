# -*- coding: utf-8 -*-
import asyncio
import time


async def tcp_scan(host: str, port: int):
    try:
        async with sem:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=3)  # 创建TCP套接字
            print(f"{host}:{port} open")
            writer.close()
            await writer.wait_closed()
            await asyncio.sleep(0.1)
    except Exception as e:
        # print(e)
        # print(f"{host}:{port} close")
        # 端口不可用
        pass


async def main():
    start = time.time()
    port_list = range(1, 65536)
    host = '127.0.0.1'
    tasks = [tcp_scan(host, port) for port in port_list]
    await asyncio.gather(*tasks)    # 开启并发任务
    end = time.time()
    print(f"total time:\t{(end - start)}")

sem = asyncio.Semaphore(5000)

if __name__ == "__main__":
    asyncio.run(main())
