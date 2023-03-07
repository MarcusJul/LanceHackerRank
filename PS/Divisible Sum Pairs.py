"""
100 22
43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71

100 40
13 91 5 100 5 12 5 79 99 87 59 65 62 73 93 73 63 65 59 46 67 35 22 55 50 53 38 79 75 44 95 53 5 73 44 94 95 21 60 2 32 48 72 13 91 74 79 99 17 31 53 20 88 17 54 47 56 79 23 49 95 81 9 50 12 20 45 82 44 82 93 15 73 51 65 96 4 77 37 41 30 11 65 100 62 51 64 48 12 11 68 81 46 37 10 46 75 82 21 23
109

"""
def divisibleSumPairs(n, k, ar):
    # Write your code here
    ar = sorted(ar)
    d = {}
    for a in ar:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    dkeys = list(sorted(d.keys()))
    # print(sorted(ar))
    smax = ar[-1] + ar[-2]
    i, j = 1, 0
    cnt, lk = 0, len(dkeys)
    while(i*k<=smax):
        s = int(i*k)
        left, right  = dkeys[j], s - dkeys[j]
        while(left<=right):
            if right in d:
                if left==right:
                    if d[left]!=1:
                        # print("1 ",left, right, int(d[left]*(d[left]-1)/2))
                        cnt+= int(d[left]*(d[left]-1)/2)
                else:
                    # print("2 ",left, right, d[left]*d[right])
                    cnt+= d[left]*d[right]
            if j<lk-1:
                j += 1
                left, right  = dkeys[j], s - dkeys[j]
            else:
                break
        i+=1
        j = 0
    return int(cnt)