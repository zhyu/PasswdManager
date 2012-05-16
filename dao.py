# -*- coding:utf-8 -*-

'''
data access object
'''

import sqlite3 as sqlite
from entity import *
import util

class MasterPwdDao(object):
    '''
    data access object for entity Master Password
    default master password: password
    encrypted MD5: 5f4dcc3b5aa765d61d8327deb882cf99
    '''
    
    def __init__(self, conn):
        '''
        constructor
        '''
        self.conn = conn

    def getMasterPwd(self):
        '''
        get master password (md5 encrypted)
        '''
        sql = """ SELECT md5String FROM MASTERPASSWORD """
        cur = self.conn.cursor()
        cur.execute(sql)
        mPwd = cur.fetchone()[0]
        cur.close()
        return mPwd
    
    def updateMasterPwd(self, newMD5):
        '''
        update master password (md5 encrypted)
        '''
        sql = """ UPDATE MASTERPASSWORD SET md5String=? """
        cur = self.conn.cursor()
        cur.execute(sql, (newMD5))
        cur.close()

class TagDao():
    '''
    data access object for tag
    '''
    
    def __init__(self, conn):
        '''
        constructor
        '''
        self.conn = conn

    def insertTag(self, name):
        tagID = self.getAvailableTagID()
        sql = """ INSERT INTO TAG (id, name) VALUES (?, ?) """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID, name))
        cur.close()
    
    def deleteTag(self, tagID):
        sql = """ DELETE FROM TAG WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID))
        cur.close()
    
    def updateTag(self, tagID, name):
        sql =  """ UPDATE TAG SET name=? WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (name, tagID))
        cur.close()
        
    def getAllTags(self):
        tagList = []
        sql = """ SELECT id, name FROM TAG """
        cur = self.conn.cursor()
        cur.execute(sql)
        for row in cur.fetchall():
            tag = Tag()
            (tag.id, tag.name) = row
            tagList.append(tag)
        cur.close()
        return tagList
    
    def getTagsByPwdID(self, PwdID):
        tagList = []
        sql = """ SELECT id, name FROM TAG WHERE id in (
        SELECT tagid FROM PWDTAGJOIN WHERE pwdid=?
        ) GROUP BY id, name """
        cur = self.conn.cursor()
        cur.execute(sql, (PwdID))
        for row in cur.fetchall():
            tag = Tag()
            (tag.id, tag.name) = row
            tagList.append(tag)
        cur.close()
        return tagList
    
    def getTagByID(self, tagID):
        sql = """ SELECT id, name FROM TAG WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID))
        row = cur.fetchone()
        tag = Tag()
        (tag.id, tag.name) = row
        cur.close()
        return tag
    
    def getPwdCntByID(self, tagID):
        res = 0
        sql = """ SELECT COUNT(i.pwdid) FROM PWDTAGJOIN i, ACCOUNT a
        WHERE i.tagid=? AND i.pwdid=a.id AND a.deleted<>1 """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID))
        res = cur.fetchone()[0]
        cur.close()
        return res
    
    def removeTagFromAccount(self, tagID):
        sql = """ DELETE FROM PWDTAGJOIN WHERE tagid=? """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID))
        cur.close()
        
    def getAvailableTagID(self):
        '''
        get the next available tag id
        '''
        sql = """ SELECT MAX(id) FROM TAG """
        cur = self.conn.cursor()
        cur.execute(sql)
        ID = cur.fetchone()[0]
        cur.close()
        return ID+1 if ID != None else 1
    
    def isTagNameValid(self, name, ID=-1):
        cur = self.conn.cursor()
        if ID == -1:
            sql = """ SELECT id FROM TAG WHERE name=? """
            cur.execute(sql, (name))
        else:
            sql = """ SELECT id FROM TAG WHERE name=? AND id<>? """
            cur.execute(sql, (name, ID))
        res = cur.fetchone()
        cur.close()
        return True if res == None else False
    
class PwdDao():
    '''
    data access object for account (password items)
    '''
    
    def __init__(self, conn):
        '''
        constructor
        '''
        self.conn = conn
        
    def getAllPwd(self):
        '''
        get all undeleted account (password items)
        '''
        pwdList = []
        sql = """ SELECT id, title, description, username, password, secret, deleted, createdate, lastupdate
        FROM ACCOUNT WHERE deleted<>1 """
        cur = self.conn.cursor()
        cur.execute(sql)
        tagDao = TagDao(self.conn)
        for row in  cur.fetchall():
            pwd = Passwd()
            (pwd.id, pwd.title, pwd.description, pwd.username, pwd.pwd, pwd.secret, pwd.deleted, pwd.createDate, pwd.lastUpdate) = row
            if pwd.id != 0:
                pwd.tags = tagDao.getTagsByPwdID(pwd.id)
                pwdList.append(pwd)
        cur.close()
        return pwdList
        
    def getPwdByID(self, pwdID):
        sql = """ SELECT id, title, description, username, password, secret, deleted, createdate, lastupdate
        FROM ACCOUNT WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (pwdID))
        tagDao = TagDao(self.conn)
        pwd = Passwd()
        (pwd.id, pwd.title, pwd.description, pwd.username, pwd.pwd, pwd.secret, pwd.deleted, pwd.createDate, pwd.lastUpdate) = cur.fetchone()
        if pwd.id != 0:
            pwd.tags = tagDao.getTagsByPwdID(pwd.id)
        cur.close()
        return pwd
    
    def getAllPwdCnt(self):
        res = 0
        sql = """ SELECT COUNT(id) FROM ACCOUNT WHERE deleted<>1 """
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()[0]
        cur.close()
        return res
    
    def getPwdListFromTagID(self, tagID):
        pwdList = []
        sql = """ SELECT id, title, description, username, password, secret, deleted, createdate, lastupdate
        FROM ACCOUNT WHERE id IN (
        SELECT pwdid FROM PWDTAGJOIN WHERE tagid=? AND deleted<>1 ) """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID))
        tagDao = TagDao(self.conn)
        for row in  cur.fetchall():
            pwd = Passwd()
            (pwd.id, pwd.title, pwd.description, pwd.username, pwd.pwd, pwd.secret, pwd.deleted, pwd.createDate, pwd.lastUpdate) = row
            if pwd.id != 0:
                pwd.tags = tagDao.getTagsByPwdID(pwd.id)
                pwdList.append(pwd)
        cur.close()
        return pwdList
        
    def updateAccount(self, id, title, description, username, password, secret, lastupdate):
        sql = """ UPDATE ACCOUNT SET title=?, description=?, username=?, password=?, secret=?, lastupdate=?
        WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (title, description, username, password, secret, lastupdate, id))
        cur.close()
        return id
    
    def insertAccount(self, id, title, description, username, password, secret, createdate):
        sql = """ INSERT INTO ACCOUNT (id, title, description, username, password, secret, createdate, lastupdate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?) """
        cur = self.conn.cursor()
        cur.execute(sql, (id, title, description, username, password, secret, createdate, createdate))
        cur.close()
        return id
    
    def recoverFromTrash(self, pwdID):
        sql = """ UPDATE ACCOUNT SET deleted=0 WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (pwdID))
        cur.close()
    
    def moveToTrash(self, pwdID):
        sql = """ UPDATE ACCOUNT SET deleted=1 WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (pwdID))
        cur.close()
    
    def emptyTrash(self):
        sql = """ DELETE FROM ACCOUNT WHERE deleted=1 """
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()
    
    def deleteAccount(self, pwdID):
        sql = """ DELETE FROM ACCOUNT WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (pwdID))
        cur.close()
    
    def setTagsOnAccount(self, accountID, tagIDs):
        sql = """ INSERT INTO PWDTAGJOIN (pwdid, tagid) VALUES (?, ?) """
        cur = self.conn.cursor()
        for tag in tagIDs:
            cur.execute(sql, (accountID, tagID))
        cur.close()
    
    def updateAccountTags(self, accountID, tagIDs):
        # 1st, remove all old tags
        sql = """ DELETE FROM PWDTAGJOIN WHERE pwdid=? """
        cur = self.conn.cursor()
        cur.execute(sql, (accountID))
        cur.close()
        
        # 2nd, insert tags passed in
        self.setTagsOnAccount(accountID, tagIDs)
    
    def getAvailablePwdID(self):
        '''
        get the next available password id
        '''
        sql = """ SELECT MAX(id) FROM ACCOUNT """
        cur = self.conn.cursor()
        cur.execute(sql)
        ID = cur.fetchone()[0]
        cur.close()
        return ID+1 if ID != None else 1
    
    def getSearchResult(self, keyword):
        '''
        username is also encrypted, so it will not be in search.
        '''
        pwdList = []
        sql = """ SELECT id, title, description, username, password FROM ACCOUNT WHERE (
        title LIKE ? OR description LIKE ?) AND deleted<>1 """
        keyword = '%' + keyword + '%'
        cur = self.conn.cursor()
        cur.execute(sql, (keyword, keyword))
        tagDao = TagDao(self.conn)
        for row in  cur.fetchall():
            pwd = Passwd()
            (pwd.id, pwd.title, pwd.description, pwd.username, pwd.pwd) = row
            if pwd.id != 0:
                pwd.tags = tagDao.getTagsByPwdID(pwd.id)
                pwdList.append(pwd)
        cur.close()
        return pwdList
    
    def getPwdListInTrash(self):
        pwdList = []
        sql = """ SELECT id, title, description, username, password, deleted, createdate, lastupdate
        FROM ACCOUNT WHERE deleted=1 """
        cur = self.conn.cursor()
        cur.execute(sql)
        tagDao = TagDao(self.conn)
        for row in  cur.fetchall():
            pwd = Passwd()
            (pwd.id, pwd.title, pwd.description, pwd.username, pwd.pwd, pwd.deleted, pwd.createDate, pwd.lastUpdate) = row
            if pwd.id != 0:
                pwd.tags = tagDao.getTagsByPwdID(pwd.id)
                pwdList.append(pwd)
        cur.close()
        return pwdList
        
    def getPwdCntInTrash(self):
        res = 0
        sql = """ SELECT COUNT(id) FROM ACCOUNT WHERE deleted=1 """
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()[0]
        cur.close()
        return res
    
    def isAccountNameValid(self, name, ID=-1):
        cur = self.conn.cursor()
        if ID == -1:
            sql = """ SELECT id FROM ACCOUNT WHERE title=? """
            cur.execute(sql, (name))
        else:
            sql = """ SELECT id FROM ACCOUNT WHERE title=? AND id<>? """
            cur.execute(sql, (name, ID))
        res = cur.fetchone()
        cur.close()
        return True if res == None else False
        