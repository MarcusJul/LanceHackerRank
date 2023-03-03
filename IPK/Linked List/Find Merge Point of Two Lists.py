def findMergeNode(head1, head2):
    c1, c2 = [], [] # cache
    node1, node2 = head1, head2
    while(node1):
        c1.append(node1)
        node1 = node1.next
    while(node2):
        c2.append(node2)
        node2 = node2.next
    l1,l2 = len(c1), len(c2)
    lmin = min(l1,l2)
    last = None
    for i in range(lmin):
        if c1[-(i+1)]!=c2[-(i+1)]:
            return c1[-(i+1)].next.data
    return c1[0].data if l1<l2 else c2[0].data
    