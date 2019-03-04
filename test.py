#!/usr/bin/env python
 
var1 = 'Hello World!'
var2 = "Runoob"
v = "a1=[0] a2=[1]"
name = 'name111'
age  = 33
sex  = 'man'
mems = []
dictU = {}
for r in range(0,5):
    m = {}
    m['conv'] = 'c:%s'%(r)
    mems.append(m)
    dictU[r] = 'c:%s'%(r)
print dictU
aa = dictU.get(9,"a")
print 'dict9=' + aa
# for mm in mems:
    # print mm['conv']

message = '''Information of %s : Name:%s Age:%s Sex:%s''' %(name,name,age,sex)
print message
print "var1[0]: var2[1]:", var1 ,var2
# print "var2[1]: ", var2