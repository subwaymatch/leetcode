public class Solution {
    public String convertToTitle(int n) {
        Stack<Integer> chars = new Stack<Integer>(); 
        
        int remainder = 0; 
        char c; 
        String columnTitle = ""; 
        boolean breakFlag = false; 
        
        while (n > 0) {
            if (n <= 26) breakFlag = true; 
            
            remainder = (n - 1) % 26 + 1; 
            
            chars.push(remainder); 
            
            n = (n - remainder) / 26; 
            
            if (breakFlag) break; 
        }
        
        while (!chars.empty()) {
            c = (char)((int)'A' - 1 + chars.pop()); 
            columnTitle += c;    
        }
        
        return columnTitle; 
    }
}
