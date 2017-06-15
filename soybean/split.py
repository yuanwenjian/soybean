#!/usr/bin/python
#coding=utf-8

import os
import sys

# 使用脚本 ./split file outFile
file=open("/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/03_gene_structure/"+sys.argv[1]+"_pep.change.fa")
fileWrite=open("/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/03_gene_structure/"+sys.argv[1]+"_pep.csv","a")
currentLine=""
count=0
while 1:
	line=file.readline()
	if not line:
		break
	if  line.startswith(">"):
		count = count+len(line)
		currentLine=line.strip().split(">")[1]
	else:
		name=currentLine+"\t"+str(count)+"\t"+str(count+len(line))+"\t"+sys.argv[1]+"\n"
		count=count+len(line)
		fileWrite.write(name)