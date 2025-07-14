# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        number = 0
        curr = head
        while curr:
            number = (number<<1) | curr.val
            curr = curr.next
        return number