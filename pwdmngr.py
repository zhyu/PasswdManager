# -*- coding:utf-8 -*-

import sys, config
from PyQt4 import QtGui
from gui.dialogs import LoginDialog
from gui.mainWindow import MainWindow

def login():
    loginDialog = LoginDialog()
    return loginDialog.authenticate()

def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    if login(): 
        win.show()
        sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()