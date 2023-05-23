#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 方法一：哈希表排序
        # 注意：字典序是正序，出现次数为倒序
        return [w for w,_ in sorted(Counter(words).items(),key=lambda x:(-x[1],x[0]))[:k]]

# @lc code=end
