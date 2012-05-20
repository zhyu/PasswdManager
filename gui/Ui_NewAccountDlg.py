# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/NewAccountDlg.ui'
#
# Created: Sun May 20 18:41:57 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewAccountDlg(object):
    def setupUi(self, NewAccountDlg):
        NewAccountDlg.setObjectName(_fromUtf8("NewAccountDlg"))
        NewAccountDlg.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewAccountDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(NewAccountDlg)
        self.buttonBox.setGeometry(QtCore.QRect(370, 530, 160, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.title = QtGui.QLineEdit(NewAccountDlg)
        self.title.setGeometry(QtCore.QRect(210, 60, 261, 22))
        self.title.setObjectName(_fromUtf8("title"))
        self.account = QtGui.QLineEdit(NewAccountDlg)
        self.account.setGeometry(QtCore.QRect(210, 230, 261, 22))
        self.account.setObjectName(_fromUtf8("account"))
        self.password = QtGui.QLineEdit(NewAccountDlg)
        self.password.setGeometry(QtCore.QRect(210, 270, 261, 22))
        self.password.setObjectName(_fromUtf8("password"))
        self.description = QtGui.QPlainTextEdit(NewAccountDlg)
        self.description.setGeometry(QtCore.QRect(210, 100, 261, 111))
        self.description.setObjectName(_fromUtf8("description"))
        self.secret = QtGui.QPlainTextEdit(NewAccountDlg)
        self.secret.setGeometry(QtCore.QRect(210, 310, 261, 151))
        self.secret.setObjectName(_fromUtf8("secret"))
        self.tags = QtGui.QListWidget(NewAccountDlg)
        self.tags.setGeometry(QtCore.QRect(570, 60, 256, 200))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.lb1 = QtGui.QLabel(NewAccountDlg)
        self.lb1.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.lb2 = QtGui.QLabel(NewAccountDlg)
        self.lb2.setGeometry(QtCore.QRect(540, 30, 31, 16))
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.lb3 = QtGui.QLabel(NewAccountDlg)
        self.lb3.setGeometry(QtCore.QRect(170, 60, 31, 21))
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.lb4 = QtGui.QLabel(NewAccountDlg)
        self.lb4.setGeometry(QtCore.QRect(130, 120, 71, 16))
        self.lb4.setObjectName(_fromUtf8("lb4"))
        self.lb5 = QtGui.QLabel(NewAccountDlg)
        self.lb5.setGeometry(QtCore.QRect(140, 230, 51, 20))
        self.lb5.setObjectName(_fromUtf8("lb5"))
        self.lb6 = QtGui.QLabel(NewAccountDlg)
        self.lb6.setGeometry(QtCore.QRect(120, 270, 81, 21))
        self.lb6.setObjectName(_fromUtf8("lb6"))
        self.lb7 = QtGui.QLabel(NewAccountDlg)
        self.lb7.setGeometry(QtCore.QRect(100, 330, 91, 20))
        self.lb7.setObjectName(_fromUtf8("lb7"))
        self.lb8 = QtGui.QLabel(NewAccountDlg)
        self.lb8.setGeometry(QtCore.QRect(130, 470, 351, 16))
        self.lb8.setStyleSheet(_fromUtf8("color: red;"))
        self.lb8.setObjectName(_fromUtf8("lb8"))
        self.lb9 = QtGui.QLabel(NewAccountDlg)
        self.lb9.setGeometry(QtCore.QRect(130, 500, 421, 16))
        self.lb9.setStyleSheet(_fromUtf8("color: red;"))
        self.lb9.setObjectName(_fromUtf8("lb9"))

        self.retranslateUi(NewAccountDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewAccountDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewAccountDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(NewAccountDlg)

    def retranslateUi(self, NewAccountDlg):
        NewAccountDlg.setWindowTitle(QtGui.QApplication.translate("NewAccountDlg", "New Account", None, QtGui.QApplication.UnicodeUTF8))
        self.lb1.setText(QtGui.QApplication.translate("NewAccountDlg", "Account Details:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb2.setText(QtGui.QApplication.translate("NewAccountDlg", "Tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb3.setText(QtGui.QApplication.translate("NewAccountDlg", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb4.setText(QtGui.QApplication.translate("NewAccountDlg", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb5.setText(QtGui.QApplication.translate("NewAccountDlg", "Account:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb6.setText(QtGui.QApplication.translate("NewAccountDlg", "(*) Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb7.setText(QtGui.QApplication.translate("NewAccountDlg", "(*) Secret notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb8.setText(QtGui.QApplication.translate("NewAccountDlg", "(*) The password and secret notes in the textbox will be visible. ", None, QtGui.QApplication.UnicodeUTF8))
        self.lb9.setText(QtGui.QApplication.translate("NewAccountDlg", "(*) Account(username), password and secret notes will be encrypted-stored.", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewAccountDlg = QtGui.QDialog()
    ui = Ui_NewAccountDlg()
    ui.setupUi(NewAccountDlg)
    NewAccountDlg.show()
    sys.exit(app.exec_())

