# -*- coding:utf-8 -*-

import config, myGui, util, sys
from func import PwdFunc, TagFunc
from dialogs import *
from PyQt4 import QtCore, QtGui

PWDLIST = []
SEARCHRESULT = []

class MainWindow(QtGui.QMainWindow):
    '''
    main window of password manager
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        
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
        self.menuAct = []
        AccountMenu = self.menuBar().addMenu('&Account')
        for icon, name, tip, act in accMenuData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            if name == '&Quit': action.setShortcut('Ctrl+Q')
            self.menuAct.append(action)
            AccountMenu.addAction(action)
        
        SettingMenu = self.menuBar().addMenu('&Setting')
        for icon, name, tip, act in settingMenuData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            self.menuAct.append(action)
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
        self.toolbarAct = []
        for icon, name, tip, act in toolbarData:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            if name == 'Separator': self.toolbar.addSeparator()
            elif name == 'TextAera':
                self.searchBox = QtGui.QLineEdit()
                self.searchBox.setFixedWidth(300)
                self.connect(self.searchBox, QtCore.SIGNAL('returnPressed()'), self.onSearch)
                self.toolbarAct.append(action)
                self.toolbar.addWidget(self.searchBox)
            else:
                action.setStatusTip(tip)
                action.triggered.connect(act)
                self.toolbarAct.append(action)
                self.toolbar.addAction(action)
    
    def createSplitter(self):
        splitter = QtGui.QSplitter(self)
        self.pwdCtrl = PwdList(self)
        self.tagCtrl = TagList(self)
        splitter.addWidget(self.tagCtrl)
        splitter.addWidget(self.pwdCtrl)
        splitter.setStretchFactor(1, myGui.SPLITTER_STRETCH_FACTOR)
        self.setCentralWidget(splitter)
        
    def enableBtns(self):
        if self.selectedTagID == myGui.ID_TAG_TRASH: self.chgTrashTagButton(True)
        else: self.chgButtonStatus(True)
    
    def disableBtns(self):
        self.chgTrashTagButton(False)
        self.chgButtonStatus(False)
    
    def chgTrashTagButton(self, status):
        for act in self.toolbarAct:
            if act.text() in myGui.NAMES_TRASHTAG_TOOLBAR:
                act.setEnabled(status)
        for act in self.menuAct:
            if act.text() in myGui.NAMES_TRASHTAG_MENU:
                act.setEnabled(status)
    
    def chgButtonStatus(self, status):
        for act in self.toolbarAct:
            if act.text() in myGui.NAMES_ENDISABLE_TOOLBAR:
                act.setEnabled(status)
        for act in self.menuAct:
            if act.text() in myGui.NAMES_ENDISABLE_MENU:
                act.setEnabled(status)
    
    # menu handlers
    def onNewAccount(self):
        dlg = NewAccountDlg(self)
        dlg.doSave()
        self.reloadWindow()
    
    def onSearch(self):
        keyword = unicode(self.searchBox.text())
        if len(keyword) == 0:
            myGui.showErrorDialog(myGui.ERR_SEARCH_EMPTY)
        else:
            global SEARCHRESULT
            SEARCHRESULT = self.pwdFunc.getSearchResult(keyword)
            self.reloadWindow(myGui.ID_TAG_SEARCH)
    
    def onShowDetail(self):
        dlg = AccountDetailDlg(self, self.selectedPwdID)
        dlg.exec_()
        dlg.destroy()
    
    def onEditAccount(self):
        dlg = EditAccountDlg(self, self.selectedPwdID)
        dlg.onSave()
        self.reloadWindow()
        dlg.destroy()
    
    def onCopyPassword(self):
        account = self.pwdFunc.getPwdByID(self.selectedPwdID)
        # decrypt password
        dePwd = util.decrypt(config.getMasterPwd(), account.pwd)
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(dePwd)
        myGui.showInfoDialog(myGui.INFO_CLIPBOARD, account.title)
    
    def onEmptyTrash(self):
        if myGui.showConfirmationDialog(myGui.CONFIRM_EMPTY_TRASH) == QtGui.QMessageBox.Ok:
            self.pwdFunc.emptyTrash()
            self.reloadWindow()
    
    def onRecover(self):
        account = self.pwdFunc.getPwdByID(self.selectedPwdID)
        self.pwdFunc.recoverFromTrash(account.id)
        self.reloadWindow()
        myGui.showInfoDialog(myGui.INFO_RECOVERED, account.title)
    
    def onRemove(self):
        '''
        if the currentTag is not Trash, move the selected accouont to Trash. Otherwise remove the account.
        '''
        account = self.pwdFunc.getPwdByID(self.selectedPwdID)
        
        if self.selectedTagID == myGui.ID_TAG_TRASH:
            if myGui.showConfirmationDialog(myGui.CONFIRM_COMPLETE_REMOVE, account.title) == QtGui.QMessageBox.Ok:
                self.pwdFunc.deleteAccount(account.id)
                self.reloadWindow(self.selectedTagID)
        else:
            if myGui.showConfirmationDialog(myGui.CONFIRM_MOVETO_TRASH, account.title) == QtGui.QMessageBox.Ok:
                self.pwdFunc.moveToTrash(account.id)
                
                # if the currentTag is SearchResult, SearchList need to be maintained.
                if self.selectedTagID == myGui.ID_TAG_SEARCH:
                    global SEARCHRESULT
                    for pwd in SEARCHRESULT:
                        if pwd.id == account.id:
                            SEARCHRESULT.remove(pwd)
                            break
                self.reloadWindow(self.selectedTagID)
    
    def onQuit(self):
        self.close()
        
    def onAbout(self):
        myGui.showAboutDialog()
    
    def onChgMasterPwd(self):
        masterDlg = ChgMasterPwdDlg(self)
        masterDlg.onChg()
        self.reloadWindow()
        masterDlg.destroy()
    
    def onNewTag(self):
        newTagDlg = NewTagDlg(self)
        newTagDlg.onSave()
        self.reloadWindow()
        newTagDlg.destroy()
    
    def onEditTag(self):
        editTagDlg = EditTagDlg(self, self.selectedTagID)
        editTagDlg.onSave()
        self.reloadWindow()
        editTagDlg.destroy()
    
    def onRemoveTag(self):
        tag = self.tagFunc.getTagByID(self.selectedTagID)
        cnt = self.tagFunc.getPwdCntByTagID(tag.id)
        if cnt > 0:
            if myGui.showConfirmationDialog(myGui.CONFIRM_REMOVE_USEDTAG, tag.name) == QtGui.QMessageBox.Ok:
                self.tagFunc.removeTagInUse(tag.id)
                self.reloadWindow()
        elif myGui.showConfirmationDialog(myGui.CONFIRM_REMOVE_TAG, tag.name) == QtGui.QMessageBox.Ok:
            self.tagFunc.removeTag(tag.id)
            self.reloadWindow()
    
    def onPwdGen(self):
        pwdGenDlg = PwdGenDlg(self)
        pwdGenDlg.generatePwd()
    
    def reloadWindow(self, selectedTag=None):
        if not selectedTag:
            selectedTag = myGui.ID_TAG_ALL
        self.tagCtrl.loadTags(selectedTag)
    
class TagList(QtGui.QListWidget):
    def __init__(self, parent):
        super(TagList, self).__init__()
        self.parent = parent
        self.installEventFilter(self)
        self.initUI()
        
    def mousePressEvent(self, event):
        if event.button() in [QtCore.Qt.LeftButton, QtCore.Qt.RightButton]:
            item = self.itemAt(event.pos())
            if not item: self.clearSelection()
            else: self.setCurrentItem(item)
    
    def initUI(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.tagMenu)
        self.connect(self, QtCore.SIGNAL('currentRowChanged(int)'), self.onSelect)
        self.loadTags()
        
    def tagMenu(self):
        self.menu = QtGui.QMenu()
        menuData = [[myGui.ICON_MENU_NEWTAG, 'Add new tag', 'Add new tag', self.parent.onNewTag],
                    [myGui.ICON_MENU_EDIT, 'Edit tag', 'Edit tag', self.parent.onEditTag],
                    [myGui.ICON_MENU_DELTAG, 'Delete tag', 'Delete tag', self.parent.onRemoveTag] ]
        cur = self.itemAt(self.mapFromGlobal(QtGui.QCursor.pos()))
        popup = menuData[:1] if (not cur or cur.type()<0) else menuData
        for icon, name, tip, act in popup:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            self.menu.addAction(action)
        self.menu.exec_(QtGui.QCursor.pos())
    
    def loadTags(self, selectedID=myGui.ID_TAG_ALL):
        pwdFunc = PwdFunc()
        tagFunc = TagFunc()
        
        allPwdCnt = pwdFunc.getAllPwdCnt()
        trashPwdCnt = pwdFunc.getPwdCntInTrash()
        tagList = tagFunc.getAllTags()
        self.clear()
        
        idxData = []
        for tag in tagList:
            idxData.append(tag.id)
            cnt = tagFunc.getPwdCntByTagID(tag.id)
            item = QtGui.QListWidgetItem(QtGui.QIcon(myGui.ICON_TAG_CUSTOM), '%s (%d)' % (tag.name, cnt), None, tag.id)
            item.setSizeHint(QtCore.QSize(60, 32))
            self.addItem(item)

        tagAdv = [ QtGui.QListWidgetItem(QtGui.QIcon(myGui.ICON_TAG_ALL), 'All (%d)' % allPwdCnt, None, myGui.ID_TAG_ALL),
                   QtGui.QListWidgetItem(QtGui.QIcon(myGui.ICON_TAG_SEARCH), 'Result (%d)' % len(SEARCHRESULT), None, myGui.ID_TAG_SEARCH),
                   QtGui.QListWidgetItem(QtGui.QIcon(myGui.ICON_TAG_TRASH), 'Trash (%d)' % trashPwdCnt, None, myGui.ID_TAG_TRASH) ]
        for tagItem in tagAdv:
            tagItem.setSizeHint(QtCore.QSize(60, 32))
            self.addItem(tagItem)
        idxData.extend([-1, -2, -3])
        self.setCurrentRow(idxData.index(selectedID))
        #self.show()
        
    def onSelect(self):
        cur = self.currentItem()
        tagID = cur.type() if cur else myGui.ID_TAG_ALL
        self.parent.selectedTagID = tagID
        pwdFunc = PwdFunc()
        
        pwdCtrl = self.parent.pwdCtrl
        if tagID == myGui.ID_TAG_SEARCH:
            pwdCtrl.loadSearchResult()
        else:
            global PWDLIST
            PWDLIST = pwdFunc.getPwdListFromTagID(tagID)
            pwdCtrl.loadPwd()

class PwdList(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(QtGui.QTableWidget, self).__init__()
        self.parent = parent
        self.initUI()
    
    def mousePressEvent(self, event):
        if event.button() in [QtCore.Qt.LeftButton, QtCore.Qt.RightButton]:
            item = self.itemAt(event.pos())
            if not item:
                self.clearSelection()
                self.onDeselect()
            else:
                self.setCurrentItem(item)
                self.onSelect()
    
    def initUI(self):
        # display format
        self.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setFixedHeight(25)
        self.verticalHeader().setVisible(False)
        
        # context menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.pwdMenu)
        self.loadPwd()
        
    def pwdMenu(self):
        self.menu = QtGui.QMenu()
        menuData = [ [myGui.ICON_MENU_ADD, 'Add new account', 'Add new account', self.parent.onNewAccount],
                     [myGui.ICON_MENU_DETAIL, 'Account details', 'Show detailed information of selected account', self.parent.onShowDetail],
                     [myGui.ICON_MENU_EDIT, 'Edit account', 'Edit the selected account', self.parent.onEditAccount],
                     [myGui.ICON_MENU_PASTE, 'Copy password to clipboard', 'Copy decrypted password of selected account to clipboard', self.parent.onCopyPassword],
                     [myGui.ICON_MENU_TRASH, 'Move to trash', 'Move selected account to trash', self.parent.onRemove],
                     [myGui.ICON_MENU_REMOVE, 'Delete from trash', 'Delete selected account from trash', self.parent.onRemove],
                     [myGui.ICON_MENU_RECOVER, 'Recover from trash', 'Recover selected account from trash', self.parent.onRecover] ]
        popup = []
        # position fix
        p = self.mapFromGlobal(QtGui.QCursor.pos())
        p.setX(p.x() - 25)
        p.setY(p.y() - 25)
        cur = self.itemAt(p)
        if self.parent.selectedTagID != myGui.ID_TAG_TRASH:
            popup = menuData[1:-2] if cur != None else menuData[:1]
        elif cur != None: popup = menuData[-2:]
        for icon, name, tip, act in popup:
            action = QtGui.QAction(QtGui.QIcon(icon), name, self)
            action.setStatusTip(tip)
            action.triggered.connect(act)
            self.menu.addAction(action)
        self.menu.exec_(QtGui.QCursor.pos())
    
    def onSelect(self):
        row = self.currentRow()
        self.parent.selectedPwdID = self.pwdIdx[row]
        self.parent.enableBtns()
    
    def onDeselect(self):
        self.parent.selectedPwdID = None
        self.parent.disableBtns()
    
        
    def loadSearchResult(self):
        global PWDLIST
        PWDLIST = SEARCHRESULT
        self.loadPwd()
    
    def loadPwd(self):
        self.clear()
        self.onDeselect()
        self.setRowCount(0)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Tags', 'Title', 'Username', 'Description'])
        wid = [200, 150, 200]
        for cid, wid in enumerate(wid): self.setColumnWidth(cid, wid)
        
        tagFunc = TagFunc()
        self.pwdIdx = []
        for idx, pwd in enumerate(PWDLIST):
            row = self.rowCount()
            self.insertRow(row)
            tags = pwd.tags
            tagStr = tagFunc.getTagNameString(tags)
            self.setItem(idx, 0, QtGui.QTableWidgetItem(tagStr, 1))
            self.setItem(idx, 1, QtGui.QTableWidgetItem(pwd.title, 1))
            self.setItem(idx, 2, QtGui.QTableWidgetItem(pwd.username, 1))
            self.setItem(idx, 3, QtGui.QTableWidgetItem(pwd.description, 1))
            self.pwdIdx.append(pwd.id)