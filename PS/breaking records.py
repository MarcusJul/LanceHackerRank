def breakingRecords(scores):
    # Write your code here
    maxcnt, mincnt = 0,0
    smax, smin = -1, 1000000000
    for s in scores:
        if s > smax:
            smax = s
            maxcnt += 1
        if s < smin:
            smin = s
            mincnt += 1
    return maxcnt-1, mincnt-1