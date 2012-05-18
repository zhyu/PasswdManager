# -*- coding:utf-8 -*-

import config, myGui, util, sys
from func import PwdFunc, TagFunc
from dialogs import *
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    '''
    main window of password manager
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        
        # value for the listCtrl
        self.pwdList = []
        self.searchResult = []
        
        # selected accountID/tagIG
        self.selectedPwdID = None
        self.selectedTagID = None
        
        # function obj
        self.pwdFunc = PwdFunc()
        self.tagFunc = TagFunc()
        
        self.initUI()
    
    def initUI(self):
        
        self.createMenu()
        self.createToolbar()
        self.createSplitter()
        
        # set the status bar
        self.statusBar().showMessage('Welcome to use Password Manager!')
        
        self.listwidget = QtGui.QListWidget()
        self.listwidget.addItem("This\nis\na\nListWidget!")
        self.treewidget = QtGui.QTreeWidget()
        self.treewidget.setHeaderLabels(['This','is','a','TreeWidgets!'])
        
        splitter = QtGui.QSplitter(self)
        splitter.addWidget(self.listwidget)
        splitter.addWidget(self.treewidget)
        self.setCentralWidget(splitter)        
        
        self.resize(*myGui.MAIN_WINDOW_SIZE)
        self.move(*myGui.MAIN_WINDOW_POSITION)
        self.setWindowTitle(config.APP_NAME + ' ' + config.VERSION)
        self.setWindowIcon(QtGui.QIcon(myGui.ICON_APP_ICON))
        
    def createMenu(self):
        # actions
        newAccAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_ADD), '&New Account', self)        
        newAccAction.setStatusTip('Add new account')
        newAccAction.triggered.connect(self.onNewAccount)
        
        accDetailAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_DETAIL), 'Account &Details', self)        
        accDetailAction.setStatusTip('Show detailed information of selected account')
        accDetailAction.triggered.connect(self.onShowDetail)
        
        editAccAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_EDIT), '&Edit Account', self)        
        editAccAction.setStatusTip('Edit the selected account')
        editAccAction.triggered.connect(self.onEditAccount)
        
        moveToTrashAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_TRASH), '&Move to Trash', self)        
        moveToTrashAction.setStatusTip('Move selected account to trash')
        moveToTrashAction.triggered.connect(self.onRemove)
        
        recoverAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_RECOVER), 'Re&cover from trash', self)        
        recoverAction.setStatusTip('Recover Selected Account from Trash')
        recoverAction.triggered.connect(self.onRecover)
        
        removeAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_REMOVE), '&Remove Selected Account', self)        
        removeAction.setStatusTip('Remove selected account')
        removeAction.triggered.connect(self.onRemove)
        
        exitAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_QUIT), 'E&xit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Password Manager')
        exitAction.triggered.connect(self.onQuit)
        
        masterPwdAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_MASTERPWD), '&Master Password', self)
        masterPwdAction.setStatusTip('Managing master password')
        masterPwdAction.triggered.connect(self.onChgMasterPwd)
        
        pwdGenAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_PWDGEN), 'Password &Generator', self)
        pwdGenAction.setStatusTip('Generating a random password')
        pwdGenAction.triggered.connect(self.onPwdGen)
        
        newTagAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_NEWTAG), '&New Tag', self)
        newTagAction.setStatusTip('Add new tag')
        newTagAction.triggered.connect(self.onNewTag)
        
        emptyTrashAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_EMPTYTRASH), '&Empty Trash', self)
        emptyTrashAction.setStatusTip('Empty trash')
        emptyTrashAction.triggered.connect(self.onEmptyTrash)
        
        aboutAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_ABOUT), '&About', self)
        aboutAction.setStatusTip('About Password Manager')
        aboutAction.triggered.connect(self.onAbout)
        
        # menus
        AccountMenu = self.menuBar().addMenu('&Account')
        AccountMenu.addAction(newAccAction)
        AccountMenu.addAction(accDetailAction)
        AccountMenu.addAction(editAccAction)
        AccountMenu.addAction(moveToTrashAction)
        AccountMenu.addAction(recoverAction)
        AccountMenu.addAction(removeAction)
        AccountMenu.addAction(exitAction)
        
        SettingMenu = self.menuBar().addMenu('&Setting')
        SettingMenu.addAction(masterPwdAction)
        SettingMenu.addAction(pwdGenAction)
        SettingMenu.addAction(newTagAction)
        SettingMenu.addAction(emptyTrashAction)
        
        HelpMenu = self.menuBar().addMenu('&Help')
        HelpMenu.addAction(aboutAction)
    
    def createToolbar(self):
        pass
    
    def createSplitter(self):
        pass
    
    # menu handlers
    def onNewAccount(self):
        dlg = NewPwdDialog(self)
        dlg.doSave()
        self.reloadWindow()
    
    def onSearch(self):
        pass
    
    def onShowDetail(self):
        pass
    
    def onEditAccount(self):
        pass
    
    def onCopyPassword(self):
        pass
    
    def onEmptyTrash(self):
        pass
    
    def onRecover(self):
        pass
    
    def onRemove(self):
        pass
    
    def onQuit(self):
        self.close()
        
    def onAbout(self):
        myGui.showAboutDialog()
    
    def onChgMasterPwd(self):
        pass
    
    def onTagMng(self):
        pass
    
    def onNewTag(self):
        newTagDlg = NewTagDialog(self)
        newTagDlg.onSave()
        self.reloadWindow()
        newTagDlg.destroy()
    
    def onEditTag(self):
        editTagDlg = EditTagDialog(self, self.selectedTagID)
        editTagDlg.onSave()
        self.reloadWindow()
        editTagDlg.destroy()
        pass
    
    def onRemoveTag(self):
        pass
    
    def onPwdGen(self):
        pass
    
    def reloadWindow(self, selectedTag=None):
        pass
    
class TagList(QtGui.QListWidget):
    pass

class PwdList(QtGui.QTreeWidget):
    pass
