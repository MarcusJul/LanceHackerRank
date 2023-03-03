def has_cycle(head):
    cnt = 0
    while(head and cnt<100):
        head = head.next
        cnt+=1
    if cnt>=100:
        return True
    else:
        return False