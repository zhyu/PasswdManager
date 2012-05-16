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
        cur.execute(sql, (newMD5, ))
        cur.close()

class PwdDao():
    '''
    data access object for account (password items)
    '''
    
    def __init__(self, conn):
        '''
        constructor
        '''
        self.conn = conn
        
 
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
        cur.execute(sql, (tagID, ))
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
        cur.execute(sql, (PwdID, ))
        for row in cur.fetchall():
            tag = Tag()
            (tag.id, tag.name) = row
            tagList.append(tag)
        cur.close()
        return tagList
    
    def getTagByID(self, tagID):
        sql = """ SELECT id, name FROM TAG WHERE id=? """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID, ))
        row = cur.fetchone()
        tag = Tag()
        (tag.id, tag.name) = row
        cur.close()
        return tag
    
    def getPwdCntByID(self, tagID):
        sql = """ SELECT COUNT(i.pwdid) FROM PWDTAGJOIN i, ACCOUNT a
        WHERE i.tagid=? AND i.pwdid=a.id AND a.deleted<>1 """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID, ))
        res = cur.fetchone()[0]
        cur.close()
        return res
    
    def removeTagFromAccount(self, tagID):
        sql = """ DELETE FROM PWDTAGJOIN WHERE tagid=? """
        cur = self.conn.cursor()
        cur.execute(sql, (tagID, ))
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
            cur.execute(sql, (name, ))
        else:
            sql = """ SELECT id FROM TAG WHERE name=? AND id<>? """
            cur.execute(sql, (name, ID))
        res = cur.fetchone()
        cur.close()
        return True if res == None else False
    