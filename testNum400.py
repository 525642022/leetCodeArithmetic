# 作者 ljc
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32为整形范围内 ( n < 231)。
#
# 示例 1:
#
# 输入:
# 3
#
# 输出:
# 3
# 示例 2:
#
# 输入:
# 11
#
# 输出:
# 0
#
# 说明:
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n -= 1
        for digits in range(1,11):
            first = 10**(digits-1)
            if n < 9 * first * digits:
                print(str(first+n/digits))
                return int(str(first+n/digits)[n%digits])
            n -= 9*first*digits

solution = Solution();
print(solution.findNthDigit(10))
