# -*- coding:utf-8 -*-

from dao import *
import config
import util
import datetime

class Func:
    def __init__(self):
        '''
        constructor
        '''
    
    def getConnection(self):
        conn = sqlite.connect(config.DB_PATH)
        return conn
    
class MasterFunc(Func):
    '''
    function about master password
    '''
    
    def __init__(self):
        '''
        constructor
        '''
        
    def getMasterPwd(self):
        '''
        get master password (md5 encrypted)
        '''
        conn = self.getConnection()
        mDao = MasterPwdDao(conn)
        res = mDao.getMasterPwd()
        conn.close()
        return res
    
    def authenticate(self, pwd):
        md5String = util.md5Encoding(pwd)
        md5Pwd = self.getMasterPwd()
        return True if md5String == md5Pwd else False
    
    def changeMasterPwd(self, newPwd):
        oldPwd = config.getMasterPwd()
        conn = self.getConnection()
        mDao = MasterPwdDao(conn)
        pDao = PwdDao(conn)
        
        # 1st re-encrypt all passwords with the new master password
        accountList = pDao.getAllPwd()
        currentDate = datetime.datetime.today()
        for account in accountList:
            dePwd = util.decrypt(oldPwd, account.pwd)
            enPwd = util.encrypt(newPwd, dePwd)
            
            if account.secret:
                deSecret = util.decrypt(oldPwd, account.secret)
                enSecret = util.encrypt(newPwd, deSecret)
            else:
                enSecret = ''
            
            deUsername = util.decrypt(oldPwd, account.username)
            enUsername = util.encrypt(newPwd, deUsername)
            
            account.pwd = enPwd
            account.username = enUsername
            account.secret = enSecret
            account.lastupdate = currentDate
            pDao.updateAccount(account.id, account.title, account.description, account.username, account.password, account.secret, account.lastupdate)
        
        # 2nd get md5 of new master password, update the masterpassword table
        newMD5String = util.md5Encoding(newPwd)
        mDao.updateMasterPwd(newMD5String)
        
        # 3rd update master password in config module
        config.setMasterPwd(newPwd)
        
        conn.commit()
        conn.close()
        
class PwdFunc(Func):
    '''
    function about account (password item)
    '''
    
    def __init__(self):
        '''
        constructor
        '''
        
    def decryptUsername(self, pwd):
        if pwd.username:
            pwd.username = util.decrypt(config.getMasterPwd(), pwd.username)
        return pwd
    
    def getAllPwd(self):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = pDao.getAllPwd()
        # decrypt username
        res = [self.decryptUsername(pwd) for pwd in res]
        conn.close()
        return res
    
    def getPwdByID(self, pwdID):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = self.decryptUsername(pDao.getPwdByID(pwdID))
        conn.close()
        return res
    
    def getAllPwdCnt(self):
        res = 0
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = pDao.getAllPwdCnt()
        conn.close()
        return res
    
    def getPwdListFromTagID(self, tagID):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = []
        if tagID == TAG_ALL: # all selected
            res = pDao.getAllPwd()
        elif tagID == TAG_TRASH: # trash selected
            res = pDao.getPwdListInTrash()
        else:
            res = pDao.getPwdListFromTagID(tagID)
        # decrypt username
        res = [self.decryptUsername(pwd) for pwd in res]
        conn.close()
        return res
    
    def updateAccount(self, id, title, description, username, password, secret, tagIDs):
        '''
        update account
        @param id: account id
        @param title: account title
        @param description: account description
        @param username: account username
        @param password: account password, it will not be updated if value is None
        @param secret: secret text from user
        @param tagIDs: a list of related tagIDs
        '''
        
        conn = self.getConnection()
        pDao = PwdDao(conn)
        pwdObj = PwdDao.getPwdByID(id)
        mPwd = config.getMasterPwd()
        
        eUsername = util.encrypt(mPwd, username) if username else ''
        ePassword = util.encrypt(mPwd, password) if password else pwdObj.pwd
        eSecret = util.encrypt(mPwd, secret) if secret else ''
        currentDate = datetime.datetime.today()
        pDao.updateAccount(id, title, description, eUsername, ePassword, eSecret, currentDate)
        pDao.updateAccountTags(id, tagIDs)
        
        conn.commit()
        conn.close()
        
    
    def addAccount(self, title, description, username, password, secret, tagIDs):
        '''
        add a user-inputed account to database
        @param title: account title
        @param description: account description
        @param username: account username
        @param password: account password
        @param secret: secret text from user
        @param tagIDs: a list of related tagIDs
        '''
        conn = self.getConnection()
        pDao = PwdDao(conn)
        
        # encrypt username & password
        mPwd = config.getMasterPwd()
        eUsername = util.encrypt(mPwd, username) if username else ''
        ePassword = util.encrypt(mPwd, password)
        eSecret = util.encrypt(mPwd, secret) if secret else ''
        currentDate = datetime.datetime.today()
        id = pDao.getAvailablePwdID()
        
        # insert
        pDao.insertAccount(id, title, description, eUsername, ePassword, eSecret, currentDate)
        
        # add tag to the new account if there is
        if len(tagIDs) > 0: pDao.setTagsOnAccount(id, tagIDs)
        
        conn.commit()
        conn.close()
    
    def getPwdCntInTrash(self):
        res = 0
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = pDao.getPwdCntInTrash()
        conn.close()
        return res
        
    
    def getSearchResult(self, keyword):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = pDao.getSearchResult(keyword)
        # decrypt username
        res = [self.decryptUsername(pwd) for pwd in res]
        conn.close()
        return res
        
    
    def recoverFromTrash(self, pwdID):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        pDao.recoverFromTrash(pwdID)
        conn.commit()
        conn.close()
    
    def moveToTrash(self, pwdID):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        pDao.moveToTrash(pwdID)
        conn.commit()
        conn.close()
    
    def deleteAccount(self, pwdID):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        pDao.deleteAccount(pwdID)
        conn.commit()
        conn.close()
    
    def emptyTrash(self):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        pDao.emptyTrash()
        conn.commit()
        conn.close()
    
    def isAccountNameValid(self, name, ID=-1):
        conn = self.getConnection()
        pDao = PwdDao(conn)
        res = pDao.isAccountNameValid(name, ID)
        conn.close()
        return res

class TagFunc(Func):
    '''
    function about tags
    '''
    
    def __init__(self):
        '''
        constructor
        '''
    def getAllTags(self):
        conn = self.getConnection()
        tDao = TagDao(conn)
        res = tDao.getAllTags()
        conn.close()
        return res
    
    def getPwdCntByTagID(self, tagID):
        conn = self.getConnection()
        tDao = TagDao(conn)
        res = tDao.getPwdCntByID(tagID)
        conn.close()
        return res
    
    def addNewTag(self, name):
        conn = self.getConnection()
        tDao = TagDao(conn)
        tDao.insertTag(name)
        conn.commit()
        conn.close()
    
    def editTag(self, tagID, name):
        conn = self.getConnection()
        tDao = TagDao(conn)
        tDao.updateTag(tagID, name)
        conn.commit()
        conn.close()
    
    def removeTag(self, tagID):
        conn = self.getConnection()
        tDao = TagDao(conn)
        tDao.deleteTag(tagID)
        conn.commit()
        conn.close()
    
    def removeTagInUse(self, tagID):
        conn = self.getConnection()
        tDao = TagDao(conn)
        tDao.removeTagFromAccount(tagID)
        tDao.deleteTag(tagID)
        conn.commit()
        conn.close()
    
    def getTagByID(self, tagID):
        conn = self.getConnection()
        tDao = TagDao(conn)
        res = tDao.getTagByID(tagID)
        conn.close()
        return res
    
    def isTagNameValid(self, name, id=-1):
        conn = self.getConnection()
        tDao = TagDao(conn)
        res = tDao.isTagNameValid(name, id)
        conn.close()
        return res
    
    def getTagNameString(self, tags):
        tagStr = '<'
        for tag in tags:
            if tag:
                tagStr += tag.name
                if tag != tags[-1]:
                    tagStr += '> <'
        tagStr += '>'
        return tagStr
    