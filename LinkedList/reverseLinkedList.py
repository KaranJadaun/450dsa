def reverse(head):
    prev = None
    curr = head
    while(curr is not None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head
