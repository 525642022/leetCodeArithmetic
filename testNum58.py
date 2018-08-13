# 作者 ljc
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        # myspit = s.split(" ")
        # for i in range(len(myspit)):
        #     if myspit[-(i + 1)] != '':
        #         return myspit[-(i + 1)]
        # return len(myspit[-1])
        return len(s.rstrip(' ').split(' ')[-1])


solution = Solution()
print(solution.lengthOfLastWord("a "))
