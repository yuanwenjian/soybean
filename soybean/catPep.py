#!/usr/bin/python3.4
#coding=utf-8

import os
from os import path
import sys

# 使用脚本 ./split file outFile
file=open("/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/03_gene_structure/"+sys.argv[1]+"_final_pep.fa")
fileWrite=open("/run/media/bmk/dac173b0-250b-42e0-97f4-fdacd8941af2/work/soybean/soybean/soybean_data_analysis/03_gene_structure/"+sys.argv[1]+"_pep.change.fa","a")
count=0
newLine=""
while 1:
	line=file.readline()
	if not line:
		break
	if  line.startswith(">"):
		# fileWrite.write(line.strip())
		fileWrite.write("\n"+newLine)
		newLine=line
	else:
		newLine=newLine+line.strip()
		print("修改dev 分支=================dev")