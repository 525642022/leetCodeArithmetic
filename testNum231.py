# 作者 ljc

# 给定一个整数，写一个函数来判断它是否是2的幂。

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)
