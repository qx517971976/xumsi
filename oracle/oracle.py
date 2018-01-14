#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cx_Oracle

db=cx_Oracle.connect('uaop','uaop','192.168.80.200:1521/fid')
#db=cx_Oracle.connect('uaop/uaop@192.168.80.200/fid')
cursor = db.cursor()
cursor.execute("select org_name from uaop_organization where rownum<=10")
while (1):
    row = cursor.fetchone()
    if row == None:
        break
    print("%s" % row[0])
#print(db.version)

#db.close()
