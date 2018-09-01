# coding：utf-8
import requests
import json
import ssl
import os
import sys
import time
import re
import urllib
import threading
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
def deal(html,start,end):
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
    path = 'bilibili图片'+str(start)+'-'+str(end)
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



def bilibili_paichong(start,end):



    # url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=6863049"
    # html = send(url)
    # deal(html)
    # print(img_url.split(".")[-1])
    error_num = []
    # for num in range(2500,6882200):
    for num in range(start,end):
        try:
            # url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id="+str(num)
            url = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id="+str(num)
            html = send(url)
            deal(html,start,end)
        except:
            print("%s有异常"%num)
            error_num.append(num)
            # print(error_num)
            continue

# 创建两个线程
def start(start,end):
    arr = []
    for i in range(start, end, 1000):
        arr.append(i)
    print(arr)
    paichong1 = threading.Thread(target=bilibili_paichong,args=(arr[0],arr[1]) )
    paichong2 = threading.Thread(target=bilibili_paichong,args=(arr[1],arr[2]) )
    paichong3 = threading.Thread(target=bilibili_paichong, args=(arr[2], arr[3]))
    paichong4 = threading.Thread(target=bilibili_paichong, args=(arr[3], arr[4]))
    paichong5 = threading.Thread(target=bilibili_paichong, args=(arr[4], arr[5]))
    paichong6 = threading.Thread(target=bilibili_paichong, args=(arr[5], arr[6]))
    paichong7 = threading.Thread(target=bilibili_paichong, args=(arr[6], arr[7]))
    paichong8 = threading.Thread(target=bilibili_paichong, args=(arr[7], arr[8]))
    paichong9 = threading.Thread(target=bilibili_paichong, args=(arr[8], arr[9]))
    paichong10 = threading.Thread(target=bilibili_paichong, args=(arr[9], end))



    paichong1.start()
    paichong2.start()
    paichong3.start()
    paichong4.start()
    paichong5.start()
    paichong6.start()
    paichong7.start()
    paichong8.start()
    paichong9.start()
    paichong10.start()
    # paichong1.join()
    # paichong2.join()
    # print ("退出主线程")

# arr = []
# for i in range(740000,750000,1000):
#     arr.append(i)
# print(arr)
start(800000,820000)