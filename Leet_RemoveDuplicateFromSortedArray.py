if __name__ == '__main__':
    # nums=[0,0,1,1,1,2,2,3,3,4]
    nums=[-1,0,0,0,0,3,3]

    set_nums = sorted(set(nums))
    k = len(set_nums)
    print(k)

    for i in range(len(set_nums)):
        nums.insert(i,set_nums[i])
    
    print(nums)


# removeDuplicates(nums)
    