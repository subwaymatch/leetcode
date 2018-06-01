class Solution {
    private class Pair {
        public Character c; 
        public Integer count; 
        
        public Pair(char c, int count) {
            this.c = c; 
            this.count = count; 
        }
    }
    
    public String frequencySort(String s) {
        Map<Character, Integer> countMap = new HashMap<Character, Integer>(); 
        List<Pair> countList = new ArrayList<Pair>(); 
        char[] chars = s.toCharArray(); 
        
        for (char c : chars) {
            if (countMap.containsKey(c)) {
                countMap.put(c, countMap.get(c) + 1); 
            }
            else {
                countMap.put(c, 1); 
            }
        }
        
        for (Map.Entry<Character, Integer> entry : countMap.entrySet()) {
            Pair newPair = new Pair(entry.getKey(), entry.getValue()); 
            countList.add(newPair); 
        }
        
        countList.sort((o1, o2)->o2.count.compareTo(o1.count)); 
        
        char[] rearrangedChars = new char[s.length()]; 
        int charIndex = 0; 
        
        for (Pair p : countList) {
            for (int i = 0; i < p.count; i++) {
                rearrangedChars[charIndex++] = p.c; 
            }
        }
        
        return new String(rearrangedChars); 
    }
}
