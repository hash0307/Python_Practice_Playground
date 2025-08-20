class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []

print(Solution().twoSum([9,6,2,3,7,5,0,1], 8))