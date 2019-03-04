#!/usr/bin/env python
# import requests
# import time
# import hashlib
# import json
import sys
# from cassandra.cluster import Cluster


from cassandra.cluster import Cluster
dbServer = "127.0.0.1"
keyspace = "brig_db"


def getRemarks():
    selectRemarks = 'select left, right, remark from connection2;'
    rows = session.execute(selectRemarks)
    mems = []

    for r in rows:
        m = {}
        m['left'] = str(r.left)
        m['right'] = str(r.right)
        m['remark'] = str(r.remark)
        mems.append(m)
    return mems

def getUsers():
    select = 'select left, right from connection;'
    rows = session.execute(select)
    users = {}
    for r in rows:
        users[str(r.left)] = str(r.right)

    return users


def updateRemark(left, right, remark):
    update = 'update connection set remark = \'%s\' where left = %s and right = %s;'%(remark,left,right)
    session.execute(update)

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    remarks = getRemarks()
    users = getUsers()
    for r in remarks:
        left = r['left']
        right = r['right']
        if(users.get(left,None) == right):
            print('update left=%s and right=%s ' % (left,right))
            updateRemark(left,right,r['remark'])
            

    print('update sucess ...')
            


cluster = Cluster([dbServer])
session = cluster.connect(keyspace)


if __name__ == "__main__":
    main()
