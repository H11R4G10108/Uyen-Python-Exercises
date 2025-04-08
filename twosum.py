#Description: Given an array of integers nums and an integer target, return index of the two numbers such that they add up to target
#Input: an arrray and a target integer
#Output: the indexes of the two numbers

def TwoSum(nums, target):
    map={} #hash map to store the indices of the numbers
    for i in range(0, len(nums)):
        complement=target-nums[i]
        if complement not in map:
            map[nums[i]]=i
        else:
            return [map[complement], i]
print(TwoSum([2,7,11,15], 9)) # Output: [0,1]
print(TwoSum([3,2,4], 6)) # Output: [1,2]       
print(TwoSum([3,3], 6)) # Output: [0,1]