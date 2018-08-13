# 作者 ljc
# 编写一个函数来查找字符串数组中最长的公共前缀字符串。
# 使用zip函数 使用自拍是元素与最短的列表元素相同你 ...
# pyhton reduce 学习
from functools import reduce
class Solution(object):
    def lcp(self,str1,str2):
        i = 0
        while(i < len(str1) and i<len(str2)):
            if str1[i] == str2 [i]:
                i = i+1
            else:
                break
        print(i)
        return str1[:i]
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        #the first 方法
        # if not strs:
        #     return ''
        # print(min(strs))
        # for i, res in enumerate(zip(*strs)):
        #     print(len(set(res)), set(res), i)
        #     if len(set(res)) > 1:
        #         return strs[0][:i]
        # return min(strs)
        # the second 方法
        if not strs:
            return ''
        else:
            return reduce(self.lcp,strs)





solution = Solution()
print(solution.longestCommonPrefix(['abc', 'ab','abcd']))
