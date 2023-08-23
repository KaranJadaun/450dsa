class Solution:
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        ans = ListNode(-1, None)
        temp = ans
        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = left
                left = left.next
            else:
                temp.next = right
                temp = right
                right = right.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return ans.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.findMiddle(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        result = self.merge(left, right)
        return result
