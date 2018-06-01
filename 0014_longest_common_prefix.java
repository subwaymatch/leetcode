public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return ""; 
        
        String refStr = strs[0]; 
        int prefixLength = 0; 
        
        for (int i = 0; i < refStr.length(); i++) {
            char c = refStr.charAt(i);  
            boolean isCommon = true; 
                
            for (int j = 1; j < strs.length; j++) {
                String str = strs[j]; 
                
                if ((str.length() <= i) || (c != str.charAt(i))) {
                    isCommon = false; 
                    break; 
                }                
            }
                    
            if (isCommon) {
                prefixLength++; 
            } else {
                break; 
            }
        }
        
        return refStr.substring(0, prefixLength);  
    }
}
