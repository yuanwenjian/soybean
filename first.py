#!/usr/bin/python
# coding=utf-8

import os;

# path="/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/大豆数据库/soybean/back/ALL_PNG/"
# fileName=[]
# file=open("/home/bmk/soybean/soybeanImgNull.csv") 
# while 1:
#     line=file.readline()
#     name=line.strip()
#     if not line:
#         break
#     if  os.path.exists(path+name+".png"):
#         print(name+"  图片存在")
#         fileName.append(name)


# print(len(fileName))
# filePath="/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/大豆数据库/soybean/png.txt"
# pngFile=open(filePath,"a+")
# for name in fileName:
#     pngFile.write(name+"\n")


path = "/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/大豆数据库/soybean/ALL_PNG/"
file = open("/home/bmk/soybean/soybeanImgNotNull.csv")
count = 0
while 1:
    line = file.readline()
    if not line:
        break
    array = line.strip().split("\t")
    name = array[1]
    ida = array[0]
    if os.path.exists(path + name + ".png"):
        # print("当前  "+name+"  图片存在,重命名为"+ida)
        os.rename(path + name + ".png", path + ida + ".png")
        count = count + 1
    else:
        print("当前 " + name + " 图片不存在")
print(count)
