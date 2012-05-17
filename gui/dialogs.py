# -*- coding:utf-8 -*-

import config, util
from func import *
from PyQt4 import QtCore, QtGui

class LoginDialog(QtGui.QDialog):
    '''
    dialog about login
    '''
    
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.pwdLabel = QtGui.QLabel('Please enter the Master Password: ')
        self.pwd = QtGui.QLineEdit()
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setFocus()
        
        okBtn = QtGui.QPushButton('&OK')
        cancelBtn = QtGui.QPushButton('&Exit')
        okBtn.setDefault(True)
        self.connect(okBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.connect(cancelBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('reject()'))
        
        layout = QtGui.QFormLayout()
        layout.addRow(self.pwdLabel)
        layout.addRow(self.pwd)
        layout.addRow(cancelBtn, okBtn)
        self.setLayout(layout)
        
        self.setWindowTitle('Login')
        self.show()
    
    def authentication(self):
        mFunc = MasterFunc()
        inPwd = unicode(self.pwd.text())
        
        if mFunc.authentication(inPwd):
            config.setMasterPwd(inPwd)
            return True
        else: 
            return False
        