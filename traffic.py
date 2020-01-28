# -*- coding:utf-8 -*-
import os
import re
import time


os.system("vnstat -m -i eth1 > /root/tx.txt")
time.sleep(1) 

def get_now_month():
    now_month_num = time.strftime("%m")
    num_to_en = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Dec'}
    return num_to_en[now_month_num]

f = []
for line in open("/root/tx.txt"):
    f.append(line),

def ftext():
    for i in range(0,len(f)):
        if re.search(get_now_month(),f[i]):
            return f[i]

tx =  re.findall(r"\|(.*?)\|",ftext())[0]
if re.search(r"TiB",tx): 

    tx_data =  float(re.sub(r"\s","",tx)[:-3])
    if tx_data > 2: 
        os.system("date=`date +%Y-%m-%d_%H:%M:%S` && echo ${date}' 服务器出向流量已超过，自动关闭shadowsocks' >> /root/stopss.log")
	os.system("shutdown -h now")
    else:
        cmd = "date=`date +%Y-%m-%d_%H:%M:%S` && echo ${date}' 服务器当前已使用流量 "+str(tx_data)+" TiB' >> /root/stopss.log"
        os.system(cmd)
else:pass
