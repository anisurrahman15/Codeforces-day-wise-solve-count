import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
import bs4
import requests
import argparse
import sys
import os
import pandas as pd
import time
from datetime import datetime
date = []
ls=[]
solve_cnt=[]
mydict={}
def convert_date():
    ls.reverse()
    pre=-1
    cnt=0
    rem=ls[0]
    yy=int(input("\n\tENTER YOUR YEAR: "))

    for timestamp in ls:
        a = datetime.fromtimestamp(timestamp)
        if a.year==yy:
            if a.day==pre or pre==-1:
                cnt=cnt+1
            else:
                m = str(rem.month)
                d = str(rem.day)
                ss=m+' '+d
                mydict[ss]=cnt
                cnt=1
            pre=a.day
            rem=a

    tot=0
    for k, v in mydict.items():
        print(k, v)
        tot += int(v)

    print("\n\ttotal solve: ", tot)

def get_sub_time():

    json_data=requests.get('https://codeforces.com/api/user.status?handle=SU_N_NY').json()
    res=json_data['result']
    prev_pb = ''
    cur_pb = ''
    for i in res:
        if i['verdict'] == 'OK':
            cur_pb = i['problem']['name']
            if cur_pb != prev_pb:
                ls.append(i['creationTimeSeconds'])
                prev_pb = i['problem']['name']

get_sub_time()
convert_date()
