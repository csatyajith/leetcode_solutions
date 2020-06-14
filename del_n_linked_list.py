# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        iternode = head
        if head.next is None:
            return None
        for _ in range(n):
            iternode = iternode.next
        saved_node = head
        if iternode is None:
            return saved_node.next
        while iternode.next is not None:
            saved_node = saved_node.next
            iternode = iternode.next
        saved_node.next = saved_node.next.next
        return head


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(4, l1)
    l3 = ListNode(3, l2)
    l4 = ListNode(2, l3)
    l5 = ListNode(1, l4)
    sol = Solution()
    l5 = sol.removeNthFromEnd(l5, 2)
    print(l5)
