#!/usr/bin/python3
# coding=utf-8

def split():
    result = ''
    fileWrite = open("issn.csv", "a")
    with open('/home/bmk/下载/J_Entrez.bin') as file:
        line = file.readline()
        while 1:
            line = file.readline()
            if not line:
                break
            if line.startswith("ISSN (Print)"):
                issn = line.strip().split(":")[1].strip()
            if line.startswith("ISSN (Online)"):
                onIssn = line.strip().split(":")[1].strip()
            if line.startswith("--"):
                if  onIssn and issn:
                    result = issn + "\t" + onIssn + "\n"
                    fileWrite.write(result)
                    result = ""

if __name__ =='__main__':
    split()