class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(left, right) -> Optional[ListNode]:
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
        if len(lists) == 0: return None 
        if len(lists) == 1: return lists[0]
        newHead = mergeTwoLists(lists[0], lists[1])
        i = 2
        while i < len(lists):
            head1 = lists[i]
            i += 1
            newHead = mergeTwoLists(head1, newHead)
        return newHead
