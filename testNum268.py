# 作者 ljc
# 给出一个包含
# 0, 1, 2, ..., n
# 中
# n
# 个数的序列，找出
# 0..n
# 中没有出现在序列中的那个数。
#
# 案例
# 1
#
# 输入: [3, 0, 1]
# 输出: 2
#
# 案例
# 2
#
# 输入: [9, 6, 4, 2, 3, 5, 7, 0, 1]
# 输出: 8
#
# 注意事项:
# 您的算法应该以线性复杂度运行。你能否仅使用恒定的额外空间复杂度来实现它？
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
