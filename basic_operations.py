# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:44:33 2020

@author: SOUMYA
"""
a=list("abccddde")
res=[]

for i in a:
    res.append(ord(i)-96)


l=[]
v=1
for i in range(len(res)):
    l.append(res[i])
    if(i<len(res)-1 and res[i+1]==res[i]):
        v=v+1
        d=res[i]*v
        l.append(d)
    else:
        v=1
        
l=set(l)


for i in q:
    if i in l:
        print("True")
    else:
        print("false")
