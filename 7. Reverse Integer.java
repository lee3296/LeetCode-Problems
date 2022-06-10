class Solution {
    public int reverse(int x) {
        if (x == 0) return 0;
        
        int if_negative = 0;
        int reverse_num = 0;
        
        if (x < 0) {
            if_negative = x * -1;
            
            while (if_negative != 0) {
                reverse_num = reverse_num + if_negative % 10;
                //reverse_num = reverse_num * 10;
                if_negative = if_negative / 10;
                
                if (if_negative == 0) {
                    break;
                }
                else {
                    reverse_num = reverse_num * 10;
                }
            }
            
            reverse_num = reverse_num * -1;
            return reverse_num;
        }
        
        while (x != 0) {
            reverse_num = reverse_num + x % 10;
            //reverse_num = reverse_num * 10;
            x = x / 10;
            
            if (x == 0) {
                break;
            }
            else {
                reverse_num = reverse_num * 10;
            }
        }
        
        return reverse_num;
    }
}
