class MinStack {
    List<Integer> stack;
    List<Integer> min;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new ArrayList<Integer>();
        min = new ArrayList<Integer>(); 
    }
    
    public void push(int x) {
        stack.add(x); 
        
        int stackSize = stack.size(); 
        
        if (stackSize == 1) min.add(x); 
        else if (x < min.get(stackSize - 2)) min.add(x); 
        else min.add(min.get(stackSize - 2)); 
    }
    
    public void pop() {
        int stackSize = stack.size(); 
        
        if (stackSize > 0) {
            stack.remove(stackSize - 1); 
            min.remove(stackSize - 1); 
        }
    }
    
    public int top() {
        int stackSize = stack.size(); 
        
        if (stackSize > 0) return stack.get(stackSize - 1); 
        else return 0; 
    }
    
    public int getMin() {
        return min.get(min.size() - 1); 
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
