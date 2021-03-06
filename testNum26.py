# 作者 ljc
#
# 给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
#
# 不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。
#
# 示例：
#
# 给定数组: nums = [1,1,2],
#
# 你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
# 不需要理会新的数组长度后面的元素
# 妈的居然少了一个条件 数组是已经升序排列好的
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail+1

solution = Solution()
print(solution.removeDuplicates([1, 2, 3, 3, 4, 4, 5]))
