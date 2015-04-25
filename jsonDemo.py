#coding:utf-8
import urllib
import urllib2
import json

url = "https://api.douban.com/v2/movie/search?q=%E5%8D%81%E9%9D%A2"

req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()

res_json = json.loads(res)

print res_json["total"]

for (i,subject) in enumerate(res_json["subjects"]):
	print subject["id"] + ":" + subject["title"]



