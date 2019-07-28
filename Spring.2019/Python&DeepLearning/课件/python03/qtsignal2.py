#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
simple signal
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

app = QApplication(sys.argv)
dlg = QDialog()
dlg.setWindowTitle('just close it')
dlg.resize(300, 200)

i = 1

def beatMe():
    global i
    dlg.setWindowTitle("Beat me one more time! " + str(i))
    i = i + 1

btn = QPushButton(dlg)
btn.resize(100, 50)
btn.setText('click it!')
btn.move(100, 100)

# 将btn的clicked信号与dlg的close槽连接
btn.clicked.connect(beatMe)

dlg.show()
sys.exit(app.exec())