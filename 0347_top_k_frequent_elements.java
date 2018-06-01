public class Solution {
    class ElementCount {
        int element; 
        int count; 
        
        public ElementCount(int element, int count) {
            this.element = element; 
            this.count = count; 
        }
    }
    
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<ElementCount> countList = new ArrayList<ElementCount>(); 
        Map<Integer, Integer> countMap = new HashMap<Integer, Integer>(); 
        List<Integer> topKList = new ArrayList<Integer>(); 
        
        for (int num : nums) {
            if (countMap.containsKey(num)) {
                countMap.put(num, countMap.get(num) + 1); 
            }
            
            else {
                countMap.put(num, 1); 
            }
        }
        
        Iterator it = countMap.entrySet().iterator(); 
        
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next(); 
            
            countList.add(new ElementCount((int) pair.getKey(), (int) pair.getValue())); 
        }
        
        Collections.sort(countList, new Comparator<ElementCount>() {
            public int compare(ElementCount o1, ElementCount o2) {
                return o2.count - o1.count; 
            }
        });
        
        for (int i = 0; i < k; i++) {
            ElementCount elCount = countList.get(i); 
            
            topKList.add(elCount.element); 
            System.out.println(elCount.element + " occured " + elCount.count + " times."); 
        }
        
        return topKList; 
    }
}
