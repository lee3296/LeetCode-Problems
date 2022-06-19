class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        #enumerate through every element in list
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                #if past first index and a is equal to previous in sort
                continue
            
            #pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                        
        return res     
