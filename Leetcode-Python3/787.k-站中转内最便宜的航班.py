#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#



# @lc code=start

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pre = [float("inf")] * n
        pre[src] = 0
        for _ in range(k + 1):
            cur = pre[:]
            for i, j, p in flights:
                if pre[i] + p < cur[j]:
                    cur[j] = pre[i] + p
            pre = cur[:]
        return pre[dst] if pre[dst] < float("inf") else -1


