# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/ChgMasterPwdDlg.ui'
#
# Created: Sun May 20 13:55:03 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChgMasterPwdDlg(object):
    def setupUi(self, ChgMasterPwdDlg):
        ChgMasterPwdDlg.setObjectName(_fromUtf8("ChgMasterPwdDlg"))
        ChgMasterPwdDlg.resize(400, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChgMasterPwdDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ChgMasterPwdDlg)
        self.buttonBox.setGeometry(QtCore.QRect(120, 150, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lb1 = QtGui.QLabel(ChgMasterPwdDlg)
        self.lb1.setGeometry(QtCore.QRect(40, 30, 151, 16))
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.lb2 = QtGui.QLabel(ChgMasterPwdDlg)
        self.lb2.setGeometry(QtCore.QRect(100, 70, 91, 16))
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.lb3 = QtGui.QLabel(ChgMasterPwdDlg)
        self.lb3.setGeometry(QtCore.QRect(70, 110, 121, 16))
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.oldPwd = QtGui.QLineEdit(ChgMasterPwdDlg)
        self.oldPwd.setGeometry(QtCore.QRect(190, 30, 171, 22))
        self.oldPwd.setEchoMode(QtGui.QLineEdit.Password)
        self.oldPwd.setObjectName(_fromUtf8("oldPwd"))
        self.newPwd = QtGui.QLineEdit(ChgMasterPwdDlg)
        self.newPwd.setGeometry(QtCore.QRect(190, 70, 171, 22))
        self.newPwd.setEchoMode(QtGui.QLineEdit.Password)
        self.newPwd.setObjectName(_fromUtf8("newPwd"))
        self.newPwd2 = QtGui.QLineEdit(ChgMasterPwdDlg)
        self.newPwd2.setGeometry(QtCore.QRect(190, 110, 171, 22))
        self.newPwd2.setEchoMode(QtGui.QLineEdit.Password)
        self.newPwd2.setObjectName(_fromUtf8("newPwd2"))

        self.retranslateUi(ChgMasterPwdDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChgMasterPwdDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChgMasterPwdDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ChgMasterPwdDlg)

    def retranslateUi(self, ChgMasterPwdDlg):
        ChgMasterPwdDlg.setWindowTitle(QtGui.QApplication.translate("ChgMasterPwdDlg", "Change Master Password", None, QtGui.QApplication.UnicodeUTF8))
        self.lb1.setText(QtGui.QApplication.translate("ChgMasterPwdDlg", "Current Master Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb2.setText(QtGui.QApplication.translate("ChgMasterPwdDlg", "New Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb3.setText(QtGui.QApplication.translate("ChgMasterPwdDlg", "New Password again:", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ChgMasterPwdDlg = QtGui.QDialog()
    ui = Ui_ChgMasterPwdDlg()
    ui.setupUi(ChgMasterPwdDlg)
    ChgMasterPwdDlg.show()
    sys.exit(app.exec_())

