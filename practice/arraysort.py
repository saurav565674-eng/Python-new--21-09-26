def isSorted(nums :list[int]) ->bool:
    if len(nums)<=1:
        return True
    for i in range(1,len(nums)):
        if int(nums[i]) < int(nums[i-1]):
            return False
    return True
