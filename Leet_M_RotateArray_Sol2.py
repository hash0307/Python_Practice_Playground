class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        arr_len = len(nums)
        # print(arr_len)
        while(k>arr_len):
            k%=arr_len
        print(f"Initial K is: {k}")
    
        self.arrReverse(nums, 0, arr_len-k-1)
        self.arrReverse(nums, arr_len-k, arr_len-1)
        self.arrReverse(nums, 0, arr_len-1)
        # print(f"K is: {k}")
    # print(nums)
    
    def arrReverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        print(nums)


        
sol = Solution()

input1 = [1,2,3,4,5,6,7]
# input1 = [-1,-100,2,99]
# 1,2,3,4 5,6,7
# 4,3,2,1 5,6,7 Reverse 1st sub-array
# 4,3,2,1 7,6,5 Reverse 2nd sub-array
# 5,6,7,1,2,3,4 Reverse 1+2nd array


sol.rotate(input1, 54944)