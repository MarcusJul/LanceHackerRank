def pageCount(n, p):
    # Write your code here
    def rounddown(a):
        return int(a//1)
        
    def ffirst(n,p):
        return rounddown(p/2)
        # 0 1 1 2 2 3 3
        # 1 2 3 4 5 6 7
    
    def flast(n,p):
        if n==p:
            return 0
        else:
            if n%2==0: # last page 1 page
                if n-p==1:
                    return 1
                return round((n-p)/2)
            # 4 3 3 2 2 1 1 0
            # 1 2 3 4 5 6 7 8
            else: # two pages in last page
            # 3 2 2 1 1 0 0
            # 1 2 3 4 5 6 7        
                return rounddown((n-p)/2)
    f,l = ffirst(n,p), flast(n,p)
    print(f,l)    
    return min(f,l)