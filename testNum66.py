# 作者 ljc
# 这是一道比较逗比的题

# 给定一个非负整数组成的非空数组，给整数加一。
#
# 可以假设整数不包含任何前导零，除了数字0本身。
#
# 最高位数字存放在列表的首位。
# 就这描述还不给例子的是烦
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]
