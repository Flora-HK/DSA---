# 由于使用一个列表判断数组是否为回文较简单，所以第一步是需要将所给链表转换成列表
# 在python中，链表和列表的转换非常简单，只需要使用while循环遍历链表即可

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

