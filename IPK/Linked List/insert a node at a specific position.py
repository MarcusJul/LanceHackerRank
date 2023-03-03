def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if position==1:
        node = SinglyLinkedListNode(data, llist)
        node.next = llist
        return node
    else:
        cnt = 0
        head, node, lastnode = llist, llist, None
        while(cnt<position):
            cnt+=1
            lastnode = node
            node = node.next
        innode = SinglyLinkedListNode(data)
        innode.next = node
        lastnode.next = innode
        return head