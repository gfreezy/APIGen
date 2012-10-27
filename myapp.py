#!/usr/bin/env python
#coding:utf-8
#import MySQLdb
from flask import Flask, g, request
from flask import render_template

app = Flask(__name__)
app.debug = True
@app.route('/')
def hello():
    return render_template('hello.html', parameters=[1,2,3], responses=[1,2], service_id=1) 

if __name__ == '__main__':
    app.run()
