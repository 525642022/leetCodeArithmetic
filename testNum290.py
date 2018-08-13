# 作者 ljc

# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循这种模式。
#
# 这里的 遵循 指完全匹配，例如在pattern里的每个字母和字符串 str 中的每个非空单词存在双向单映射关系。
#
# 例如：
#
# pattern = "abba", str = "dog cat cat dog", 返回true
# pattern = "abba", str = "dog cat cat fish", 返回false.
# pattern = "aaaa", str = "dog cat cat dog" , 返回false.
# pattern = "abba", str = "dog dog dog dog" , 返回false.
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分开的小写单词
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return map(s.find,s) ==  map(t.index,t)
