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
    
    def authentication(self, pwd):
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
        