class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        BRUTE FORCE SOLUTION
        """
        # print(nums)
        arr_len = len(nums)
        # print(arr_len)
        while(k>arr_len):
            k%=arr_len
        
        print(f"Initial K is: {k}")
        while(k>0):
            x, y = 0, arr_len-1
            for j in range(arr_len-1):
                nums[x], nums[y] = nums[y], nums[x]
                print(nums[x], nums[y])
                x+=1
            
            k-=1
            print(f"K is: {k}")
        
        print(nums)

        
sol = Solution()

input1 = [1,2,3,4,5,6,7]
# input1 = [-1,-100,2,99]
# 7,2,3,4,5,6,1
# 7,1,3,4,5,6,2
# 7,1,2,4,5,6,3
# 7,1,2,3,5,6,4
# 7,1,2,3,4,6,5
# 7,1,2,3,4,5,6

# 6,1,2,3,4,5,7
# 6,7,2,3,4,5,1
# 6,7,1,3,4,5,2
# 6,7,1,2,4,5,3
# 6,7,1,2,3,5,4
# 6,7,1,2,3,4,5

sol.rotate(input1, 3)