def reverse(head):
    if (not head):
        return None
    curr = head
    prev = None
    while (curr != None):
        temp = curr.next
        curr.next = prev
        curr.prev = temp
        prev = curr
        curr = temp
    return prev
