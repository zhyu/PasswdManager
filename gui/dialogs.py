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
from Ui_NewAccountDlg import Ui_NewAccountDlg
from Ui_EditAccountDlg import Ui_EditAccountDlg
from Ui_AccountDetailDlg import Ui_AccountDetailDlg

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
 
class AccountDetailDlg(QtGui.QDialog, Ui_AccountDetailDlg):
    def __init__(self, parent, pwdID):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.pwdID = pwdID
        self.pwdFunc = PwdFunc()
        self.tagFunc = TagFunc()
        self.accountObj = self.pwdFunc.getPwdByID(self.pwdID)
        self.loadData()
        
    def loadData(self):
        acc = self.accountObj
        self.title.setText(acc.title)
        self.account.setText(acc.username)
        self.tags.setText(self.tagFunc.getTagNameString(acc.tags))
        self.cTime.setText(acc.createDate)
        self.uTime.setText(acc.lastUpdate)
        self.description.setPlainText(acc.description)
        
    @pyqtSignature("bool")
    def on_checkBox_toggled(self, checked):
        self.showHidePwd()
    
    @pyqtSignature("")
    def on_editBtn_clicked(self):
        self.accept()
        self.parent.onEditAccount()
    
    def showHidePwd(self):
        if self.checkBox.isChecked(): # show
            self.password.setStyleSheet('')
            self.secret.setStyleSheet('')
            self.password.setText(util.decrypt(config.getMasterPwd(), self.accountObj.pwd))
            self.secret.setPlainText(util.decrypt(config.getMasterPwd(), self.accountObj.secret).decode('utf-8') if self.accountObj.secret else '')
        else: # hide
            self.password.setStyleSheet("background-color: black; color: rgb(192, 0, 0);")
            self.secret.setStyleSheet("background-color: black; color: rgb(192, 0, 0);")
            self.password.setText(myGui.INFO_HIDE_TXT)
            self.secret.setPlainText(myGui.INFO_HIDE_TXT)
       
class EditAccountDlg(QtGui.QDialog, Ui_EditAccountDlg):
    def __init__(self, parent, pwdID):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pwdID = pwdID
        self.pwdFunc = PwdFunc()
        self.accountObj = self.pwdFunc.getPwdByID(self.pwdID)
        self.loadTags()
        self.loadData()
        self.show()
    
    def loadData(self):
        acc = self.accountObj
        self.title.setText(acc.title)
        self.description.setPlainText(acc.description)
        self.account.setText(acc.username)
        self.secret.setPlainText(util.decrypt(config.getMasterPwd(), acc.secret).decode('utf-8') if acc.secret else '')
        tagName = [tag.name for tag in acc.tags]
        cnt = self.tags.count()
        for idx in xrange(cnt):
            if unicode(self.tags.item(idx).text()) in tagName:
                self.tags.item(idx).setSelected(True)
    
    def loadTags(self):
        self.tags.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        tagFunc = TagFunc()
        tagList = tagFunc.getAllTags()
        self.tagIDList = []
        for idx, tag in enumerate(tagList):
            self.tags.addItem(QtGui.QListWidgetItem(tag.name))
            self.tagIDList.append(tag.id)
    
    def onSave(self):
        val = self.exec_()
        if val:
            if len(unicode(self.title.text())) == 0:
                myGui.showErrorDialog(myGui.ERR_TITLE_EMPTY)
                self.title.setFocus()
                self.onSave()
            elif len(unicode(self.account.text())) == 0:
                myGui.showErrorDialog(myGui.ERR_ACCOUNT_EMPTY)
                self.account.setFocus()
                self.onSave()
            elif not self.pwdFunc.isTitleNameValid(unicode(self.title.text()), self.pwdID):
                myGui.showErrorDialog(myGui.ERR_ACCOUNTTITLE_UNIQUE)
                self.title.setFocus()
                self.onSave()
            else:
                nTitle = unicode(self.title.text())
                nDescription = unicode(self.description.toPlainText())
                nAccount = unicode(self.account.text())
                nPassword = unicode(self.password.text()) if len(unicode(self.password.text())) > 0 else None
                nSecret = unicode(self.secret.toPlainText()).encode('utf-8')
                nTagIDs = []
                cnt = self.tags.count()
                for idx in xrange(cnt):
                    if self.tags.item(idx).isSelected():
                        nTagIDs.append(self.tagIDList[idx])
                self.pwdFunc.updateAccount(self.pwdID, nTitle, nDescription, nAccount, nPassword, nSecret, nTagIDs)

class NewAccountDlg(QtGui.QDialog, Ui_NewAccountDlg):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        self.loadTags()

    def loadTags(self):
        self.tags.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        tagFunc = TagFunc()
        tagList = tagFunc.getAllTags()
        self.tagIDList = []
        for idx, tag in enumerate(tagList):
            self.tags.addItem(QtGui.QListWidgetItem(tag.name))
            self.tagIDList.append(tag.id)
            # select the current selected tag if not in ALL or Trash
            selelectedTagID = self.parent.selectedTagID
            if tag.id == selelectedTagID and selelectedTagID >= 0:
                self.tags.item(idx).setSelected(True)
    
    def doSave(self):
        pwdFunc = PwdFunc()
        var = self.exec_()
        if var:
            if len(unicode(self.title.text())) == 0:
                myGui.showErrorDialog(myGui.ERR_TITLE_EMPTY)
                self.title.setFocus()
                self.doSave()
            elif len(unicode(self.account.text())) == 0:
                myGui.showErrorDialog(myGui.ERR_ACCOUNT_EMPTY)
                self.account.setFocus()
                self.doSave()
            elif len(unicode(self.password.text())) == 0:
                myGui.showErrorDialog(myGui.ERR_PWD_EMPTY)
                self.password.setFocus()
                self.doSave()
            elif not pwdFunc.isTitleNameValid(unicode(self.title.text())):
                myGui.showErrorDialog(myGui.ERR_ACCOUNTTITLE_UNIQUE)
                self.title.setFocus()
                self.doSave()
            else:
                nTitle = unicode(self.title.text())
                nDescription = unicode(self.description.toPlainText())
                nAccount = unicode(self.account.text())
                nPassword = unicode(self.password.text())
                nSecret = unicode(self.secret.toPlainText()).encode('utf-8')
                nTagIDs = []
                cnt = self.tags.count()
                for idx in xrange(cnt):
                    if self.tags.item(idx).isSelected():
                        nTagIDs.append(self.tagIDList[idx])
                pwdFunc.addAccount(nTitle, nDescription, nAccount, nPassword, nSecret, nTagIDs)
                
    
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