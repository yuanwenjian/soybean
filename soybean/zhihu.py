#!/usr/bin/python3
#coding=utf-8

import requests

url='https://www.zhihu.com/question/39731953'
cookies={'cookies':'_zap=f3dc53e0-109d-4af8-834e-9211bd04abe2; d_c0="ADDCJZ2ZFguPTn8ehYHr6_M5zbIeixyvStk=|1483275224"; _zap=d0f7c328-881d-44b6-acee-d7e15ae57cd3; _ga=GA1.2.601320109.1491663111; aliyungf_tc=AQAAAFzkZnIP1wIA+hRHeXFQASiVOJNw; q_c1=e603c86fd8b2467488aa815b96c051d8|1498892426000|1483275224000; q_c1=e603c86fd8b2467488aa815b96c051d8|1498892426000|1483275224000; l_cap_id="MDNkNGRmODBhYmMyNGE5ZmFlNTI2NWRjNTZjMGUwOTE=|1498920603|4838c2f3cbb42c5abc873afffab039f6a83b138f"; r_cap_id="ZDFiNTBkZWVkZjYxNGRmNWFlYjcyM2YwODFjMmYzMzY=|1498920603|abe0988858cd432d3ac5bcc536e197d60c61b0c3"; cap_id="NTUzOWI0NDA5NzMxNGYwNDlhMjU5MTFhZGJkZDdlMzA=|1498920603|e1db21a2c514a48ede8c503e01efd1ede6b42390"; capsion_ticket="2|1:0|10:1498922051|14:capsion_ticket|44:ODJiNTkxY2U3ZmMxNDZlOWJkOTFlZmI4YTVkMjgxMGM=|8523d3510d2f8d36aef6a60096e1fc86c42b631cd248fb6b3cda111a07f9fdd6"; z_c0="2|1:0|10:1498922055|4:z_c0|92:Mi4wQUFEQTJ3U01sQWtBTU1JbG5aa1dDeVlBQUFCZ0FsVk5SMGxfV1FCX1JHUWRoTUFfQXFjVDVwQ0tZbTRSSm1qOG93|e0687b3b740f82d6de2c417d8020e6e98a1f1751fce4a4a99c9ea246a264ba89"; s-q=%E6%B0%94%E8%B4%A8; s-i=3; sid=uc5119ko; __utma=51854390.601320109.1491663111.1498924046.1498975440.2; __utmb=51854390.0.10.1498975440; __utmc=51854390; __utmz=51854390.1498975440.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/yuan-wen-jian-21/activities; __utmv=51854390.100--|2=registration_date=20160308=1^3=entry_date=20160308=1; _xsrf=7a89fb89-e03b-4a02-8e02-9a10d0c0ea11'}

head={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch, br',
		'Connection':'keep-alive',
		'Cookie':'_zap=f3dc53e0-109d-4af8-834e-9211bd04abe2; d_c0="ADDCJZ2ZFguPTn8ehYHr6_M5zbIeixyvStk=|1483275224"; _zap=d0f7c328-881d-44b6-acee-d7e15ae57cd3; _ga=GA1.2.601320109.1491663111; aliyungf_tc=AQAAAFzkZnIP1wIA+hRHeXFQASiVOJNw; q_c1=e603c86fd8b2467488aa815b96c051d8|1498892426000|1483275224000; q_c1=e603c86fd8b2467488aa815b96c051d8|1498892426000|1483275224000; l_cap_id="MDNkNGRmODBhYmMyNGE5ZmFlNTI2NWRjNTZjMGUwOTE=|1498920603|4838c2f3cbb42c5abc873afffab039f6a83b138f"; r_cap_id="ZDFiNTBkZWVkZjYxNGRmNWFlYjcyM2YwODFjMmYzMzY=|1498920603|abe0988858cd432d3ac5bcc536e197d60c61b0c3"; cap_id="NTUzOWI0NDA5NzMxNGYwNDlhMjU5MTFhZGJkZDdlMzA=|1498920603|e1db21a2c514a48ede8c503e01efd1ede6b42390"; capsion_ticket="2|1:0|10:1498922051|14:capsion_ticket|44:ODJiNTkxY2U3ZmMxNDZlOWJkOTFlZmI4YTVkMjgxMGM=|8523d3510d2f8d36aef6a60096e1fc86c42b631cd248fb6b3cda111a07f9fdd6"; z_c0="2|1:0|10:1498922055|4:z_c0|92:Mi4wQUFEQTJ3U01sQWtBTU1JbG5aa1dDeVlBQUFCZ0FsVk5SMGxfV1FCX1JHUWRoTUFfQXFjVDVwQ0tZbTRSSm1qOG93|e0687b3b740f82d6de2c417d8020e6e98a1f1751fce4a4a99c9ea246a264ba89"; s-q=%E6%B0%94%E8%B4%A8; s-i=3; sid=uc5119ko; __utma=51854390.601320109.1491663111.1498924046.1498975440.2; __utmb=51854390.0.10.1498975440; __utmc=51854390; __utmz=51854390.1498975440.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/yuan-wen-jian-21/activities; __utmv=51854390.100--|2=registration_date=20160308=1^3=entry_date=20160308=1; _xsrf=7a89fb89-e03b-4a02-8e02-9a10d0c0ea11',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
		}

r=requests.get(url,headers=head)
print(r.text)
