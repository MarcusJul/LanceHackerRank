def isBalanced(s):
    left = ["(", "[", "{"]
    d = {"(":")", "{":"}", "[":"]"}
    lenS = len(s)
    ls, out = [], True
    for i in range(lenS):
        if s[i] in left:
            ls.append(s[i])
        else:
            if ls!=[]:
                p = ls.pop()
                if d[p]==s[i]:
                    continue
                else:
                    out = False
                    break
            else:
                out = False
                break
    if ls!=[]:
        out=False
    return "YES" if out else "NO"