#
# 给定一个正整数，返回它在Excel表中相对应的列名称。
#
# 示例：
#
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
# # 作者 ljc

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n-1)/26)+chr((n-1)%26+ord('A'))