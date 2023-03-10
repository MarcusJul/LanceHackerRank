def encryption(s):
    # Write your code here
    ss = "".join(s.split(" "))
    l = len(ss)
    lsq = l**(1/2)
    upper = lsq//1+1 if not lsq.is_integer() else lsq
    row, col, cnt, d = int(upper), int(upper), 0, {}
    
    while(row*col>=l):
        d[cnt] = [row, col]
        print(row, col)
        if row==col:
            row-=1
        else:
            col-=1
            
    i, im = 0, d[0][0]*d[0][1]
    for k,v in d.items():
        if v[0]*v[1]<im:
            im, i = v[0]*v[1], k
    row, col = int(d[k][0]), int(d[k][1])
    print(row, col)
    mat,r,c,tmp = [],0,0,[]
    for j in range(l):
        tmp.append(ss[j])
        c+=1
        if c==col:
            mat.append(tmp)
            tmp = []
            r, c = r+1, 0

    mat.append(tmp)
        
    out = ""
    for c in range(col):
        for r in range(row):
            try:
                out = out+mat[r][c]
            except:
                pass
        out = out+" "
    return out