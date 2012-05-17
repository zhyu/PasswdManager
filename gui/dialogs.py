# -*- coding:utf-8 -*-

import config, util
from func import *
from PyQt4 import QtCore, QtGui

RETRY = 5

class LoginDialog(QtGui.QDialog):
    '''
    dialog about login
    '''
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        pwdLable = QtGui.QLabel(self.setLableText())
        self.pwd = QtGui.QLineEdit()
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        okBtn = QtGui.QPushButton('OK')
        cancelBtn = QtGui.QPushButton('Exit')
        self.connect(okBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.connect(cancelBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('reject()'))
        layout = QtGui.QFormLayout()
        layout.addRow(pwdLable)
        layout.addRow(self.pwd)
        layout.addRow(cancelBtn, okBtn)
        self.setLayout(layout)
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('Login')    
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def setLableText(self):
        if RETRY == 1:
            s = 'Please enter the Master Password: ( Last Try!!! )'
        else:
            s = 'Please enter the Master Password: ( %d tries left )' % (RETRY)
        return s
    
    def authenticate(self):
        mFunc = MasterFunc()
        
        
    