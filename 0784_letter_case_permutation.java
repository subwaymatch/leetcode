class Solution {
    public List<String> letterCasePermutation(String S) {
        if (S.equals("")) {
            return Arrays.asList(new String[] { "" });
        }
        return buildPermutations(S, 0, new ArrayList<String>()); 
    }
    
    public List<String> buildPermutations(String S, int idx, List<String> currentList) {
        if (idx == S.length())
            return currentList;
    
        List<String> newList = new ArrayList<String>(); 
        
        if (S.charAt(idx) >= 'A' && S.charAt(idx) <= 'z') {
            char lower = S.charAt(idx);
            char upper = S.charAt(idx);
            
            if (S.charAt(idx) <= 'Z') {
                lower += 'a' - 'A';    
            }
            else {
                upper += 'A' - 'a';
            }
            
            if (currentList.isEmpty()) {
                newList.add(((Character)lower).toString()); 
                newList.add(((Character)upper).toString()); 
            }
            
            else {
                for (String s : currentList) {
                    newList.add(s + lower);
                    newList.add(s + upper);
                }
            }
        }
        
        else {
            if (currentList.isEmpty()) {
                newList.add("" + S.charAt(idx)); 
            }
            
            else {
                for (String s: currentList) {

                    newList.add(s + S.charAt(idx)); 
                }
            }
        }
        
        return buildPermutations(S, idx + 1, newList);
    }
}
