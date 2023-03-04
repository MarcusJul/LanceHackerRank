def superDigit(n, k):
    def SumD(n):
        if int(n)<10: return int(n)
            
        s, out = sum([int(a) for a in n]), ""
        while(s>0):
            left, right = s//10, s%10
            out, s = str(right) + out, left
        return SumD(out)
    sec = SumD(str(SumD(n)*k))
    return sec