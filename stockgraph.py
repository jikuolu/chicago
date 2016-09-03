# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:44:01 2016

@author: Jikuo
"""
import requests
import datetime
import simplejson as json
import pandas as pd
from bokeh.charts import TimeSeries, show, output_file, save
from bokeh.layouts import column


def stock_graph(ticker):

    quandl_apikey = "mWZdFiBfbyUzVK2xeec6"
    quandl_header = "https://www.quandl.com/api/v3/datasets/WIKI"

    today = datetime.date.today()
    lastmonth = today - datetime.timedelta(days=31) # not so accurate...
    dateformat = "%Y-%m-%d"
    end_date = today.strftime(dateformat)
    start_date = lastmonth.strftime(dateformat)
    stock = ticker
    qurl='https://www.quandl.com/api/v3/datasets/WIKI/%s.json?column_index=4&'\
    'start_date=%s&end_date=%s&api_key=mWZdFiBfbyUzVK2xeec6'%(stock, start_date, end_date)

    r = requests.get(qurl)
    if r.status_code != requests.codes.ok: return 0
    print r.url
    print r.json()

    print(json.dumps(r.json(), sort_keys=True, indent=4 * ' '))
    #print json.loads(r.json())

    tsdata = r.json()['dataset']['data']

    print json.dumps(tsdata)

    # format data as pandas' time series data
    s = pd.Series()
    for price in tsdata:
        s.set_value(pd.Timestamp(price[0]), price[1])
    print s.is_time_series
    print s

    graph_title = "30 Day Stock Price of " + stock.encode('ascii','ignore')
    tsline = TimeSeries(s, title=graph_title, ylabel='Stock Prices', 
    xlabel='Date', legend=True)
#    output_file("timeseries.html", autosave=True)

    save(obj=tsline, filename='templates/timeseries.html')
#    save(column(tsline))
    return 1