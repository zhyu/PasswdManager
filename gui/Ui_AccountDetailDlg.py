# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/AccountDetailDlg.ui'
#
# Created: Sun May 20 18:41:59 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccountDetailDlg(object):
    def setupUi(self, AccountDetailDlg):
        AccountDetailDlg.setObjectName(_fromUtf8("AccountDetailDlg"))
        AccountDetailDlg.resize(650, 680)
        AccountDetailDlg.setStyleSheet(_fromUtf8(""))
        self.lb1 = QtGui.QLabel(AccountDetailDlg)
        self.lb1.setGeometry(QtCore.QRect(60, 20, 81, 16))
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.lb2 = QtGui.QLabel(AccountDetailDlg)
        self.lb2.setGeometry(QtCore.QRect(210, 61, 31, 20))
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.lb3 = QtGui.QLabel(AccountDetailDlg)
        self.lb3.setGeometry(QtCore.QRect(190, 101, 52, 20))
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.lb4 = QtGui.QLabel(AccountDetailDlg)
        self.lb4.setGeometry(QtCore.QRect(210, 141, 31, 20))
        self.lb4.setObjectName(_fromUtf8("lb4"))
        self.lb5 = QtGui.QLabel(AccountDetailDlg)
        self.lb5.setGeometry(QtCore.QRect(160, 181, 81, 20))
        self.lb5.setObjectName(_fromUtf8("lb5"))
        self.lb6 = QtGui.QLabel(AccountDetailDlg)
        self.lb6.setGeometry(QtCore.QRect(150, 230, 81, 20))
        self.lb6.setObjectName(_fromUtf8("lb6"))
        self.lb7 = QtGui.QLabel(AccountDetailDlg)
        self.lb7.setGeometry(QtCore.QRect(170, 310, 71, 16))
        self.lb7.setObjectName(_fromUtf8("lb7"))
        self.lb8 = QtGui.QLabel(AccountDetailDlg)
        self.lb8.setGeometry(QtCore.QRect(180, 411, 61, 20))
        self.lb8.setObjectName(_fromUtf8("lb8"))
        self.lb9 = QtGui.QLabel(AccountDetailDlg)
        self.lb9.setGeometry(QtCore.QRect(160, 470, 71, 16))
        self.lb9.setObjectName(_fromUtf8("lb9"))
        self.checkBox = QtGui.QCheckBox(AccountDetailDlg)
        self.checkBox.setGeometry(QtCore.QRect(80, 590, 211, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.title = QtGui.QLineEdit(AccountDetailDlg)
        self.title.setGeometry(QtCore.QRect(250, 60, 301, 22))
        self.title.setObjectName(_fromUtf8("title"))
        self.account = QtGui.QLineEdit(AccountDetailDlg)
        self.account.setGeometry(QtCore.QRect(250, 100, 301, 22))
        self.account.setObjectName(_fromUtf8("account"))
        self.tags = QtGui.QLineEdit(AccountDetailDlg)
        self.tags.setGeometry(QtCore.QRect(250, 140, 301, 22))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.cTime = QtGui.QLineEdit(AccountDetailDlg)
        self.cTime.setGeometry(QtCore.QRect(250, 180, 301, 22))
        self.cTime.setObjectName(_fromUtf8("cTime"))
        self.uTime = QtGui.QLineEdit(AccountDetailDlg)
        self.uTime.setGeometry(QtCore.QRect(250, 230, 301, 22))
        self.uTime.setObjectName(_fromUtf8("uTime"))
        self.description = QtGui.QTextEdit(AccountDetailDlg)
        self.description.setGeometry(QtCore.QRect(250, 270, 301, 121))
        self.description.setObjectName(_fromUtf8("description"))
        self.password = QtGui.QLineEdit(AccountDetailDlg)
        self.password.setGeometry(QtCore.QRect(250, 410, 301, 22))
        self.password.setStyleSheet(_fromUtf8("background-color: black; color: rgb(192, 0, 0);"))
        self.password.setObjectName(_fromUtf8("password"))
        self.secret = QtGui.QTextEdit(AccountDetailDlg)
        self.secret.setGeometry(QtCore.QRect(250, 450, 301, 131))
        self.secret.setStyleSheet(_fromUtf8("background-color: black; color: rgb(192, 0, 0);"))
        self.secret.setObjectName(_fromUtf8("secret"))
        self.editBtn = QtGui.QPushButton(AccountDetailDlg)
        self.editBtn.setGeometry(QtCore.QRect(200, 630, 91, 23))
        self.editBtn.setObjectName(_fromUtf8("editBtn"))
        self.closeBtn = QtGui.QPushButton(AccountDetailDlg)
        self.closeBtn.setGeometry(QtCore.QRect(310, 630, 91, 23))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))

        self.retranslateUi(AccountDetailDlg)
        QtCore.QObject.connect(self.closeBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDetailDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountDetailDlg)

    def retranslateUi(self, AccountDetailDlg):
        AccountDetailDlg.setWindowTitle(QtGui.QApplication.translate("AccountDetailDlg", "Account Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.lb1.setText(QtGui.QApplication.translate("AccountDetailDlg", "Account Detail:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb2.setText(QtGui.QApplication.translate("AccountDetailDlg", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb3.setText(QtGui.QApplication.translate("AccountDetailDlg", "Account:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb4.setText(QtGui.QApplication.translate("AccountDetailDlg", "Tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb5.setText(QtGui.QApplication.translate("AccountDetailDlg", "Created Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb6.setText(QtGui.QApplication.translate("AccountDetailDlg", "Last update at:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb7.setText(QtGui.QApplication.translate("AccountDetailDlg", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb8.setText(QtGui.QApplication.translate("AccountDetailDlg", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb9.setText(QtGui.QApplication.translate("AccountDetailDlg", "Secret notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("AccountDetailDlg", "Show Password and Secret notes", None, QtGui.QApplication.UnicodeUTF8))
        self.password.setText(QtGui.QApplication.translate("AccountDetailDlg", "[Hidden]", None, QtGui.QApplication.UnicodeUTF8))
        self.secret.setHtml(QtGui.QApplication.translate("AccountDetailDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'WenQuanYi Micro Hei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[Hidden]</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.editBtn.setText(QtGui.QApplication.translate("AccountDetailDlg", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.closeBtn.setText(QtGui.QApplication.translate("AccountDetailDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AccountDetailDlg = QtGui.QDialog()
    ui = Ui_AccountDetailDlg()
    ui.setupUi(AccountDetailDlg)
    AccountDetailDlg.show()
    sys.exit(app.exec_())

