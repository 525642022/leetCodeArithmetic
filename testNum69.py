# 作者 ljc
# 使用牛顿算法
# 牛顿算法介绍

# 链接：https://www.zhihu.com/question/25913884/answer/31779629


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r