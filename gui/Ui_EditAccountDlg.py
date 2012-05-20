# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/EditAccountDlg.ui'
#
# Created: Sun May 20 18:41:58 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditAccountDlg(object):
    def setupUi(self, EditAccountDlg):
        EditAccountDlg.setObjectName(_fromUtf8("EditAccountDlg"))
        EditAccountDlg.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditAccountDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(EditAccountDlg)
        self.buttonBox.setGeometry(QtCore.QRect(370, 540, 160, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.title = QtGui.QLineEdit(EditAccountDlg)
        self.title.setGeometry(QtCore.QRect(210, 60, 261, 22))
        self.title.setObjectName(_fromUtf8("title"))
        self.account = QtGui.QLineEdit(EditAccountDlg)
        self.account.setGeometry(QtCore.QRect(210, 230, 261, 22))
        self.account.setObjectName(_fromUtf8("account"))
        self.password = QtGui.QLineEdit(EditAccountDlg)
        self.password.setGeometry(QtCore.QRect(210, 270, 261, 22))
        self.password.setObjectName(_fromUtf8("password"))
        self.description = QtGui.QPlainTextEdit(EditAccountDlg)
        self.description.setGeometry(QtCore.QRect(210, 100, 261, 111))
        self.description.setObjectName(_fromUtf8("description"))
        self.secret = QtGui.QPlainTextEdit(EditAccountDlg)
        self.secret.setGeometry(QtCore.QRect(210, 310, 261, 151))
        self.secret.setObjectName(_fromUtf8("secret"))
        self.tags = QtGui.QListWidget(EditAccountDlg)
        self.tags.setGeometry(QtCore.QRect(570, 60, 256, 200))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.lb1 = QtGui.QLabel(EditAccountDlg)
        self.lb1.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.lb2 = QtGui.QLabel(EditAccountDlg)
        self.lb2.setGeometry(QtCore.QRect(540, 30, 31, 16))
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.lb3 = QtGui.QLabel(EditAccountDlg)
        self.lb3.setGeometry(QtCore.QRect(170, 60, 31, 21))
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.lb4 = QtGui.QLabel(EditAccountDlg)
        self.lb4.setGeometry(QtCore.QRect(130, 120, 71, 16))
        self.lb4.setObjectName(_fromUtf8("lb4"))
        self.lb5 = QtGui.QLabel(EditAccountDlg)
        self.lb5.setGeometry(QtCore.QRect(140, 230, 51, 20))
        self.lb5.setObjectName(_fromUtf8("lb5"))
        self.lb6 = QtGui.QLabel(EditAccountDlg)
        self.lb6.setGeometry(QtCore.QRect(120, 270, 81, 21))
        self.lb6.setObjectName(_fromUtf8("lb6"))
        self.lb9 = QtGui.QLabel(EditAccountDlg)
        self.lb9.setGeometry(QtCore.QRect(130, 510, 371, 16))
        self.lb9.setStyleSheet(_fromUtf8("color: red;"))
        self.lb9.setObjectName(_fromUtf8("lb9"))
        self.lb8 = QtGui.QLabel(EditAccountDlg)
        self.lb8.setGeometry(QtCore.QRect(130, 480, 351, 16))
        self.lb8.setStyleSheet(_fromUtf8("color: red;"))
        self.lb8.setObjectName(_fromUtf8("lb8"))
        self.lb7 = QtGui.QLabel(EditAccountDlg)
        self.lb7.setGeometry(QtCore.QRect(100, 350, 91, 20))
        self.lb7.setObjectName(_fromUtf8("lb7"))

        self.retranslateUi(EditAccountDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditAccountDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditAccountDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(EditAccountDlg)

    def retranslateUi(self, EditAccountDlg):
        EditAccountDlg.setWindowTitle(QtGui.QApplication.translate("EditAccountDlg", "New Account", None, QtGui.QApplication.UnicodeUTF8))
        self.lb1.setText(QtGui.QApplication.translate("EditAccountDlg", "Account Details:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb2.setText(QtGui.QApplication.translate("EditAccountDlg", "Tags:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb3.setText(QtGui.QApplication.translate("EditAccountDlg", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb4.setText(QtGui.QApplication.translate("EditAccountDlg", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb5.setText(QtGui.QApplication.translate("EditAccountDlg", "Account:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb6.setText(QtGui.QApplication.translate("EditAccountDlg", "(*) Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb9.setText(QtGui.QApplication.translate("EditAccountDlg", "(*) Leave the password empty if you wanna keep the old password.", None, QtGui.QApplication.UnicodeUTF8))
        self.lb8.setText(QtGui.QApplication.translate("EditAccountDlg", "(*) The password and secret notes in the textbox will be visible. ", None, QtGui.QApplication.UnicodeUTF8))
        self.lb7.setText(QtGui.QApplication.translate("EditAccountDlg", "(*) Secret notes:", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditAccountDlg = QtGui.QDialog()
    ui = Ui_EditAccountDlg()
    ui.setupUi(EditAccountDlg)
    EditAccountDlg.show()
    sys.exit(app.exec_())

