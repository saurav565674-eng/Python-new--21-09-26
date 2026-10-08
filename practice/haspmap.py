def twoSum(nums: list[int], target: int) -> list[int]:
    seen ={}
    for i,num in enumerate(nums):
        n = target - num
        if n in seen:
            return[seen[n],i]
        seen[num]=i
    return[]
