# 作者 ljc
# 将包含 n 个元素的数组向右旋转 k 步。
#
# 例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。
#
# 注意:
#
# 尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。
#
# [显示提示]
#
# 提示:
#
# 要求空间复杂度为 O(1)
#
# 关联的问题: 反转字符串中的单词 II
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]