# -*- coding:utf-8 -*-

import config, myGui, util
from func import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from Ui_PwdGenDlg import Ui_PwnGenDlg
from Ui_LoginDlg import Ui_LoginDlg
from Ui_NewTagDlg import Ui_NewTagDlg
from Ui_EditTagDlg import Ui_EditTagDlg
from Ui_ChgMasterPwdDlg import Ui_ChgMasterPwdDlg

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
    
class ChgMasterPwdDlg(QtGui.QDialog, Ui_ChgMasterPwdDlg):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        
    def onChg(self):
        pwdFunc = PwdFunc()
        masterFunc = MasterFunc()
        
        self.oldPwd.setFocus()
        val = self.exec_()
        if val:
            if len(unicode(self.oldPwd.text())) < 5 or len(unicode(self.oldPwd.text())) > 16:
                myGui.showErrorDialog(myGui.ERR_MASTERPWD_LEN)
                self.oldPwd.setFocus()
                self.onChg()
            elif len(unicode(self.newPwd.text())) < 5 or len(unicode(self.newPwd.text())) > 16:
                myGui.showErrorDialog(myGui.ERR_MASTERPWD_LEN)
                self.newPwd.setFocus()
                self.onChg()
            elif unicode(self.newPwd.text()) != unicode(self.newPwd2.text()):
                myGui.showErrorDialog(myGui.ERR_NEWMASTER_IDENTICAL)
                self.newPwd.clear()
                self.newPwd2.clear()
                self.newPwd.setFocus()
                self.onChg()
            elif unicode(self.oldPwd.text()) != config.getMasterPwd():
                myGui.showErrorDialog(myGui.ERR_OLDMASTER_WRONG)
                self.oldPwd.setFocus()
                self.onChg()
            else:
                masterFunc.changeMasterPwd(unicode(self.newPwd.text()))
                myGui.showInfoDialog(myGui.INFO_MASTERPWD)

class PwdGenDlg(QtGui.QDialog, Ui_PwnGenDlg):
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

class NewTagDlg(QtGui.QDialog, Ui_NewTagDlg):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)    
    
    def onSave(self):
        tagFunc = TagFunc()
        self.tag.setFocus()
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
                   

class EditTagDlg(QtGui.QDialog, Ui_EditTagDlg):
    def __init__(self, parent, tagID):
        QtGui.QDialog.__init__(self, parent)
        self.tagID = tagID
        self.setupUi(self)        
        self.tagFunc = TagFunc()
        tag = self.tagFunc.getTagByID(self.tagID)
        self.tag.setText(tag.name)
        self.tag.setFocus()
    
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