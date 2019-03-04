#!/usr/bin/env python
# import requests
# import time
# import hashlib
# import json

# from cassandra.cluster import Cluster


from cassandra.cluster import Cluster
dbServer = "127.0.0.1"
keyspace = "galley_db"


def getMemberRef():
    selectMemberRef = 'SELECT conv, child, parent, cdate FROM member_ref'
    rows = session.execute(selectMemberRef)
    mems = []

    for r in rows:
        m = {}
        m['conv'] = str(r.conv)
        m['child'] = str(r.child)
        m['parent'] = str(r.parent)
        m['cdate'] = r.cdate
        mems.append(m)
    return mems


def updateMemberRef(conv ,uid):
    update = 'INSERT INTO member_ref (conv, child, parent, cdate) VALUES (%s, %s, %s, dateof(now()));'%(conv,uid,conv)
    session.execute(update)

def deleteMemberRef(conv ,uid):
    delete = 'delete from member_ref where conv = %s and child = %s and parent = %s'%(conv,uid,uid)
    session.execute(delete)

def main():
    refs = getMemberRef()
    for r in refs:
        if r['child'] == r['parent']:
            print r['child']
            deleteMemberRef(r['conv'],r['child'])
            updateMemberRef(r['conv'],r['child'])

    print 'update sucess ...'
            


cluster = Cluster([dbServer])
session = cluster.connect(keyspace)


if __name__ == "__main__":
    main()
