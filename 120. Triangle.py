class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        numRows = len(triangle)
        sum_total = 0
        index = 0
        left = 0
        right = 0
        
        
        if numRows == 1:
            return triangle[0][0]
        
        for i in xrange(numRows):
            if i == 0:
                sum_total = triangle[0][0]
            else:
                left = sum_total + triangle[i][index]
                right = sum_total + triangle[i][index+1]
                
                if left < right:
                    sum_total += triangle[i][index]
                else:
                    sum_total += triangle[i][index+1]
                    index += 1
                    
        return sum_total
