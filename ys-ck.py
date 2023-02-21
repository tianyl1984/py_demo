#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 分析 '

from urllib import parse
from urllib import request
import time
import json

target_url = 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog?win_mode=fullscreen&authkey_ver=1&sign_type=2&auth_appid=webview_gacha&init_type=301&gacha_id=666e99c499de824cf10211511d3c2ad3b48cf38d&timestamp=1673997960&lang=zh-cn&device_type=pc&game_version=CNRELWin3.4.0_R12875869_S12901190_D13021296&plat_type=pc&region=cn_gf01&authkey=Ee1z5GAVieocXPzN63sT8DuUKoX5Y9LAGj%2fmgez2C%2foe1EVjnvhqOp38ww0vVZcNOgrMfgqAqm6jcZxWaw06LdJ%2bGBRUbzAb2N%2bBgXDaqGFl%2fipN0Of94wBzSyktlI6LupsIeAqkuD7JhJxXbCUJ5I%2frhW4Sf6%2fHD9ZpwVlPimVvdJnpWHdd3CvY0%2bxc2cHTCn3klg8%2b%2bCpwQIhVXMeeE5WReTkPS6Bgfm5Ec7eZ%2bv%2fQLJkEPkmd5P5GeGd404kLpOKRYHcAV57DRga06cb0udDO59%2bGG12A%2b12z%2f9X5DgLUB5jRk25JK2uvpCuqLgln9i8sHtv57G2oe7qWRDyKlUROQOEUKERhBRG2yu1IeNzk7vbBmBAT8DRmElAKbG%2b2D8sAtcr6%2fCgKZ00Qw6TKzYC9Hk1w5QavFG71t7gAvAjsX0tIpJZUqZziFOCnzCFA9Y8MPz34bORgc%2f%2fe%2fRXEM1XbUPYF2tIfSTGgQeqVoGXqU4c6iT%2bvwxnUPUMi5wnbLsVUUXWL%2bP%2fO9ltb%2bAf5FBlqGf33tIeD1QdQcngNXAvazWc6KoEciWw2A0j9gDZbN8XXmdKgfE0i2csa%2ba3wLBcVTMYC8L8xAOGX5ZT1dqvLC32TD9Ov2LlirIZJd01y3iATbbnYlPvYb%2f662%2fMAyOJaG8x60QtxwY7dycWmvw7io%2bkf%2fgU5T8UblwcS60uHobiNNoKsdqJlJgMdupROWVTf8Ji1bMayHL0jphlW09SzgKtdB%2blwNC%2fI56mcUeH%2bPpoCuvHGNVPV%2bPLefcQOgt5TBljIBwmj1KL3eDG7Qhh9oZ4gBIs5kaXsbsvVn9CtzHvznlaTn9tsxmu8wmvR7xtmRTLe1gIc6P3XSS7M%2fSDB8Y1ttTr83HUnA63SPDXbrmH4F5ZpFrQJ4g2Rj%2f%2bqyF8%2bnsaa2RkK9rhX%2byZVohFW7aZRvT00y9im9cEHe8704LbhRmO49CdokkHwOq6sfBqETjjk1irU0y%2fWB6eEjVv0aszywbAGjTXOxeA2IJBZQXCJZ4R3s0c23jZVFH8GH%2bFqcwWXR%2fQnBKYrdl1qdwc47Y%2fuAd8kjqaW%2f%2fk6JnqIdFkGPBQt00hQfBAzkOkJwQ6I6f6RcBhCOc1PNDva3gTl0m%2fAE1wYO1Q2HgIX7of2SBhFqJ22lQmufgXrsFl10GD1Ymh5elLXl84LRxQCORAADH2OhVxcohLZwGfvn8nX417R%2f333y7%2b8QUqiSEoxfvJwdgP6dQK4E6BBnXS3czzxNcvi2zxpFQ2DSq4Gu60gS3DEA9Ke9ncU424mQJLO0BydoqncgfxBgu4XOHmH1pOJBnCWs5Qbh1S1FITWVxjdW1abJ6Mv1SRHiwVJ4imRVg%3d%3d&game_biz=hk4e_cn&gacha_type=301&page=1&size=5&end_id=0'

def req(url):
    # print(url)
    req = request.Request(url)
    req.add_header("accept", "application/json")
    with request.urlopen(req) as f:
        if f.status != 200 :
            print('请求出错:', f)
            raise RuntimeError('请求出错')
        data = f.read()
        # print('status:', f.status, f.reason)
        result = data.decode('utf-8')
        return result

def save_file(data):
    with open('./ys.json', 'a', encoding='utf-8') as f:
        f.write(data)
        f.write('\n')

def parse_end_id(data):
    result = json.loads(data)
    if (result['retcode'] != 0) :
        raise RuntimeError('retcode异常:' + data)
    datalist = result['data']['list']
    size = len(datalist)
    if (size == 0) :
        return -1
    return datalist[size - 1]['id']

def query_log():
    pr = parse.urlparse(target_url)
    query = parse.parse_qs(pr.query)
    endId = '0'
    page = 0
    while True:
        page = page + 1
        query['page'] = [page]
        query['end_id'] = endId
        print(f'query page:{page},endId:{endId}')
        query_new = parse.urlencode(query, doseq=True)
        pr = pr._replace(query=query_new)
        new_url = parse.urlunparse(pr)
        print('request page ', page)
        data = req(new_url)
        save_file(data)
        endId = parse_end_id(data)
        if (endId == -1) :
            break
        time.sleep(5)


query_log()
