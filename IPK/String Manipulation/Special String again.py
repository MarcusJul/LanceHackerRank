# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:15:13 2023

@author: Lance
"""
# too slow
def substrCount(n, s):
    
    cnt = n
    def findS(st, l):
        if len(list(set(st)))==1:
            return True 
        if l%2==0:
            return False
        else:
            # st[int(l-1)/2]
            mid = st[int((l-1)/2)]
            if mid!=st[int((l-1)/2+1)] and st[int((l-1)/2-1)]!=mid and len(list(set(st)))<=2:
                return True
            else:
                return False 
            
    for i in range(2,n+1):
        for k in range(n-i+1):
            if findS(s[k:k+i],i):
                cnt+=1
    
    return cnt