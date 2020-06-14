# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        pair = [head, head.next]
        if pair[1].next is None:
            pair[0].next = None
            pair[1].next = pair[0]
            return pair[1]
        else:
            pair[0].next = self.swapPairs(pair[1].next)
            pair[1].next = pair[0]
            return pair[1]


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(3, l1)
    l3 = ListNode(2, l2)
    l4 = ListNode(1, l3)
    ans = Solution().swapPairs(l4)
    print(ans)
