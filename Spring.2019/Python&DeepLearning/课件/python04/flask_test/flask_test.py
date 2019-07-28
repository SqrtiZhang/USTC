# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:55:27 2019

@author: ustc
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_page():
    return 'This is the index page!'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def user_page(username):
    return 'Welcome, ' + username + "!"