# -*- coding: utf-8 -*-

def print_info():
    print("Hello World")
    
class TestClass(object):
    
    num = 0
    def __init__(self, num):
        self.num = num
    
    def doSth(self):
        print(self.num)
        