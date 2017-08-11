#!/usr/bin/python3.4
# -*- coding:utf-8 -*-
''' test'''
from urllib import request


def server():
    lines = request.urlopen("http://python.jobbole.com/81478/")
    for line in lines:
        print(line.decode("utf-8"))

server()
