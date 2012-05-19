# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/LoginDlg.ui'
#
# Created: Sat May 19 21:56:25 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginDlg(object):
    def setupUi(self, LoginDlg):
        LoginDlg.setObjectName(_fromUtf8("LoginDlg"))
        LoginDlg.resize(400, 130)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(LoginDlg)
        self.buttonBox.setGeometry(QtCore.QRect(110, 80, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pwdLabel = QtGui.QLabel(LoginDlg)
        self.pwdLabel.setGeometry(QtCore.QRect(50, 20, 281, 21))
        self.pwdLabel.setText(_fromUtf8(""))
        self.pwdLabel.setObjectName(_fromUtf8("pwdLabel"))
        self.pwd = QtGui.QLineEdit(LoginDlg)
        self.pwd.setGeometry(QtCore.QRect(40, 50, 311, 22))
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setObjectName(_fromUtf8("pwd"))

        self.retranslateUi(LoginDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoginDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoginDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDlg)

    def retranslateUi(self, LoginDlg):
        LoginDlg.setWindowTitle(QtGui.QApplication.translate("LoginDlg", "Login", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginDlg = QtGui.QDialog()
    ui = Ui_LoginDlg()
    ui.setupUi(LoginDlg)
    LoginDlg.show()
    sys.exit(app.exec_())

