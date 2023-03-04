# -*- coding: utf-8 -*-
def flippingBits(n):
    bins = [2**(i) for i in range(31,-1,-1)] # create one list
    
    s, i = "", 0
    num = n
    if num not in [0,1]:
        while(i<32):
            if bins[i]<=num:
                bit, left = 1, num-bins[i]
                s += str(bit)
                num = left
            else:
                s+="0"
            i+=1
        
    else:
        if num:
            s = "0"*31+"1"
        else:
            s = "0"*32
    sr=""
    for i in range(len(s)):
        sr += "0" if int(s[i])>0 else "1"   
    i = -1
    sout = 0
    try:
        while(i>-33):
            sout += bins[i]*int(sr[i])
            i-=1
    except:
        pass
    return sout

#
def flippingBits(n):
    bins = [2**(i) for i in range(31,-1,-1)] # create one list
    
    s, i = "", 0
    num = n
    while(i<32):
        if bins[i]<=num:
            bit, left = 1, num-bins[i]
            s += str(bit)
            num = left
        else:
            s+="0"
        i+=1
        
    sr=""
    for i in range(len(s)):
        sr += "0" if int(s[i])>0 else "1"   
    i = 0
    sout = 0
    while(i<32):
        sout += bins[-i]*int(sr[-i])
        i+=1
    
    return sout
