# -*- coding: utf-8 -*-
"""
30
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484
529
576
625
676
729
784
841
907
"""
def primality(n):
    # Write your code here
    if n ==1:
        return "Not prime"
    cur = 2
    d = {}
    flag = True
    while(cur*cur<=n):
        if cur*cur not in d: #dont need this line acty
            if n%cur!=0:
                d[cur*cur], d[cur]= 1, 1
                cur+=1
            else:
                flag = False
                break
        else:
            flag = False
            break
    return "Prime" if flag else "Not prime"
def primality(n): # best 
    # Write your code here
    if n ==1:
        return "Not prime"
    cur = 2
    flag = True
    while(cur*cur<=n):
        if n%cur!=0:
            cur+=1
        else:
            flag = False
            break

    return "Prime" if flag else "Not prime"