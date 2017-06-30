#!/usr/bin/python
# coding=utf-8

import os

files=["A","B","C","D","E","F","F"]

for file in files:
    lowName=file.lower()
    os.system("cp /share/nas1/xiayh/Species_database/dadou/Soybean_data_analysis/02_final_assembly_version/"+files+".fa /var/lib/gbrowse2/databases/soybean_"+lowName+"_scaffolds/")