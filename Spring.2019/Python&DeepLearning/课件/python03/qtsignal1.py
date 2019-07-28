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


btn = QPushButton(dlg)
btn.resize(100, 50)
btn.setText('click it!')
btn.move(100, 100)

btn.clicked.connect(dlg.close)

dlg.show()
sys.exit(app.exec())