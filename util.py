# -*- coding:utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Hash import MD5
import binascii
import urllib2
import string, random

# algorithm
MODE = AES.MODE_CBC

def __getKeyObject(key):
    obj = AES.new(md5Encoding(key), MODE)
    return obj

def md5Encoding(msg):
    '''
    get md5 encrypted text
    @param msg: the plain text message
    '''
    m = MD5.new()
    m.update(msg)
    return m.hexdigest()

def getRandomString(length, optionList=['number', 'lower', 'upper', 'punc']):
    charPool = {'number' : string.digits,
                'lower'  : string.lowercase,
                'upper'  : string.uppercase,
                'punc'   : string.punctuation }
    pool = ''
    for key in optionList:
        if charPool.has_key(key):
            pool = pool + charPool.get(key)
    s = [random.choice(pool) for _ in xrange(length)]
    return ''.join(s)

def encrypt(key, msg):
    '''
    Encrypt message using given password
    @param key: the master password
    @param msg: the plain text to be encrypted
    '''
    obj = __getKeyObject(key)
    
    # encrypt
    xx = msg*16
    cipher = obj.encrypt(xx)
    
    # convert bin to string
    s = binascii.b2a_hex(cipher)
    return s
    
def decrypt(key, msg):
    '''
    Encrypt message
    @param key: the master password
    @param msg: the cipher text to be dencrypted
    '''
    obj = __getKeyObject(key)
    
    # convert string to bin
    b = binascii.a2b_hex(msg)
    
    # decrypt
    plain = obj.decrypt(b)
    return plain[:len(plain)/16]

def getLastVersion(versionUrl):
    ver = ''
    try:
        f = urllib2.urlopen(versionUrl)
        s = f.read()
        f.close()
        ver = s.split(' ')[1]
    except:
        pass
    return ver