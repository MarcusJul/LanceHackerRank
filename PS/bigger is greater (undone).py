def biggerIsGreater(w):
    # Write your code here
    s="abcdefghijklmnopqrstuvwxyz"
    d = {}
    for i,a in enumerate(s):
        d[a]=i
    
    nums = [d[a] for a in w]
    
    def comp(a,b):
        i=0 # a>b 1, a<b -1, a==b 0
        if a==b:
            return 0,-1
        while(True):
            if a[i]>b[i]:
                return 1,i
            elif a[i]<b[i]:
                return -1,i
            else:
                i+=1
    
    store, prev = [],nums[-1]
    for i in range(len(w)-2,-1,-1):
        if nums[i]<prev:
            store.append(i+1)
        prev = nums[i]
    print(nums, "".join([s[a] for a in nums]))

        
    
    if store==[]:
        return "no answer"
    else:
        if store[0]!=0:
            nums = cons(nums, store[0])
            return "".join([s[a] for a in nums])
            
        else:
            return "no answer"