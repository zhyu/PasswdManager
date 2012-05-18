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
        self.setWindowIcon(QtGui.QIcon(myGui.ICON_APP_ICON))
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

class AccountDetailDialog(QtGui.QDialog):
    '''
    show account detail (read only)
    '''
    pass

class EditAccountDialog(QtGui.QDialog):
    pass

class NewPwdDialog(QtGui.QDialog):
    '''
    dialog about add new password
    '''
    
    def __init__(self, parent):
        super(NewPwdDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        pass
    
    def loadTags(self):
        pass
    
    def doSave(self):
        pass

class ChgMasterPwdDialog(QtGui.QDialog):
    pass

class PwdGenDialog(QtGui.QDialog):
    pass

class NewTagDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(NewTagDialog, self).__init__()
        self.initUI()
    
    def initUI(self):
        lb = QtGui.QLabel('The name of new tag:')
        self.tag = QtGui.QLineEdit()
        
        okBtn = QtGui.QPushButton('&OK')
        cancelBtn = QtGui.QPushButton('&Cancel')
        okBtn.setDefault(True)
        self.connect(okBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.connect(cancelBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('reject()'))
        
        layout = QtGui.QFormLayout()
        layout.addRow(lb, self.tag)
        layout.addRow(cancelBtn, okBtn)
        self.setLayout(layout)
        
        self.setWindowTitle('Add New Tag')
        self.setWindowIcon(QtGui.QIcon(myGui.ICON_APP_ICON))
        self.show()
    
    def onSave(self):
        tagFunc = TagFunc()
        var = self.exec_()
        if var:
            tagName = unicode(self.tag.text())
            if not tagName:
                myGui.showErrorDialog(myGui.ERR_NEWTAG_EMPTY)
                self.onSave()
            elif not TagFunc.isTagNameValid(tagName):
                myGui.showErrorDialog(myGui.ERR_NEWTAG_UNIQUE)
                self.onSave()
            else:
                tagFunc.addNewTag(tagName)
                   

class EditTagDialog(QtGui.QDialog):
    def __init__(self, parent, tagID):
        super(EditTagDialog, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.tagID = tagID
        self.tagFunc = TagFunc()
        tag = self.tagFunc.getTagByID(tagID)
        lb = QtGui.QLabel('The new name of the tag:')
        self.tag = QtGui.QLineEdit(tag.name)
        
        okBtn = QtGui.QPushButton('&OK')
        cancelBtn = QtGui.QPushButton('&Cancel')
        okBtn.setDefault(True)
        self.connect(okBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.connect(cancelBtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('reject()'))
        
        layout = QtGui.QFormLayout()
        layout.addRow(lb, self.tag)
        layout.addRow(cancelBtn, okBtn)
        self.setLayout(layout)
        
        self.setWindowTitle('Edit Tag')
        self.setWindowIcon(QtGui.QIcon(myGui.ICON_APP_ICON))
        self.show()
    
    def onSave(self):
        var = self.exec_()
        if var:
            tagName = unicode(self.tag.text())
            if not tagName:
                myGui.showErrorDialog(myGui.ERR_NEWTAG_EMPTY)
                self.onSave()
            elif not TagFunc.isTagNameValid(tagName, self.tagID):
                myGui.showErrorDialog(myGui.ERR_NEWTAG_UNIQUE)
                self.onSave()
            else:
                self.tagFunc.editTag(self.tagID, tagName)