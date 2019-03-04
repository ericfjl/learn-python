#!/usr/bin/env python
# import requests
# import time
# import hashlib
# import json

# from cassandra.cluster import Cluster


from cassandra.cluster import Cluster
dbServer = "127.0.0.1"
keyspace = "brig_db"


def getUserRef():
    selectUserRef = 'select id,user_address,user_referrerid, user_referrer_address from user;'
    rows = session.execute(selectUserRef)
    mems = []

    for r in rows:
        m = {}
        m['id'] = str(r.id)
        m['user_address'] = str(r.user_address)
        m['user_referrerid'] = str(r.user_referrerid)
        m['user_referrer_address'] = r.user_referrer_address
        mems.append(m)
    return mems


def updateUserRef(uid ,ref):
    update = 'update user set user_referrerid = %s where id = %s;'%(ref,uid)
    session.execute(update)

def main():
    refs = getUserRef()
    dictU = {}
    for r in refs:
        addr = r['user_address']
        if addr is not None and len(addr) >10:
            dictU[r['user_address']] = r['id']
    for r in refs:
        ref_addr = r['user_referrer_address']
        if ref_addr is not None and len(ref_addr) >10:
            uid = r['id']
            addr = r['user_address']
            # print 'id=%s,addr=%s,ref_addr=%s'%(uid,addr,ref_addr)
            ref = dictU.get(ref_addr,None)
            if ref is not None:
                updateUserRef(uid,ref)

    print 'update sucess ...'
            


cluster = Cluster([dbServer])
session = cluster.connect(keyspace)


if __name__ == "__main__":
    main()
