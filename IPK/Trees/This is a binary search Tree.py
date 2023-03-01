def checkBST(root):
    d = {}
    def checkB(node, cmax, cmin):# cmax is max of (left) child, cmin is min of (right) child
        # Current node
        if node==None:
            return True, cmax, cmin
        else:
            if node.data in d:
                d[node.data] += 1
            else:
                d[node.data] = 1
            
            
        # node data larger than max of left
        if node.left!=None:
            resl, cmaxl, cminl = checkB(node.left, cmax, cmin)
        else:
            resl, cmaxl, cminl = True, cmax, cmin
        # node data less than min of right
        if node.right!=None:
            resr, cmaxr, cminr = checkB(node.right, cmax, cmin)
        else:
            resr, cmaxr, cminr = True, cmax, cmin
        
        if cmaxl>node.data or cminr<node.data:
            res = False
        else:
            if all([resl, resr]):
                res = True
        
        return res, max([node.data, cmaxr, cmaxl]), min([node.data, cminl, cminr])
    for k,v in d.items():
        if v>1:return False
    return checkB(root, -1, 10001)[0]

"""
2
1 2 3 4 5 6 7 
Yes

2
3 5 7 9 11 13 15
Yes



"""