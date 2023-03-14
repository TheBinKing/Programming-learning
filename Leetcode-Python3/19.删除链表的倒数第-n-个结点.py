#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """_summary_
        首先从头节点开始对链表进行一次遍历，得到链表的长度L。
        随后再从头节点开始对链表进行一次遍历，当遍历到第 L−n+1个节点时，它就是我们需要删除的节点

        Args:
            head (Optional[ListNode]): _description_
            n (int): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next








# @lc code=end

