def timeInWords(h, m):
    # Write your code here
    d = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
    14:"fourteen", 16:"sixteen",17:"seventeen", 18:"eighteen",19:"ninteen", 20:"twenty",
    }
    if m==0:
        return "%s o' clock"%d[h]
    if m>30:
        if m==45:
            return "quarter to %s"%d[h+1]
        else:
            return "%s minute%s to %s"%(d[60-m] if m>40 else d[20]+" "+d[40-m], "" if 60-m==1 else "s", d[h+1])
    else:
        if m==15:
            return "quarter past %s"%d[h]
        elif m==30:
            return "half past %s"%d[h]
        else:
            return "%s minute%s past %s"%(d[m] if m<15 else d[20]+" "+d[m-20], "" if m==1 else "s", d[h])
    
