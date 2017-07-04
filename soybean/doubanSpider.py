#!/usr/bin/python3
# coding=utf-8
import requests
import json
import codecs


def connect(url):
    fileName="/home/bmk/PycharmProjects/soybean/result/table.csv"
    response = requests.get(url, verify=False)
    movieStr = response.json()
    subjects=movieStr['subjects']
    result=''
    for ject in subjects:
        rate=ject['rate']
        title=ject['title']
        id=ject["id"]
        cover=ject["cover"]
        result= result+title+"\t"+rate+"\t"+id+"\t"+cover+"\n"
        print("写入 "+title+" 至文件")
        # movie = requests.get("https://movie.douban.com/subject/26605881/", verify=False)
        # with open("/home/bmk/PycharmProjects/soybean/result/"+title+".png","w") as image:
        #     img=requests.get(ject["url"],verify=False).content
        #     image.write(image)

    with open(fileName,"a") as fileName:
        fileName.write(result)

for index in range(0,25):
    types=["美剧", "英剧", "韩剧", "日剧", "国产剧", "港剧", "日本动画", "综艺"]
    for type in types:
        url='https://movie.douban.com/j/search_subjects?type=tv&tag='+type+'&sort=recommend&type=tv&page_limit=20&page_start='+str(index*20)
        print("url="+url)
        connect(url)



