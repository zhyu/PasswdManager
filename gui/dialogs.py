# -*- coding:utf-8 -*-

import config, myGui, util
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
        self.pwdLabel = QtGui.QLabel()
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
        
        self.setLabelText()
        self.setWindowTitle('Login')
        self.show()
    
    def setLabelText(self):
        if RETRY == 1:
            s = 'Please enter the Master Password: ( Last Try!!! )'
        else :
            s = 'Please enter the Master Password: ( %d tries left )' % (RETRY)
        self.pwdLabel.setText(s)

    
    def authenticate(self):
        mFunc = MasterFunc()
        var = self.exec_()
        self.setLabelText()
        if var:
            inPwd = unicode(self.pwd.text())
            
            if not (mFunc.authenticate(inPwd)):
                myGui.showErrorDialog(myGui.ERR_LOGIN)
                global RETRY
                
                if RETRY > 1:
                    RETRY -= 1
                    self.setLabelText()
                    self.pwd.clear()
                    return self.authenticate()
                else:
                    return False
            else:
                config.setMasterPwd(inPwd)
                return True
        else:
            return False
        
class MsgDialog(QtGui.QDialog):
    '''
    dialog about popup message
    '''
    
    def __init__(self, parent=None, title='Msg', msg=''):
        super(MsgDialog, self).__init__()
        self.initUI(title, msg)
        
    def initUI(self, title, msg):
        lb = QtGui.QLabel(msg)
        okBtn = QtGui.QPushButton('&OK')
        okBtn.setDefault(True)
        self.connect(okBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('reject()'))
    
        layout = QtGui.QFormLayout()
        layout.addRow(lb)
        layout.addRow(okBtn)
        self.setLayout(layout)
        
        self.setWindowTitle(title)
        self.show()
