#!/usr/bin/python3
# coding=utf-8

import requests
import json
import pymysql
from bs4 import BeautifulSoup


class Movie():
    def __init__(self,data):
        print(data)
        self.__dict__=data
def collectIds(url):
    spon = requests.get(url)
    html = BeautifulSoup(spon.content)
    dict = {"data-act": "movie-click"}
    movies = html.find_all("a", dict)
    for movie in movies:
        movieId = str(movie["data-val"])
        id = movieId.split(":")[1].replace("}", "")
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': "_lx_utm=; __mta=156627460.1499223039988.1499223039988.1499223039988.1; iuuid=0B778C79BA76884ABE831512DBE1746E95ED37A720F987A0E1A08215C073D43C; JSESSIONID=ynx52l9v8swikywkvi77zmwt; ci=1; curci=1; latlng=40.120375,116.609207,1499223944185; _lx_utm=; revrev=76338a29; isWebp=0; __mta=156627460.1499223039988.1499223039988.1499223946557.2; __utma=17099173.1480034428.1499223944.1499223944.1499223944.1; __utmc=17099173; __utmz=17099173.1499223944.1.1.utmcsr=jianshu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/9855610eb1d4",
            'Host': 'm.maoyan.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
        }
        response = requests.get("http://m.maoyan.com/movie/" + id + ".json", headers=head)
        result = response.json()
        jsonMovie = result["data"]['MovieDetailModel']
        movieObj=movie(jsonMovie)
        insertMysql(movieObj)
    print("当前一页写入完成")


def insertMysql(movie):
    db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="splider")
    db.set_charset("utf8")
    curosr = db.cursor()
    sql="insert into t_movie (name,cat,dir,dra,img,score,snum,star) VALUES (movie.nm,movie.cat,movie.dir,movie.dra,movie.img,movie.sc,movie.snum,movie.start)"


if __name__ == '__main__':
    for index in range(0, 500):
        collectIds("http://maoyan.com/films?showType=1&offset=" + str(index * 30))
