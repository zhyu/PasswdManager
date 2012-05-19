# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PasswdManager/gui/EditTagDlg.ui'
#
# Created: Sat May 19 22:36:32 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditTagDlg(object):
    def setupUi(self, EditTagDlg):
        EditTagDlg.setObjectName(_fromUtf8("EditTagDlg"))
        EditTagDlg.resize(330, 120)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditTagDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(EditTagDlg)
        self.buttonBox.setGeometry(QtCore.QRect(80, 80, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tag = QtGui.QLineEdit(EditTagDlg)
        self.tag.setGeometry(QtCore.QRect(30, 50, 261, 22))
        self.tag.setObjectName(_fromUtf8("tag"))
        self.lb = QtGui.QLabel(EditTagDlg)
        self.lb.setGeometry(QtCore.QRect(40, 20, 221, 16))
        self.lb.setObjectName(_fromUtf8("lb"))

        self.retranslateUi(EditTagDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditTagDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditTagDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(EditTagDlg)

    def retranslateUi(self, EditTagDlg):
        EditTagDlg.setWindowTitle(QtGui.QApplication.translate("EditTagDlg", "Edit tag", None, QtGui.QApplication.UnicodeUTF8))
        self.lb.setText(QtGui.QApplication.translate("EditTagDlg", "The new name of the tag:", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditTagDlg = QtGui.QDialog()
    ui = Ui_EditTagDlg()
    ui.setupUi(EditTagDlg)
    EditTagDlg.show()
    sys.exit(app.exec_())

