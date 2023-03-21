#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """_summary_
        统计链表长度 length，用于通过判断 intv < length 判定是否完成排序；
        额外声明一个节点 res，作为头部后面接整个链表，用于：
        intv *= 2 即切换到下一轮合并时，可通过 res.next 找到链表头部 h；
        执行排序合并时，需要一个辅助节点作为头部，而 res 则作为链表头部排序合并时的辅助头部 pre；后面的合并排序可以将上次合并排序的尾部 tail 用做辅助节点。
        在每轮 intv 下的合并流程：
        根据 intv 找到合并单元 1 和单元 2 的头部 h1, h2。由于链表长度可能不是 2^n，需要考虑边界条件：
        在找 h2 过程中，如果链表剩余元素个数少于 intv，则无需合并环节，直接 break，执行下一轮合并；
        若 h2 存在，但以 h2 为头部的剩余元素个数少于 intv，也执行合并环节，h2 单元的长度为 c2 = intv - i。
        合并长度为 c1, c2 的 h1, h2 链表，其中：
        合并完后，需要修改新的合并单元的尾部 pre 指针指向下一个合并单元头部 h。（在寻找 h1, h2 环节中，h指针已经被移动到下一个单元头部）
        合并单元尾部同时也作为下次合并的辅助头部 pre。
        当 h == None，代表此轮 intv 合并完成，跳出。
        每轮合并完成后将单元长度 ×2，切换到下轮合并：intv *= 2。
        https://leetcode.cn/problems/sort-list/solutions/13728/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
        Args:
            head (ListNode): _description_

        Returns:
            ListNode: _description_
        """
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
    
    def sortList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """_summary_
        冒泡排序进行。
        25/30 cases passed (N/A)
        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        if not head:
            return head
        head_before=ListNode(val=-1,next=head) 
        now=head
        len=0
        while now.next:
            len+=1
            now=now.next
        for i in range(len):
            num=len-i-1
            p=head_before.next
            q=p.next
            tail=head_before
            for i in range(num+1):
                if p.val > q.val:
                    p.next=q.next
                    q.next=p
                    tail.next=q
                
                tail=tail.next
                p=tail.next
                q=p.next
        return head_before.next
# @lc code=end

