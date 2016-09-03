# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:49:46 2016

@author: Jikuo
"""

from flask import Flask,render_template,request,redirect
from stockgraph import stock_graph
app_stock = Flask(__name__)

@app_stock.route('/')
def main():
  return redirect('/index')
  
@app_stock.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        ticker = request.form['name_ticker']
        print ticker
        s = stock_graph(ticker)
        print s
        if s == 1:
            return redirect('/timeseries')
        else:
            return redirect('/retry')
            

@app_stock.route('/timeseries')
def timeseries():
    return render_template('timeseries.html')
    
@app_stock.route('/retry')
def retry():
    return render_template('resubmit.html')
            
if __name__ == "__main__":
    app_stock.run(debug=True)
