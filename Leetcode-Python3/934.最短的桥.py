#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
        n, m = len(grid), len(grid[0])
        # 先随便找一个岛
        st = list()
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1:
                    st.append((i, j))
                    grid[i][j] = -1
                    break
            if st: break
        # 扩展全岛入队
        p = 0
        while p < len(st):
            i, j = st[p]
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                    continue
                st.append((x, y))
                grid[x][y] = -1
            p += 1
        # 多源 BFS 找最短路
        for step in range(n * m + 1):
            st2 = list()
            for i, j in st:
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == -1:
                        continue
                    if grid[x][y] == 1:
                        return step
                    st2.append((x, y))
                    grid[x][y] = -1
            st = st2
        return -1

