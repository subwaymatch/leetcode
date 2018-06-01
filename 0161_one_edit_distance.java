class Solution {
    public boolean isOneEditDistance(String s, String t) {
        System.out.println("Math.abs(s.length() - t.length())=" + Math.abs(s.length() - t.length())); 
        
        if (s.equals(t) || (Math.abs(s.length() - t.length()) > 1)) {
            return false; 
        }
        
        if (s.length() == t.length()) {
            boolean foundDifferentChar = false; 
            
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) != t.charAt(i)) {
                    if (foundDifferentChar == true) return false; 
                    else foundDifferentChar = true; 
                }
            }
            
            if (foundDifferentChar == true) return true; 
        }
        
        else {
            if (s.length() + t.length() == 1) return true; 
            
            String shorterStr = (s.length() < t.length()) ? s : t; 
            String longerStr = (s.length() > t.length()) ? s : t; 
            
            System.out.println("shorterStr=" + shorterStr + ", longerStr=" + longerStr); 
            
            boolean foundDifferentChar = false; 
            int longerStrIndex = 0; 
            
            for (int i = 0; i < shorterStr.length(); i++) {
                longerStrIndex = i + (foundDifferentChar ? 1 : 0); 
                
                if (shorterStr.charAt(i) != longerStr.charAt(longerStrIndex)) {
                    if (foundDifferentChar == true) return false; 
                    else { 
                        foundDifferentChar = true; 
                        i--; 
                    }
                }
            }
            
            return true; 
        }
        
        return false; 
    }
}
