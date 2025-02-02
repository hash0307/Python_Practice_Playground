class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)-1):
            product=1
            for j in range(len(nums)-1):
                if(i!=j):
                    product*=nums[j]
                print(i, j, product)
            ans[i] = product
        
        return ans
        


sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)

# IP = [1,2,3,4]
# OP = [24,12,8,6]