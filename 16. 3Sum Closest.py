class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        res = 0
        previous = 0
        
        if target >= 0:
            previous = 10 ** 4
        else:
            previous = -1 * 10 ** 4
        
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                #if past first index and a is equal to previous in sort
                continue
            
            #pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if target == threeSum:
                    return target
                
                if target < 0:
                    if target - threeSum > previous:
                        res = threeSum
                        previous = target - threeSum
                else:
                    if target - threeSum < previous:
                        res = threeSum
                        previous = target - threeSum
                
                l += 1
        
        return res
