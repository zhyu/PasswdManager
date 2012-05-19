# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PwdGenDlg.ui'
#
# Created: Sat May 19 21:38:45 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PwnGenDlg(object):
    def setupUi(self, PwnGenDlg):
        PwnGenDlg.setObjectName(_fromUtf8("PwnGenDlg"))
        PwnGenDlg.resize(520, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/app16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PwnGenDlg.setWindowIcon(icon)
        self.lb1 = QtGui.QLabel(PwnGenDlg)
        self.lb1.setGeometry(QtCore.QRect(40, 20, 111, 20))
        self.lb1.setObjectName(_fromUtf8("lb1"))
        self.leng = QtGui.QLineEdit(PwnGenDlg)
        self.leng.setGeometry(QtCore.QRect(40, 40, 211, 22))
        self.leng.setObjectName(_fromUtf8("leng"))
        self.lb2 = QtGui.QLabel(PwnGenDlg)
        self.lb2.setGeometry(QtCore.QRect(40, 70, 151, 21))
        self.lb2.setObjectName(_fromUtf8("lb2"))
        self.low = QtGui.QCheckBox(PwnGenDlg)
        self.low.setEnabled(True)
        self.low.setGeometry(QtCore.QRect(40, 100, 201, 21))
        self.low.setChecked(True)
        self.low.setObjectName(_fromUtf8("low"))
        self.up = QtGui.QCheckBox(PwnGenDlg)
        self.up.setGeometry(QtCore.QRect(40, 130, 211, 21))
        self.up.setChecked(True)
        self.up.setObjectName(_fromUtf8("up"))
        self.num = QtGui.QCheckBox(PwnGenDlg)
        self.num.setGeometry(QtCore.QRect(40, 160, 151, 21))
        self.num.setChecked(True)
        self.num.setObjectName(_fromUtf8("num"))
        self.punc = QtGui.QCheckBox(PwnGenDlg)
        self.punc.setGeometry(QtCore.QRect(40, 190, 241, 21))
        self.punc.setObjectName(_fromUtf8("punc"))
        self.lb3 = QtGui.QLabel(PwnGenDlg)
        self.lb3.setGeometry(QtCore.QRect(50, 220, 121, 16))
        self.lb3.setObjectName(_fromUtf8("lb3"))
        self.pwd = QtGui.QLineEdit(PwnGenDlg)
        self.pwd.setGeometry(QtCore.QRect(40, 240, 271, 22))
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.cpBtn = QtGui.QPushButton(PwnGenDlg)
        self.cpBtn.setEnabled(False)
        self.cpBtn.setGeometry(QtCore.QRect(330, 240, 111, 23))
        self.cpBtn.setObjectName(_fromUtf8("cpBtn"))
        self.genBtn = QtGui.QPushButton(PwnGenDlg)
        self.genBtn.setGeometry(QtCore.QRect(140, 290, 91, 23))
        self.genBtn.setObjectName(_fromUtf8("genBtn"))
        self.cloBtn = QtGui.QPushButton(PwnGenDlg)
        self.cloBtn.setGeometry(QtCore.QRect(280, 290, 91, 23))
        self.cloBtn.setObjectName(_fromUtf8("cloBtn"))

        self.retranslateUi(PwnGenDlg)
        QtCore.QObject.connect(self.cloBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), PwnGenDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PwnGenDlg)

    def retranslateUi(self, PwnGenDlg):
        PwnGenDlg.setWindowTitle(QtGui.QApplication.translate("PwnGenDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lb1.setText(QtGui.QApplication.translate("PwnGenDlg", "Password Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb2.setText(QtGui.QApplication.translate("PwnGenDlg", "Password Pattern Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.low.setText(QtGui.QApplication.translate("PwnGenDlg", "Lowercase letters (a,b,c,d,e.....z)", None, QtGui.QApplication.UnicodeUTF8))
        self.up.setText(QtGui.QApplication.translate("PwnGenDlg", "Uppercase letters (A,B,C,D,E.....Z)", None, QtGui.QApplication.UnicodeUTF8))
        self.num.setText(QtGui.QApplication.translate("PwnGenDlg", "Numbers (0,1,2,3,4...9)", None, QtGui.QApplication.UnicodeUTF8))
        self.punc.setText(QtGui.QApplication.translate("PwnGenDlg", "Punctuations ( #, $, @, [, ), /, ; ,\\,  _, - ... )", None, QtGui.QApplication.UnicodeUTF8))
        self.lb3.setText(QtGui.QApplication.translate("PwnGenDlg", "Generated Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.cpBtn.setText(QtGui.QApplication.translate("PwnGenDlg", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.genBtn.setText(QtGui.QApplication.translate("PwnGenDlg", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.cloBtn.setText(QtGui.QApplication.translate("PwnGenDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
