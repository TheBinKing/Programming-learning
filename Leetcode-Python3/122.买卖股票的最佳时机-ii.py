#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        wallet,day=0,len(prices)
        for i in range(1,day):
            temp=prices[i]-prices[i-1]
            if temp>0:
                wallet+=temp
        return wallet
# @lc code=end

