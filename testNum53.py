# 作者 ljc
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    # 给定一个序列（至少含有
    # 1
    # 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。
    #
    # 例如，给定序列[-2, 1, -3, 4, -1, 2, 1, -5, 4]，
    # 连续子序列[4, -1, 2, 1]
    # 的和最大，为
    # 6。
    #
    #
    #
    # 扩展练习:
    #
    # 若你已实现复杂度为
    # O(n)
    # 的解法，尝试使用更为精妙的分治法求解。
    # 扩展暂时没有完成 等第二轮完成
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
