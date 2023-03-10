def biggerIsGreater(w):
    # Write your code here
    
    s="abcdefghijklmnopqrstuvwxyz"
    
    d = {}
    for i,a in enumerate(s):
        d[a]=i
    
    nums = [d[a] for a in w]
    if len(w)==2:
        if nums[1]>nums[0]:
            return w[1]+w[0]
        else:
            return "no answer"

    # def comp(a,b):
    #     i=0 # a>b 1, a<b -1, a==b 0
    #     if a==b:
    #         return 0,-1
    #     while(True):
    #         if a[i]>b[i]:
    #             return 1,i
    #         elif a[i]<b[i]:
    #             return -1,i
    #         else:
    #             i+=1
    
    store, prev = [],nums[-1]
    for i in range(len(w)-2,-1,-1):
        if nums[i]<prev:
            store.append(i+1)
        prev = nums[i]
    print(nums, "".join([s[a] for a in nums]))
    def cons(nums, i):
        print(i) # i is where the number is larger then the number befroe it for the first time
        start = i-1
        f = nums[:i+1] # i is the last of this
        t = nums[i+1:]
        st = sorted(t)
        print(t)
        if t==st and st!=[]: # meaning behind
            if len(f)>1:
                if f[-1]-f[-2]>f[-1]-st[0]:
                    # fina the value in st, which is the smallest among all the numbers larger than f[-2]

                    for j in range(1,len(st)):
                        if st[j]<=f[-2]:
                            break
                    st[j], f[-2] = f[-2], st[j]
                    st = sorted(st)
                    return f+st
                else:
                    f[-1], f[-2] = f[-2], f[-1]
            else:
                return f+t
        # the key is given an array, find the combination that is smallest among all
        # the combination larger
        return f+t