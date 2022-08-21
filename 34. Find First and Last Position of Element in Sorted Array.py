class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if target == 0 or len(nums) == 0:
            return [-1, -1]
        
        first = 0
        last = 0
        numTracker = 0;
        res = []
        
        for i in range(len(nums)):
            if nums[i] > target:
                break
            
            if last == 0 and nums[i] == target:
                first = i
                numTracker += 1
                res.append(first)
                last = i
            elif nums[i] == target and last < i:
                last = i
                numTracker += 1
        
        #edge case, 0 last value
        if numTracker == 0:
            return [-1, -1]
        
        res.append(last)
        return res
