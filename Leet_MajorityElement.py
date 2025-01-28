if __name__ == '__main__':
    # def majorityElement(self, nums: list[int]) -> int:
    nums = [2,2,1,1,1,2,2,1]
    dictCount = {}
    # listLength = 
    
    for ele in nums:
        if ele in dictCount:
            dictCount[ele] += 1
        else:
            dictCount[ele] = 1
    
    print(dictCount)
    
    for k,v in dictCount.items():
        if v >= (len(nums)/2):
            print(k)

    