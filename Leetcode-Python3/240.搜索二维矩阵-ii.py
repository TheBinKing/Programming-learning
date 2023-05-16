#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start

class Solution:
    def searchMatrix0(self, M: List[List[int]], T: int) -> bool:
        '''
        装逼的最短代码
        '''
        return T in chain(*M)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Python3+指针
        '''
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1

        while 0<=i<m and 0<=j<n and matrix[i][j] != target:
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                
        return 0<=i<m and 0<=j<n and matrix[i][j] == target

# @lc code=end

