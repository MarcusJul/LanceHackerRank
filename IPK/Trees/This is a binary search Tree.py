def checkBST(root):
    d = {}
    def filld(data):
        if data in d:return False
        else: d[data] = 1
            
    def CheckB(node):
        if node==None:return False
        if not filld(node.data): return False
        if node.left!=None: resl = CheckB(node.left) 
        else: resl = True
        if node.right!=None: resr = CheckB(node.right) 
        else: resr = True
        return all([resl, resr])
    return CheckB(root)

"""
2
1 2 3 4 5 6 7 
Yes

2
3 5 7 9 11 13 15
Yes



"""