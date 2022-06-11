class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1
        
        i = 0
        res = 0
        negative = 1
        
        #whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
            
        #plus or minus
        if i < len(s) and s[i] == '-':
            i += 1
            negative = -1
        elif i < len(s) and s[i] == '+':
            i += 1
            
        #check 0-9
        checker = set('0123456789')
        while i < len(s) and s[i] in checker:
            # move one over to make room for new digit
            res = res * 10 + int(s[i])
            i += 1
            
        #make number negative if it is
        res = res * negative;
        
        if max(res, MIN_INT) == MIN_INT:
            return MIN_INT
        elif max(res, MAX_INT) == res:
            return MAX_INT
        
        return res;
