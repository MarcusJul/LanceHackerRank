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
    

if __name__ == '__main__':
    # fptr = open("text.py", 'w')
    from pandas import read_json
    import json
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])
    print(n,r)
    # arr = list(map(int, input().rstrip().split()))
    # arr = read_json("test.json")
    arr = []
    for line in open("test.json","r"):
        print(line)
        arr.append(json.loads(line))

    # print(arr)
    print("Starting")
    ans = countTriplets(arr, r)
    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()