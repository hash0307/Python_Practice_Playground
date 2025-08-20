class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in numMap:
        #         return [numMap[complement], i]
        #     numMap[nums[i]] = i
        # return []
    
        # Use enumerate to get both index and value
        for i, val in enumerate(nums):
            complement = target - val
            # Check if the complement exists in the map
            if complement in numMap:
                return [numMap[complement], i]
            else:
                # Store the index of the current number
                numMap[nums[i]] = i
        return []

print(Solution().twoSum([9,6,2,3,7,5,0,1], 8))