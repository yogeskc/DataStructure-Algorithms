#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                sum = nums[i] + nums[j]
                if sum == target: 
                    return (nums[i],nums[j])
        return False

# The following solution has #BIG(O): n2  trying to optimize the solution
def twoSumOptimize(nums, target): 
    complementsDict = {}
    for i in range(len(nums)): 
        num = nums[i]
        complement = target - num 
        if num in complementsDict:
            return [nums[complementsDict[num]],nums[i]]
        else:
           
            complementsDict[complement] = i
            print(complementsDict)
    return False
       

 # 9 = 10-1 
    
nums=[1,23,4,9,6,4]
target = 10

print(twoSumOptimize(nums,target))
        