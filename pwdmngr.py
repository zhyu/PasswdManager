# -*- coding:utf-8 -*-

import sys, config
from PyQt4 import QtGui
from gui.dialogs import LoginDialog

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(200, 200)
        
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