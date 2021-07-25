import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
import bs4
import requests
import argparse
import os
import pandas as pd
import time
from datetime import datetime as kk
import datetime
ls=[]
mydict={}
def convert_date():
    yy = int(input("\n\tENTER YOUR YEAR: \n"))
    d1 = datetime.date(yy, 1, 1)
    d2 = datetime.date(yy, 12, 31)
    days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]
    for day in days:
        cur=str(day.year)+str(day.month)+str(day.day)
        mydict[cur]=0

    ls.reverse()
    for timestamp in ls:
        day = kk.fromtimestamp(timestamp)
        if day.year == yy:
            cur =str(day.year)+str(day.month)+str(day.day)
            mydict[cur]+=1

    for value in mydict.values():
        print(value)

def get_sub_time():
    json_data = requests.get('https://codeforces.com/api/user.status?handle=SU_N_NY').json()
    res = json_data['result']
    rem=[]
    for i in res:
        if i['verdict'] == 'OK':
            if rem.count(i['problem']['name'])==0:
                ls.append(i['creationTimeSeconds'])
                rem.append(i['problem']['name'])

get_sub_time()
convert_date()

