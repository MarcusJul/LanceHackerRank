def riddle(arr):
    # complete this function
    l = len(arr)
    out = []
    for wind in range(1,l+1): 
        stack = arr[:wind]
        # print(stack)
        mins = min(stack)
        minall = mins
        for i in range(wind,l):
            item = stack.pop(0)
            # print(stack)
            if arr[i]<=mins:
                mins = arr[i]
            else:
                if item==mins:
                    if wind!=1:
                        mins = min(min(stack), arr[i])
                    else:
                        mins = arr[i]
            minall = max(mins, minall)
            stack.append(arr[i])
            
        out.append(minall)
    return out