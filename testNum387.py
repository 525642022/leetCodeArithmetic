# 作者 ljc

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set(s)
        return min([s.index(l) for l in chars if s.count(l) == 1]or[-1])