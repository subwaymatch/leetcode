class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramsMap = new HashMap<String, List<String>>(); 
        List<List<String>> groupedAnagramsList = new ArrayList<List<String>>(); 
        
        for (String str : strs) {
            char[] charArr = str.toCharArray(); 
            Arrays.sort(charArr); 
            String sortedStr = new String(charArr); 
            
            if (anagramsMap.containsKey(sortedStr)) {
                anagramsMap.get(sortedStr).add(str); 
            }
            
            else {
                List<String> anagramsList = new ArrayList<String>(); 
                anagramsList.add(str); 
                
                anagramsMap.put(sortedStr, anagramsList); 
            }
        }
        
        return new ArrayList<List<String>>(anagramsMap.values()); 
    }
}
