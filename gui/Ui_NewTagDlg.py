# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/NewTagDlg.ui'
#
# Created: Sat May 19 22:36:31 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewTagDlg(object):
    def setupUi(self, NewTagDlg):
        NewTagDlg.setObjectName(_fromUtf8("NewTagDlg"))
        NewTagDlg.resize(330, 120)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewTagDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(NewTagDlg)
        self.buttonBox.setGeometry(QtCore.QRect(80, 70, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lb = QtGui.QLabel(NewTagDlg)
        self.lb.setGeometry(QtCore.QRect(40, 20, 121, 16))
        self.lb.setObjectName(_fromUtf8("lb"))
        self.tag = QtGui.QLineEdit(NewTagDlg)
        self.tag.setGeometry(QtCore.QRect(40, 40, 251, 22))
        self.tag.setObjectName(_fromUtf8("tag"))

        self.retranslateUi(NewTagDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewTagDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewTagDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTagDlg)

    def retranslateUi(self, NewTagDlg):
        NewTagDlg.setWindowTitle(QtGui.QApplication.translate("NewTagDlg", "New tag", None, QtGui.QApplication.UnicodeUTF8))
        self.lb.setText(QtGui.QApplication.translate("NewTagDlg", "The name of new tag:", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewTagDlg = QtGui.QDialog()
    ui = Ui_NewTagDlg()
    ui.setupUi(NewTagDlg)
    NewTagDlg.show()
    sys.exit(app.exec_())

