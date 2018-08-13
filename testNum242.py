# 作者 ljc

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
#
# 例如，
# s = "anagram"，t = "nagaram"，返回 true
# s = "rat"，t = "car"，返回 false
#
# 注意:
# 假定字符串只包含小写字母。
#
# 提升难度:
# 输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)
        dic1, dic2 = {},{}
        for item in s:
            dic1[item] = dic1.get(item, 0)+1
        for item in dic2:
            dic2[item] = dic2.get(item, 0)+1
        return dic1 == dic2