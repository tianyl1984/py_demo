#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 处理西咸社会停车场key '

def process_line(line):
    line = line.strip()
    if ('  ' in line):
        line = line.replace('  ', ' ')
        return process_line(line)
    return line

def start():
    with open('C:/Users/tianyale/Desktop/xixian.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = process_line(line)
            parkId = line
            locationId = ''
            companyCode = ''
            if (' ' in line):
                parkId = line.split(' ', 3)[0]
                locationId = line.split(' ', 3)[1]
                companyCode = line.split(' ', 3)[2]
            print(f"insert into parking_garage_key(park_id,location_id,company_code) values ('{parkId}','{locationId}','{companyCode}');")
            # print(line)

start()
