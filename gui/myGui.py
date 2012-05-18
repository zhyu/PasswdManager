# -*- coding:utf-8 -*-

import config, dialogs
from PyQt4.QtGui import QMessageBox

##################################
# GUI size/position properties
##################################
#Application window size,position
MAIN_WINDOW_SIZE=(1100,700)
MAIN_WINDOW_POSITION=(100,80)
#Dialog position is needed for windows platform.
DIALOG_POSITION=(270,150)

# Long Textbox
SIZE_LONG_TEXT=(300,28)
SIZE_NORMAL_TEXT=(200,28)
SIZE_MULTILINE_TEXT=(400,100)

# textbox in create/edit/detail dialog. keeping same length with multilineTextBox
SIZE_DETAIL_TEXT= (400,28) 
SIZE_SECRET_TEXT= (400,200) 

# Dialog
SIZE_DIALOG_LOGIN = (400, 130)
SIZE_DIALOG_NEWACCOUNT = (900, 610)
SIZE_DIALOG_EDITACCOUNT = (900,610)
SIZE_DIALOG_ACCOUNTDETAIL = (650,680)
SIZE_DIALOG_CHGMASTERPWD = (500, 240)   
SIZE_DIALOG_PWDGEN = (520, 360)      

# splitterwindow min pane size
SPLITTERWINDOW_MIN_SIZE = 100 

##################################
# GUI Position properties
##################################


# splitterwindow Sash Position
SPLITTERWINDOW_SASH_POS = 200 


##################################
# GUI Window name
##################################
TAG_LIST_NAME = 'tagListCtrl'
PWD_LIST_NAME = 'pwdListCtrl'
NAME_TEXTBOX_SEARCH = 'searchTextBox'

##################################
#Information messages
##################################
INFO_CLIPBOARD = """ The password of [%s] has been copied to Clipboard. """
INFO_PWD_CLIPBOARD = """ The password has been copied to Clipboard. """
INFO_MOVETO_TRASH = """ The account [%s] has been moved to trash,\n you can recover at any time """
INFO_COMPLETE_REMOVE = """ The account [%s] has been deleted from trash. """
INFO_RECOVERED = """ The account [%s] has been recovered from trash. """
INFO_MASTERPWD = """ The Master password was successfully changed. """
INFO_HIDE_TXT = """[ Hidden ]"""
INFO_ACCOUNT_ACTIVE = """[ Active ]"""
INFO_ACCOUNT_INTRASH = """[ In Trash ]"""

##################################
#Confirmation messages
##################################
CONFIRM_MOVETO_TRASH = """Are you sure to move the account [%s]?"""
CONFIRM_COMPLETE_REMOVE = """Are you sure to PERMANENTLY DELETE the account [%s]?"""
CONFIRM_EMPTY_TRASH = """Are you sure to empty the trash?"""
CONFIRM_REMOVE_TAG = """Are you sure to remove the tag [%s]?"""
CONFIRM_REMOVE_USEDTAG = """Removing tag [%s] will NOT remove related accounts. Continue to remove Tag?"""

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
    QMessageBox.critical(None, 'Error', errMsg, QMessageBox.Ok)
    
def showConfirmationDialog(msg, name=''):
    if not name:
        return QMessageBox.question(None, 'Confirmation', msg, QMessageBox.Cancel | QMessageBox.Ok, QMessageBox.Cancel)
    else:
        return QMessageBox.question(None, 'Confirmation', msg % name, QMessageBox.Cancel | QMessageBox.Ok, QMessageBox.Cancel)

def showInfoDialog(msg, name=''):
    if not name:
        QMessageBox.information(None, 'Infomation', msg, QMessageBox.Ok)
    else:
        QMessageBox.information(None, 'Infomation', msg % name, QMessageBox.Ok)
    
def showAboutDialog():
    description = """<h1><font size=500>Password Manager</font></h1>\n is a simple password management tool written in python and qt """
    QMessageBox.about(None, 'About', description)
