# -*- coding:utf-8 -*-

import config, myGui, util
from func import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from Ui_PwdGenDlg import Ui_PwnGenDlg
from Ui_LoginDlg import Ui_LoginDlg

RETRY = 5

class LoginDlg(QtGui.QDialog, Ui_LoginDlg):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def setLabelText(self):
        if RETRY == 1:
            s = 'Please enter the Master Password: ( Last Try!!! )'
        else :
            s = 'Please enter the Master Password: ( %d tries left )' % (RETRY)
        self.pwdLabel.setText(s)
    
    def authenticate(self):
        mFunc = MasterFunc()
        self.setLabelText()
        self.pwd.setFocus()
        var = self.exec_()
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

class PwdGenDialog(QtGui.QDialog, Ui_PwnGenDlg):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_cpBtn_clicked(self):
        self.copyToClipboard()
    
    @pyqtSignature("")
    def on_genBtn_clicked(self):
        self.doGenerate()
    
    def doGenerate(self):
        patternList = []
        if self.low.isChecked():
            patternList.append('lower')
        if self.up.isChecked():
            patternList.append('upper')
        if self.num.isChecked():
            patternList.append('number')
        if self.punc.isChecked():
            patternList.append('punc')
        if len(patternList) == 0:
            myGui.showErrorDialog(myGui.ERR_PWD_EMPTYPATTERN)
        else:
            try:
                length = int(unicode(self.leng.text()))
                if length > 0:
                    self.pwd.setText(util.getRandomString(length, patternList))
                    self.genBtn.setText('Re&generate')
                    self.cpBtn.setEnabled(True)
                else:
                    myGui.showErrorDialog(myGui.ERR_PWD_LEN)
            except ValueError:
                myGui.showErrorDialog(myGui.ERR_PWD_LEN)
            
    
    def copyToClipboard(self):
        clipboard = QtGui.QApplication.clipboard()
        if len(str(self.pwd.text()).strip()) > 0:
            txt = self.pwd.text()
            clipboard.setText(txt)
            myGui.showInfoDialog(myGui.INFO_PWD_CLIPBOARD)
        else:
            myGui.showInfoDialog(myGui.ERR_PWD_COPY)
    
    def generatePwd(self):
        self.exec_()

class NewTagDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(NewTagDialog, self).__init__()
        self.parent = parent
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
            elif not tagFunc.isTagNameValid(tagName):
                myGui.showErrorDialog(myGui.ERR_NEWTAG_UNIQUE)
                self.onSave()
            else:
                tagFunc.addNewTag(tagName)
                   

class EditTagDialog(QtGui.QDialog):
    def __init__(self, parent, tagID):
        super(EditTagDialog, self).__init__()
        self.tagID = tagID
        self.initUI()
        
    def initUI(self):
        self.tagFunc = TagFunc()
        tag = self.tagFunc.getTagByID(self.tagID)
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
            elif not self.tagFunc.isTagNameValid(tagName, self.tagID):
                myGui.showErrorDialog(myGui.ERR_NEWTAG_UNIQUE)
                self.onSave()
            else:
                self.tagFunc.editTag(self.tagID, tagName)