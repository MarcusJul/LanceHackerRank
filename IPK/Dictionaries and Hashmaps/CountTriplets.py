# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:39:37 2023

@author: Lance
"""

def countTriplets(arr, r):
    # note that all triplets are defined by the smallest within
    d1, d2, d3 = {},{},{}
    dall = {}
    dcnt = {}# dcnt uses i of steps as key and the number of a*k and a*k*k behind this step as value
    for a in arr:
        if a in dall:
            dall[a]+=1
        else:
            dall[a] = 1
    
    # if len(dall.keys())==1:
    #     if r==1:
    #         return int(len(arr)*(len(arr)-1)*(len(arr)-2)/6)
    #     else:
    #         return 0        
    
    s = 0    
    for a in arr:
        dall[a]-=1
        a1,a2 = int(a*r), int(a*r*r)
        left1, left2 = dall[a1] if a1 in dall else 0, dall[a2] if a2 in dall else 0
        s+=1*left1*left2
    
    return int(s)
 