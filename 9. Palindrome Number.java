class Solution {
    public boolean isPalindrome(int x) {
        if (x == 0) return true;
        
        int reversed = 0;
        
        reversed = this.reverseNumber(x);
        
        if (reversed == x) {
            return true;
        }
        
        return false;
    }
    
    public int reverseNumber(int input) {
        int reversedNum = 0;
        int input_long = input;

        while (input_long != 0) {
            reversedNum = reversedNum * 10 + input_long % 10;
            input_long = input_long / 10;
        }
        
        return reversedNum;
    }
}
