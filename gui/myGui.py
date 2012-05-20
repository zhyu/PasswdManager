# -*- coding:utf-8 -*-

import config, dialogs
from PyQt4.QtGui import QMessageBox

##################################
# ICON path properties
##################################
# icon root path
ICON_ROOT='gui/icons/'

ICON_APP_LOGO = ICON_ROOT + 'app.png'
ICON_APP_ICON = ICON_ROOT + 'app16.png'

# tag icon used in main window
ICON_TAG_CUSTOM = ICON_ROOT + 'tagM.png'
ICON_TAG_ALL = ICON_ROOT + 'allTags.png'
ICON_TAG_TRASH = ICON_ROOT + 'trash.png'
ICON_TAG_SEARCH = ICON_ROOT + 'result.png'
ICON_TAG_FAV = ICON_ROOT + 'favs.png'

ICON_TOOLBAR_ADD = ICON_ROOT + 'add.png'
ICON_TOOLBAR_QUIT = ICON_ROOT + 'exit.png'
ICON_TOOLBAR_SEARCH = ICON_ROOT + 'search.png'
ICON_TOOLBAR_REMOVE = ICON_ROOT + 'remove.png'
ICON_TOOLBAR_TRASH = ICON_TAG_TRASH
ICON_TOOLBAR_EMPTYTRASH = ICON_ROOT + 'empty.png'
ICON_TOOLBAR_DETAIL = ICON_ROOT + 'detail.png'
ICON_TOOLBAR_RECOVER = ICON_ROOT + 'recover.png'
ICON_TOOLBAR_MASTERPWD = ICON_ROOT + 'masterpwd.png'
ICON_TOOLBAR_EDIT = ICON_ROOT + 'edit.png'
ICON_TOOLBAR_PWDGEN =ICON_ROOT + 'pwdgen.png'

ICON_MENU_ADD = ICON_ROOT + 'add16.png'
ICON_MENU_REMOVE = ICON_ROOT + 'remove16.png'
ICON_MENU_QUIT = ICON_ROOT + 'exit16.png'
ICON_MENU_DETAIL = ICON_ROOT + 'detail16.png'
ICON_MENU_EMPTYTRASH = ICON_ROOT + 'empty16.png'
ICON_MENU_ABOUT = ICON_ROOT + 'about16.png'
ICON_MENU_RECOVER = ICON_ROOT + 'recover16.png'
ICON_MENU_TRASH = ICON_ROOT + 'trash16.png'
ICON_MENU_PASTE = ICON_ROOT + 'paste16.png'
ICON_MENU_MASTERPWD = ICON_ROOT + 'masterpwd16.png'
ICON_MENU_NEWTAG =ICON_ROOT + 'newtag16.png'
ICON_MENU_DELTAG =ICON_ROOT + 'deltag16.png'
ICON_MENU_EDIT =ICON_ROOT + 'edit16.png'
ICON_MENU_PWDGEN =ICON_ROOT + 'pwdgen16.png'

##################################
# GUI size/position properties
##################################
# Application window size,position
MAIN_WINDOW_SIZE=(1100,700)
MAIN_WINDOW_POSITION=(100,80)

# splitter stretch factor
SPLITTER_STRETCH_FACTOR = 200 

##################################
# special tag id
##################################

ID_TAG_ALL = -1
ID_TAG_SEARCH = -2
ID_TAG_TRASH = -3

ID_TOOLBAR_DETAIL   = 7677 
ID_TOOLBAR_REMOVE   = 7676
ID_TOOLBAR_TRASH    = 7675
ID_TOOLBAR_RECOVER  = 7674
ID_TOOLBAR_EDIT     = 7673

ID_MENU_DETAIL      = 7672
ID_MENU_ADD         = 7671
ID_MENU_REMOVE      = 7670
ID_MENU_TRASH       = 7669
ID_MENU_RECOVER     = 7668
ID_MENU_EDIT        = 7667
ID_MENU_QUIT        = 7666

#enable/disable NAMEs
NAMES_ENDISABLE_MENU = ['Account &Details', '&Edit Account', '&Move to Trash']
NAMES_ENDISABLE_TOOLBAR = ['Account Details', 'Edit Account', 'Move to Trash']
NAMES_TRASHTAG_MENU = ['Re&cover from trash', '&Remove Selected Account']
NAMES_TRASHTAG_TOOLBAR = ['Recover from trash', 'Remove Selected Account']

##################################
# Information messages
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
# Confirmation messages
##################################
CONFIRM_MOVETO_TRASH = """Are you sure to move the account [%s]?"""
CONFIRM_COMPLETE_REMOVE = """Are you sure to PERMANENTLY DELETE the account [%s]?"""
CONFIRM_EMPTY_TRASH = """Are you sure to empty the trash?"""
CONFIRM_REMOVE_TAG = """Are you sure to remove the tag [%s]?"""
CONFIRM_REMOVE_USEDTAG = """Removing tag [%s] will NOT remove related accounts. Continue to remove Tag?"""

##################################
# Error messages
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
    header = """<h1><img src=""" + ICON_APP_LOGO + """></img>   Password Manager</h1>"""
    description = """ a simple password management tool written in python and qt """
    cprt = """ <p align="right">(C) 2012 zhyu</p> """
    QMessageBox.about(None, 'About', header+description+cprt)
