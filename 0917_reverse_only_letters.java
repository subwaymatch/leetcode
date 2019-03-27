class Solution {
    public boolean isLetter(char c) {
        return ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'));
    }
    
    public String reverseOnlyLetters(String S) {
        int leftPointer = 0; 
        int rightPointer = S.length() - 1; 
        
        char[] reversedS  = S.toCharArray(); 
        
        while (leftPointer < rightPointer) {
            char leftChar = S.charAt(leftPointer); 
            char rightChar = S.charAt(rightPointer); 
            
            if (!isLetter(leftChar)) {
                leftPointer++; 
                continue; 
            }
            
            if (!isLetter(rightChar)) { 
                rightPointer--; 
                continue; 
            }
            
            reversedS[leftPointer] = rightChar; 
            reversedS[rightPointer] = leftChar; 
            leftPointer++;
            rightPointer--; 
        }
        
        return new String(reversedS);
    }
}
