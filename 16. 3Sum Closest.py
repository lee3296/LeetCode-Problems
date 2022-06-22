class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #In java: Arrays.sort(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums) - 1]
        
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
                
                if threeSum > target:
                    r -= 1
                else:
                    l += 1
                
                #find absolute value comparison
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
        
        return res
