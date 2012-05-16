# -*- coding:utf-8 -*-

# master password
# Default: password
# MD5: 5f4dcc3b5aa765d61d8327deb882cf99
MASTER_PWD = ''

# database path
DB_PATH = 'data/data.db'

# version
VERSION = '0.0.1'
VERSION_URL = 'https://github.com/angellwings/PasswdManager/raw/master/version'
LATEST_VERSION = None

# APP_Name
APP_NAME = 'PasswdManager'

def setLatestVersion(version):
    global LATEST_VERSION
    LATEST_VERSION = version
    
def setMasterPwd(newPwd):
    global MASTER_PWD
    MASTER_PWD = newPwd

def getMasterPwd():
    global MASTER_PWD
    return MASTER_PWD