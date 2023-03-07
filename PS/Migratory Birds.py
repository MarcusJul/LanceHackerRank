def migratoryBirds(arr):
    # Write your code here
    d = {}
    for a in arr:
        if a in d:
            d[a]+=1
        else:
            d[a] = 1
    store = []
    m = -1
    for k,v in d.items():
        if v>m:
            store = [k]
            m=v
        elif v==m:
            store.append(k)
        else:
            pass
    return min(store)