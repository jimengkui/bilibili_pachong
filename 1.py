# coding：utf-8
import requests
import json
import ssl
import os
import sys
import time
import re
import urllib
def send(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    # url = 'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=6663049'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                  "Connection":"keep-alive",
                  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                  "Accept-Language":"zh-CN,zh;q=0.8"}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.json()
    return html
def deal(html):
    # print(html['data']['item']['title'])
    user_name = html['data']['user']['name']
    upload_time = str(html['data']['item']['upload_time'])
    # print(str(upload_time))
    year = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[0])
    month = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[1])
    date = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[2])
    hour = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[3])
    minute = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[4])
    second = str(time.strptime(upload_time, "%Y-%m-%d %H:%M:%S")[5])

    Upload_time = year+'年'+month+'月'+date+'日'+hour+"时"+minute+'分'+second+"秒"
    # print(Upload_time)
    # print(upload_time )
    title = html['data']['item']['title']
    if title=="":
        title = "无"
    img_url = html['data']['item']['pictures'][0]['img_src']
    img_len = len(html['data']['item']['pictures'])
    # print(len(html['data']['item']['pictures']))
    suffix_arr = ['jpg','png','gif','webp']
    suffix = img_url.split(".")[-1]
    path = 'bilibili图片700000-710000'
    # user_word = {}
    if not os.path.isdir(path):
        print(1)
        os.makedirs(path)
    for num in range(0,img_len):
        img_url = html['data']['item']['pictures'][num]['img_src']
        # print(sys.path[0])

        for suffix_i in suffix_arr:

            if suffix ==suffix_i:
                image = requests.get(img_url).content
                # print(image)

                with open(sys.path[0]+'/'+path+'/'+'上传者：'+user_name+'；图片标题：'+title+'；上传时间：'+Upload_time+'；_'+str(num)+'.'+suffix_i, 'wb') as f:
                    f.write(image)
                f.close()
            else:
                pass



# url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=6863049"
# html = send(url)
# deal(html)
# print(img_url.split(".")[-1])
error_num = []
# for num in range(2500,6882200):
for num in range(700000,710000):
    try:
        # url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id="+str(num)
        url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id="+str(num)
        html = send(url)
        deal(html)
    except:
        print("%s有异常"%num)
        error_num.append(num)
        # print(error_num)
        continue
