# 思路
# 拿到页面源代码  需要requests模块
# 通过正则表达式提取想要的有效信息  需要re模块

import requests
import re
import csv

url = "https://movie.douban.com/top250"
num = 0
while num < 250:
    param = {
        "start": 0,
        "filter": "",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    resp = requests.get(url, headers = headers,params = param)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r' <li>.*?<span class="title">(?P<name>.*?)</span>.*?<b'
                     r'r>(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp.*?<sp'
                     r'an class="rating_num" property="v:average">(?P<score>.*?)</s'
                     r'pan>.*?<span>(?P<people>.*?)人评价</span>',re.S)

    result = obj.finditer(page_content)
    f = open("data.csv", mode = "w",encoding="UTF-8")
    csvwriter = csv.writer(f)
    for i in result:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    num+=25

f.close()
print("over!!!")