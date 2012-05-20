import sqlite3 as sqlite

cx = sqlite.connect('data.db')

cu = cx.cursor()

#sql = """ CREATE TABLE MASTERPASSWORD ( md5String TEXT(700) NOT NULL ) """
#cu.execute(sql)
#cx.commit()
#sql = """ CREATE TABLE ACCOUNT  ( id INTEGER NOT NULL, title TEXT NOT NULL, username TEXT, description TEXT, password TEXT NOT NULL, deleted INTEGER DEFAULT 0, createdate DATETIME, lastupdate DATETIME, secret TEXT, PRIMARY KEY (id), CONSTRAINT ix1 UNIQUE (title) ) """
#cu.execute(sql)
#cx.commit()
#sql = """ CREATE TABLE TAG ( id INTEGER NOT NULL, name TEXT(200) NOT NULL, PRIMARY KEY (id) ) """
#cu.execute(sql)
#cx.commit()
#sql = """ CREATE TABLE PWDTAGJOIN ( tagid INTEGER NOT NULL, pwdid INTEGER NOT NULL, CONSTRAINT fktag FOREIGN KEY (tagid) REFERENCES TAG(id) CONSTRAINT fkpwd FOREIGN KEY (pwdid) REFERENCES ACCOUNT(id) ) """
#cu.execute(sql)
#cx.commit()

sql = """ insert into MASTERPASSWORD values('5f4dcc3b5aa765d61d8327deb882cf99') """

#sql = """ select * from sqlite_master where type="table" """

cu.execute(sql)
cx.commit()

#pwd = cu.fetchall()
#print pwd

