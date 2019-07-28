# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:05:14 2019

@author: ustc
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)