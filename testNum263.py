# 作者 ljc
# 编写程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因子 2, 3, 5 的正整数。例如， 6, 8 是丑数，而 14 不是，因为它包含了另外一个质因子 7。
#
# 注意：
#
# 1 也可以被当做丑数。
# 输入不会超过32位整数的范围
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2,3,5:
            while num % p == 0 < num:
                num /= p
            return num == 1