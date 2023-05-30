#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # 1.初始化队列及标记数组，存入起点
        q = deque((i, 1 << i, 0) for i in range(n)) # 三个属性分别为 idx, mask, dist；存入起点，起始距离0，标记
        vis = {(i, 1 << i) for i in range(n)} # 节点编号及当前状态
        
        # 开始搜索
        while q:
            u, mask, dist = q.popleft() # 弹出队头元素
            if mask == (1 << n) - 1: # 找到答案，返回结果
                return dist
            # 扩展
            for x in graph[u]:
                nextmask = mask | (1 << x)
                if (x, nextmask) not in vis:
                    q.append((x, nextmask, dist + 1))
                    vis.add((x, nextmask))
        
        return 0
