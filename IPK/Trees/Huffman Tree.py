def decodeHuff(root, s):
    def proceedT(node, k):
        next_node = None
        if int(k)==1:
            if node.right==None:
                res_alpha = node.data
            else:
                res_alpha, next_node = node.data, node.right
        else:
            if node.left==None:
                res_alpha = node.data
            else:
                res_alpha, next_node = node.data, node.left
        return res_alpha, next_node # res means if the next node is available, alpha is the alphabet

    i, ls, node, output = 0, len(s), root, ""

    while(i<ls):
        # look for next node
        res_alpha, node = proceedT(node, s[i])
        if not node: # if the next node is not ava, means this is a complete alphabet
            node, output = root, output+res_alpha
        else: #  if the next node is ava, means should keep digging
            i+=1

    output+=node.data
    
    print(output)
    return 