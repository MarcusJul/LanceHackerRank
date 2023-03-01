"""
8
8 4 9 1 2 3 6 5
1 2
1

9
8 6 5 7 11 12 13 10 9
9 12
11
"""
def lca(root, v1, v2):
    
    # Define a function that searches for both v1 and v2 from the node
    # if you can find it on one leg, keep finding and return the last node from which v1 and v2 can be found
    # otherwise this is not a common ancestor for both
    def findone(node, v):
        if node==None: return False
        if node.left==v or node.right==v or node==v: return True
        else: return any([findone(node.left, v), findone(node.right, v)])
        
    def findboth(node, lvl):
        res1, res2 = findone(node,v1), findone(node,v2)
        if all([res1, res2]):
            lnode, llvl = findboth(node.left, lvl+1)
            rnode, rlvl = findboth(node.right, lvl+1)
            return (lnode, llvl) if llvl>=rlvl else (rnode, rlvl)
        else:
            return (node, lvl)
    
    return findboth(root, 0)[0]