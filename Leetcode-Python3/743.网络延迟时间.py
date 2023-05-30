#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
# Dijkstra

import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s,e,c in times:
            graph[s][e] = c

        seen = [-1]*n
        Q = [[0, k]] # 初始位置

        heapq.heapify(Q)

        while Q:
            cost, cur_pos = heapq.heappop(Q)
            if seen[cur_pos-1] == -1:
                seen[cur_pos-1] = cost
                for next_pos in graph[cur_pos]:
                    heapq.heappush(Q, [cost + graph[cur_pos][next_pos], next_pos])

        if -1 in seen:
            return -1
        return max(seen)

# @lc code=end

