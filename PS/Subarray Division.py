def birthday(s, d, m):
    # Write your code here
    flag = 0
    cnt=0
    S = s[0:m]
    if sum(S)==d:
        cnt+=1
        flag = 1
    for i in range(m, len(s)):
        if flag==1:
            if s[i]==S[0]:
                cnt+=1
            else:
                flag = 0
        else:
            if sum(S[1:])+s[i]==d:
                cnt+=1
                flag = 1
        S = s[i-m+1:i+1]
    return cnt