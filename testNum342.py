# 作者 ljc

# 给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。
#
# 示例:
# 当 num = 16 时 ，返回 true 。 当 num = 5时，返回 false。
#
# 问题进阶：你能不使用循环/递归来解决这个问题吗？
#
# 致谢:
# 特别感谢 @yukuairoy 添加这个问题并创建所有测试用例。
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        test = 1
        while test < num:
            test = test<<2
        return test == num