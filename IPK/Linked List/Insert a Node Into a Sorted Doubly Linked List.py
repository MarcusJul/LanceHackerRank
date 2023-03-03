def sortedInsert(llist, data):
    # Write your code here
    cnode = DoublyLinkedListNode(data)
    if llist.data>data:
        cnode.next = llist
        return cnode
    else:
        head, node, lastnode = llist, llist, llist
        try:
            while(not (data<=node.data and lastnode.data<data)):
                lastnode = node
                node = node.next
        except:
            pass
        if node!=None:
            cnode.prev, cnode.next = lastnode, node
        lastnode.next = cnode
            
        return head