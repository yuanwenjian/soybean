#!/usr/bin/python3
# coding=utf-8

import pymysql

db = pymysql.connect(host='localhost', user="root", passwd="", db="soybean_test")
db.set_charset("utf8")
cursor = db.cursor()

for index in range(2, 20):
    print("创建t_"+str(index)+"表")
    sql = '''CREATE TABLE t_'''+str(index)+''' ( 
   chromosome varchar(50) DEFAULT NULL,
   position int(11) DEFAULT NULL COMMENT '位置',
   ref_base varchar(50) DEFAULT NULL COMMENT '参考碱基',
   allele varchar(50) DEFAULT NULL COMMENT '碱基',
   id bigint(20) NOT NULL AUTO_INCREMENT,
   PRIMARY KEY (id),
   KEY position (position)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8'''
    # cursor.execute('SET NAMES utf8;')
    # cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    db.commit()
    cursor.execute(sql)
    db.commit()
