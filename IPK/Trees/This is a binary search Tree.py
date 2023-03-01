""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

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
            
        res = True
        if cmaxl>node.data or cminr<node.data:
            res = False
        
        return all([res, resr, resl]), max([node.data, cmaxr, cmaxl]), min([node.data, cminl, cminr])
 
    res = checkB(root, -1, 10001)[0]
    if sum(d.values())>len(d.keys()):
        return False

    return res
        
    

"""
2
1 2 3 4 5 6 7 
Yes

2
3 5 7 9 11 13 15
Yes

2
1 2 2 4 5 6 7
No

4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31
No
"""