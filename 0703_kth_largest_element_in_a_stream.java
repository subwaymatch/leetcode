class KthLargest {
    private final int k;
    private final PriorityQueue<Integer> pq; 
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>(k); 
        
        for (int num : nums) {
            add(num); 
        }
    }
    
    public int add(int val) {
        pq.add(val);
        
        if (pq.size() > k) {
            pq.poll(); 
        }
        
        return pq.peek(); 
    }
}
