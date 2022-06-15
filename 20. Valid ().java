class Solution {
    public boolean isValid(String s) {
        
        //a valid string can only be even in length
        if (s.length() % 2 != 0) {
            return false;
        }
        
        Stack<Character> stack = new Stack();
        
        
        //if a matching pair exists, the pushed char should be popped
        for (char c: s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
                //peek checks the object on top of the stack
                stack.pop();
            } else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
                //peek checks the object on top of the stack
                stack.pop();
            } else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
                //peek checks the object on top of the stack
                stack.pop();
            }
        }
        
        //stack should be empty
        return stack.isEmpty();
        
        
    }
}
