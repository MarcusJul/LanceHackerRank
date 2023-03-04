def stepPerms(n):
    # Write your code here
    d = {1:1, 2:2, 3:4}
    def countstep(n, d):
        if n in d:
            return d[n]
        else:
            s3 = countstep(n-3, d) if n>3 else 0
            if n-3 not in d:
                d[n-3] = s3
            s2 = countstep(n-2, d) if n>2 else 0
            if n-2 not in d:
                d[n-2] = s2
            s1 = countstep(n-1, d) if n>1 else 0
            if n-1 not in d:
                d[n-1] = s1
            return s1+s2+s3
    return countstep(n,d)

def stepPerms(n): # same but shorter
    # Write your code here
    d = {1:1, 2:2, 3:4}
    def countstep(n, d):
        if n in d:
            return d[n]
        else:
            out = [0,0,0]
            for i in range(1,4):
                out[i-1] = countstep(n-i, d) if n>i else 0
                if n-i not in d:
                    d[n-i] = out[i-1]
            return sum(out)
    return countstep(n,d)