class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        #edge case: one row or rows greater than s length
        if numRows == 1 or numRows >= len(s):
            return s
        
        direction = -1
        row = 0
        res = [[] for i in xrange(numRows)]
        
        #iterate and fill array
        for c in s:
            res[row].append(c)
            
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction
            
        for i in xrange(len(res)):
            # if there are 3 rows, then len(res) will give 3
            #join function takes all items in iterable and joins into one string
            res[i] = ''.join(res[i])
        return ''.join(res)
