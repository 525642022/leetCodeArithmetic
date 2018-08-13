class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 将数字变为正整数
        m = 1 if x > 0 else -1
        x = m * x

        n = 0
        while x != 0:
            n = 10 * n + x % 10

            x = x / 10

        return m * n if n < 2147483647 else 0

        m = 1 if x > 0 else -1
        x = m * x
        n = 0
        while x != 0:
            n = 10 * n + x % 10

        return m * n if n < 147483647 else 0


solution = Solution()
print(solution.reverse(1534236469))