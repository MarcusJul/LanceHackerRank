# -*- coding: utf-8 -*-
# HackerRank IPK, Trees - Height of a binary tree

# Classic 
def height(root):
    def findH(node, cur_d):
        if node.left==None and node.right!=None:
            return max(findH(node.right,cur_d+1), cur_d)    
        elif node.left!=None and node.right==None:
            return max(findH(node.left, cur_d+1), cur_d)  
        elif node.left==None and node.right==None:
            return cur_d 
        else:
            return max(findH(node.left, cur_d+1), findH(node.right, cur_d+1))
    
    if root.left==None and root.right==None:
        return 0
    
    return findH(root, 0)

# Short version
def height(root):
    def comp(node, cd):
        if node==None: return cd
        if node.right==node.left==None:
            return cd
        else:
            return max(comp(node.left, cd+1), comp(node.right, cd+1))
    return comp(root, 0)