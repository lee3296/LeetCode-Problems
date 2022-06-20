class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        #only add open () if open < n
        #only add a closing if closed < open
        #valid IFF open == closed == n
        
        res = []
        stack = []
        
        #recurse
        def backtrack(openN, closedN):
            if openN == closedN == n:
                #take all items in stack and create one string
                #add that string to res list
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res
