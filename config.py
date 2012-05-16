# -*- coding:utf-8 -*-

# root password
# Default: password
# MD5: 5f4dcc3b5aa765d61d8327deb882cf99
ROOT_PWD = ''

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
    
def setRootPwd(newPwd):
    global ROOT_PWD
    ROOT_PWD = newPwd

def getRootPwd():
    global ROOT_PWD
    return ROOT_PWD