class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
        # Used help from: https://www.youtube.com/watch?v=SKLu5FKsr3k
        
        #find max gap of horizontal cuts
        #then find max gap of vertical cuts
        #multiply them to get max area
        #Lines will always intersect
        #append 0 and max width or height to lists to account for those slices
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        #append 0 and max at beginning
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        max_h,max_w = 0, 0
        for i in range(1,len(horizontalCuts)):
            max_h = max(max_h, abs(horizontalCuts[i-1]-horizontalCuts[i]))
        for i in range(1,len(verticalCuts)):
            max_w = max(max_w, abs(verticalCuts[i-1]-verticalCuts[i]))
            
        return (max_h * max_w) % (10 ** 9 + 7)
