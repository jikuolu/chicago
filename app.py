# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:49:46 2016

@author: Jikuo
"""

from flask import Flask,render_template,request,redirect, send_from_directory
from stockgraph import stock_graph
app_stock = Flask(__name__)

@app_stock.route('/')
def main():
  return redirect('/index')
  
@app_stock.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app_stock.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

if __name__ == "__main__":
    app_stock.run(debug=True)
