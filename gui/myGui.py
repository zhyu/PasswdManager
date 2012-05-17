# -*- coding:utf-8 -*-

import config, dialogs
from PyQt4 import QtGui

##################################
#Error messages
##################################
ERR_LOGIN = 'Password is not correct!'
ERR_TITLE_EMPTY='Title cannot be empty!'
ERR_ACCOUNT_EMPTY='Account cannot be empty!'
ERR_PWD_EMPTY = 'Password cannot be empty!'
ERR_SEARCH_EMPTY = 'Search Keyword cannot be empty!'
ERR_MASTERPWD_LEN = 'Master Password length should between 5 and 16 digits'
ERR_NEWMASTER_IDENTICAL = 'The two new Master Passwords are not identical, please input again!'
ERR_OLDMASTER_WRONG = 'Given current Master Password is not correct!'
ERR_NEWTAG_EMPTY = 'Tag name cannot be empty!'
ERR_NEWTAG_UNIQUE = 'Tag name has already existed!'
ERR_ACCOUNTTITLE_UNIQUE = 'Account title has already existed!'
ERR_PWD_LEN = 'Password length should be a positive integer!'
ERR_PWD_EMPTYPATTERN= 'At least one Password Pattern needs to be choosen!'
ERR_PWD_COPY= 'Before do the coping, please generating a password first.'

def showErrorDialog(errMsg):
    dlg = dialogs.MsgDialog(None, 'Error', errMsg)
    dlg.exec_()