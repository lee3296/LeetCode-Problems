class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                  ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                  ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                  ["M", 1000]]
        res = ""
        
        
        #Go through list in reverse order since largest is first
        for sym, val in reversed(symList):
            #double slash makes the answer an int not a float
            if num // val:
                count = num // val
                res += (sym * count) #take sym string and make count copies
                num = num % val
                
        return res
