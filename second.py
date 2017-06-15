#!/usr/bin/python3.4
# coding=utf-8

import os

path = "/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/大豆数据库/soybean/back/ALL_PNG/"

os.rename(path + "皖豆25.png", path + "皖豆25(杂优豆1号).png")
os.rename(path + "交选1号.png", path + "交选1号(上农298).png")
os.rename(path + "淮豆.png", path + "淮豆(黑)5号.png")
os.rename(path + "晋豆.png", path + "晋豆(鲜食)33.png")
os.rename(path + "交选2号.png", path + "交选2号(上农4号).png")
# fileList=os.listdir(path)

# for file in fileList:
# 	if not file.find(" ") ==-1:
# 		name=file.replace(" ","")
# 		os.rename(path+file,path+name)#重命名
# 		print(file+"包含空格")


# import sys
# for arg in range(len(sys.argv)):
# 	print("参数为:\t"+sys.argv[arg])

# from itertools import islice    
# input_file = open("/home/bmk/bin/python/first.py")    
# for line in islice(input_file, 100, None):    
#     print(line)
