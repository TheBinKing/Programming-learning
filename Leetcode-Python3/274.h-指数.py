#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """_summary_
        排序+线性搜索 首先将citations进行排序。
        再进行线性搜索，目标是找到一个最长区间使得区间中的每一个数大于等于区间长度，
        区间长度即为答案。注意对特殊情况citation全为0的处理
        

        Args:
            citations (List[int]): _description_

        Returns:
            int: _description_
        """
        citations.sort()
        n = len(citations)
        if n==0 or citations[-1]==0:
            return 0
        for i in range(n):
            if citations[i]>=n-i:
                return n-i 
        
    def hIndex0(self, citations: List[int]) -> int:
        citations.sort( reverse=True)
        for i in range(len(citations)):
            if citations[i]<=i+1:
                return citations[i]
        if citations[-1]>len(citations):
            return len(citations)
        return citations[-1]
        
        
        
        
# @lc code=end

