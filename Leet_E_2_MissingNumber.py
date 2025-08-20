class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        return next(i for i in range(len(nums)+1) if i not in nums)
        #OR
        # return sum(range(len(nums)+1)) - sum(nums)

print(Solution().missingNumber([9,6,4,2,3,7,5,0,1]))