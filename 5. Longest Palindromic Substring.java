class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }
        
        int start_index = 0;
        int end_index = 0;
        
        for (int i = 0; i < s.length(); i++) {
            //consider both cases of even and odd
            int len_odd = this.fromMiddleFindLength(s, i, i);
            int len_even = this.fromMiddleFindLength(s, i, i+1);
            int len = Math.max(len_odd,len_even);
            
            if (len > end_index - start_index) {
                start_index = i - ((len - 1) / 2);
                end_index = i + len / 2;
            }
        }
       
        
        return s.substring(start_index, end_index+1);
    }
    
    public int fromMiddleFindLength(String given, int left, int right) {
        if (given == null || left > right) {
            return 0;
        }
        
        while (left >= 0 && right < given.length() && given.charAt(left) == given.charAt(right)) {
            left--;
            right++;
        }
        
        return right - left - 1;
    }
}
