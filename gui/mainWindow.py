# -*- coding:utf-8 -*-

import config, myGui, util, sys
from func import PwdFunc, TagFunc
from dialogs import *
from PyQt4 import QtCore, QtGui

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
        
        self.resize(*myGui.MAIN_WINDOW_SIZE)
        self.move(*myGui.MAIN_WINDOW_POSITION)
        self.setWindowTitle(config.APP_NAME + ' ' + config.VERSION)
        self.setWindowIcon(QtGui.QIcon(myGui.ICON_APP_ICON))
        
    def createMenu(self):
        # actions
        accMenuData = [ [myGui.ICON_MENU_ADD, '&New Account', 'Add new account', self.onNewAccount],
                        [myGui.ICON_MENU_DETAIL, 'Account &Details', 'Show detailed information of selected account', self.onShowDetail],
                        [myGui.ICON_MENU_EDIT, '&Edit Account', 'Edit the selected account', self.onEditAccount],
                        [myGui.ICON_MENU_TRASH, '&Move to Trash', 'Move selected account to trash', self.onRemove],
                        [myGui.ICON_MENU_RECOVER, 'Re&cover from trash', 'Recover Selected Account from Trash', self.onRecover],
                        [myGui.ICON_MENU_REMOVE, '&Remove Selected Account', 'Remove selected account', self.onRemove],
                        [myGui.ICON_MENU_QUIT, '&Quit', 'Quit Password Manager', self.onQuit] ]
        settingMenuData = [ [myGui.ICON_MENU_MASTERPWD, '&Master Password', 'Managing master password', self.onChgMasterPwd],
                            [myGui.ICON_MENU_PWDGEN, 'Password &Generator', 'Generating a random password', self.onPwdGen],
                            [myGui.ICON_MENU_NEWTAG, '&New Tag', 'Add new tag', self.onNewTag],
                            [myGui.ICON_MENU_EMPTYTRASH, '&Empty Trash', 'Empty trash', self.onEmptyTrash] ]
        
        aboutAction = QtGui.QAction(QtGui.QIcon(myGui.ICON_MENU_ABOUT), '&About', self)
        aboutAction.setStatusTip('About Password Manager')
        aboutAction.triggered.connect(self.onAbout)
        
        # menus
        AccountMenu = self.menuBar().addMenu('&Account')
        for icon, name, tip, act in accMenuData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            if name == '&Quit': action.setShortcut('Ctrl+Q')
            AccountMenu.addAction(action)
        
        SettingMenu = self.menuBar().addMenu('&Setting')
        for icon, name, tip, act in settingMenuData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            SettingMenu.addAction(action)
        
        HelpMenu = self.menuBar().addMenu('&Help')
        HelpMenu.addAction(aboutAction)
    
    def createToolbar(self):
        self.toolbar = self.addToolBar('Toolbar')
        # actions
        toolbarData= [ [myGui.ICON_TOOLBAR_ADD, 'New Account', 'Add new account', self.onNewAccount],
                        [myGui.ICON_TOOLBAR_DETAIL, 'Account Details', 'Show detailed information of selected account', self.onShowDetail],
                        [myGui.ICON_TOOLBAR_EDIT, 'Edit Account', 'Edit the selected account', self.onEditAccount],
                        [myGui.ICON_TOOLBAR_TRASH, 'Move to Trash', 'Move selected account to trash', self.onRemove],
                        [myGui.ICON_TOOLBAR_RECOVER, 'Recover from trash', 'Recover Selected Account from Trash', self.onRecover],
                        [myGui.ICON_TOOLBAR_REMOVE, 'Remove Selected Account', 'Remove selected account', self.onRemove],
                        [myGui.ICON_TOOLBAR_EMPTYTRASH, 'Empty Trash', 'Empty trash', self.onEmptyTrash],
                        ['', 'Separator', '', None],
                        [myGui.ICON_MENU_NEWTAG, 'New Tag', 'Add new tag', self.onNewTag],
                        [myGui.ICON_TOOLBAR_MASTERPWD, 'Master Password', 'Managing master password', self.onChgMasterPwd],
                        [myGui.ICON_TOOLBAR_PWDGEN, 'Password &Generator', 'Generating a random password', self.onPwdGen],
                        ['', 'Separator', '', None],
                        ['', 'TextAera', '', None],
                        [myGui.ICON_TOOLBAR_SEARCH, 'Search', 'Search', self.onSearch],
                        ['', 'Separator', '', None],
                        [myGui.ICON_TOOLBAR_QUIT, 'Quit', 'Quit Password Manager', self.onQuit] ]
        for icon, name, tip, act in toolbarData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            if name == 'Separator': self.toolbar.addSeparator()
            elif name == 'TextAera':
                self.searchBox = QtGui.QLineEdit()
                self.connect(self.searchBox, QtCore.SIGNAL('returnPressed()'), self.onSearch)
                self.toolbar.addWidget(self.searchBox)
            else:
                action.setStatusTip(tip)
                action.triggered.connect(act)
                self.toolbar.addAction(action)
    
    def createSplitter(self):
        self.listwidget = QtGui.QListWidget()
        self.listwidget.addItem("This\nis\na\nListWidget!")
        self.pwdCtrl = QtGui.QTableWidget()
        self.pwdCtrl.setColumnCount(4)
        self.pwdCtrl.setHorizontalHeaderLabels(['Tags', 'Title', 'Username', 'Description'])
        
        #self.treewidget = QtGui.QTreeWidget()
        #self.treewidget.setHeaderLabels(['This','is','a','TreeWidgets!'])
        
        splitter = QtGui.QSplitter(self)
        splitter.addWidget(self.listwidget)
        #splitter.addWidget(self.treewidget)
        splitter.addWidget(self.pwdCtrl)
        splitter.setStretchFactor(1, myGui.SPLITTER_STRETCH_FACTOR)
        self.setCentralWidget(splitter)
    
    # menu handlers
    def onNewAccount(self):
        dlg = NewPwdDialog(self)
        dlg.doSave()
        self.reloadWindow()
    
    def onSearch(self):
        myGui.showAboutDialog()
    
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
