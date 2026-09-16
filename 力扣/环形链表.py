# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    ''' 
    使用哈希表来实现，将遍历过的元素加入哈希表，重复即为环形链表
    时间复杂度O(n)，空间复杂度O(n)
    在python中，哈希表可以通过set和dict来实现
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        使用快慢指针完成，快指针每次移动两步，慢指针每次移动一步
        当快指针和慢指针相遇重合的时候，说明有环
        此时，快指针已经走了a + n * (b + c) + b 步，慢指针走了a + b步
        化简一下，快指针fast走了 a+(n+1)b+nc 步，慢指针走了a+b步
        又因为，快指针fast走过的距离都为慢指针slow的两倍，所以有：
        a+(n+1)b+nc = 2(a+b)
        化简得：a = c + (n-1)(b+c)
        此时，将快指针重新指向head，然后快慢指针每次都移动一步，当快指针和慢指针相遇时，即为环的入口

        '''
        fast = head
        slow = head
        while fast:
            slow = slow.next
            if (fast.next is None):
                return None
            fast = fast.next.next
            if (fast == slow):
                ptr = head
                while(ptr != slow):
                    ptr = ptr.next
                    slow = slow.next
                return ptr
            return None




