# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        '''
        递归调用自身实现有序链表的合并，其时间复杂度为调用次数(m+n) * O(1) = O(m+n)
        递归调用的 'self.mergeTwoLists(line1.next, line2)' 意味着将line1.next节点和line2节点留给了下一次拼接
        这部分可以代指为line1“后面”的那部分东西
        '''
        line1 = list1
        line2 = list2
        if line1 is None:
            return line2
        if line2 is None:
            return line1
        if line1.val <= line2.val:
            line1.next = self.mergeTwoLists(line1.next, line2)
            return line1
        else:
            line2.next = self.mergeTwoLists(line1, line2.next)
            return line2
        

