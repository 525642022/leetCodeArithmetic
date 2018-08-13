# 作者 ljc
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使 nums [i] = nums [j]，并且 i 和 j 的绝对差值最大为 k。
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False