# 作者 ljc
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。
# 思路 使用堆栈 当遇到'('时进行入栈操作，当遇到')'时进行出栈操作
# 最后结果如果栈是空则是一个有效 否则是无效的
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')': '(',
                '}': '{',
                ']': '['}
        st = []
        for c in s:
            if c in dict and st[-1]==dict[c]:
                st.pop()
            else:
                st.append(c)
        return  not st
solution = Solution()
print(solution.isValid())
