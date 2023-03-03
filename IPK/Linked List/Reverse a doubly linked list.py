def reverse(llist): # cant pass one issue
    # Write your code here
    cnode, new = llist, DoublyLinkedListNode(-1)
    flag = 0
    try:
        while(cnode.next!=None):
            tmp = cnode.next.next # No.3
            nxt = cnode.next
            nxt.next, cnode.prev = cnode, nxt# reverse 1 pair, No.1 and 2
            
            if flag==0: # first reversal
                cnode.next = None
            else:# not first reversal
                tmp_start = new.next # assign start of the reversed to a tmp ticker
                tmp_start.prev, cnode.next = cnode, tmp_start    
            new.next = nxt# assign start of the reversed to new  
            
            cnode = tmp
            flag+=1
    except:
        pass
    
    if cnode!=None: # cnode != None meaning it its not the last but its None after him 
        tmp_start = new.next
        cnode.next, tmp_start.prev = tmp_start, cnode
        # nxt.prev, cnode.next = cnode, nxt
        return cnode
    else:
        return new.next
    
def reverse(llist): # solution 2, still cant pass
    # Write your code here
    node, rev_head = llist, DoublyLinkedListNode(-1)# rev_head is the start of the reversed
    flag = 0
    if node.next==None:
        return node
    if node.next.next==None:
        tmp = node.next
        node.prev, tmp.next = tmp, node
        return tmp
    else:
        tmp = node.next.next
        nextnode = node.next
        node.prev, nextnode.next, node.next  = nextnode, node, None
        rev_head.next, node = nextnode, tmp
        
        while(node!=None): # if node is not None, reverse it
            store = node.next # store the next node
            start = rev_head.next
            start.prev, node.next = node, start
            rev_head.next = node
            node = store
    return rev_head.next