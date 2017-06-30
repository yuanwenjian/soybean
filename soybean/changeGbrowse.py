#!/usr/bin/python3.4
# coding=utf-8

import os
import sys

file = open(
    "/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/A_final_gff3")
fileWrite = open(
    "/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/A_change_gff3", "a")
lines=[]
line=''
while 1:
    line = file.readline()
    if not line:
        break
    lines = line.split("\t")

    if lines[2] == "gene":
        id=lines[0]
        line=lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[3]+"\t"+lines[4]+"\t"+lines[5]+"\t"+lines[6]+"\t"+lines[7]+"\tID="+lines[0]+";Name="+lines[0]+"\n"
        fileWrite.write(line)
    # elif lines[2] =="mRNA":
    #     id = lines[0]
    #     name=lines[8].split(";")[0]
    #     line=lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[3]+"\t"+lines[4]+"\t"+lines[5]+"\t"+lines[6]+"\t"+lines[7]+"\t"+name+";Parent="+id+"\n"
    # else:
    #     id = lines[0]
    #     name = lines[8].split(" ")[0]
    #     line=lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[3]+"\t"+lines[4]+"\t"+lines[5]+"\t"+lines[6]+"\t"+lines[7]+"\t"+name+lines[8].split(" ")[1]
    # fileWrite.write(line)
