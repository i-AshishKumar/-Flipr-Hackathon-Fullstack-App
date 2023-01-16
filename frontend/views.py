from datetime import datetime

import pandas as pd
import requests as rq
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64


# Create your views here.

def home(request):    
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def notRegistered(request):
    return render(request,'notregistered.html')

def login(request):
    return render(request,'login.html')


def nsebse(request):
    if request.user.is_authenticated:
        endpoint1 = rq.get('http://localhost:8000/api/bse/').json()
        endpoint2 = rq.get('http://localhost:8000/api/nse/').json()
        bseData = helper(endpoint1)
        nseData = helper(endpoint2)
        return render(request,'nsebse.html',{'bseData':bseData,'nseData':nseData})
    else:
        return render(request,'notauth.html')

def companies(request):
    if request.user.is_authenticated:
        
        return render(request,'companies.html')
    else:
        return render(request,'notauth.html')







def helper(data):
    df = pd.DataFrame(columns = ['id','date','open','high','low','close','adj_close','volume'])
    for i in range(len(data)):
        item = data[i]
        df.loc[i] = [item['id'],item['date'],item['open'],item['high'],item['low'],item['close'],item['adj_close'],item['volume']]
        df['date']= pd.to_datetime(df['date'])
    today, req_day = datetime(2023,1,12), datetime(2022,1,12)

    one_year_df = df[(df['date'] <= today) & (df['date'] > req_day)]
    fifty_two_week_high = max(one_year_df['high'])
    fifty_two_week_low = min(one_year_df['low'])

    day_high = df[df['date']==today]['high']
    day_low = df[df['date']==today]['low']

    previous_day = today - pd.Timedelta(days=1)
    today_close = float(df[df['date']==today]['close'])
    prev_close = float(df[df['date']==previous_day]['close'])

    today_open = float(df[df['date']==today]['open'])
    today_gain_or_loss = float(today_close - prev_close)

    data = {
            'today_open':today_open,
            'today_close':today_close,
            'prev_close': prev_close,
            'today_gain_or_loss' : today_gain_or_loss,
            'day_high':float(day_high),
            'day_low':float(day_low),
            'fifty_two_week_high':fifty_two_week_high,
            'fifty_two_week_low':fifty_two_week_low,
            'xAxis':list(df['date']),
            'yAxis':list(df['close']),
            }
    return data


