#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle0(self, head: Optional[ListNode]) -> bool:
        
        pass
    def hasCycle0(self, head: Optional[ListNode]) -> bool:
        """
        快慢指针，一个快指针一个慢指针进行链表遍历，如果有环那么快指针会折回和慢指针相遇，如果没有还将会遇到尾巴的判空条件而中止。
        """
        if not head:
            return False
        fast=head
        slow=head
        while(fast.next and fast.next.next):
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
# @lc code=end

