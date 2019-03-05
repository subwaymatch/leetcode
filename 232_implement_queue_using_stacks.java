class MyQueue {
    private Stack<Integer> addStack; 
    private Stack<Integer> reversedStack; 

    /** Initialize your data structure here. */
    public MyQueue() {
        addStack = new Stack<Integer>(); 
        reversedStack = new Stack<Integer>(); 
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        addStack.push(x); 
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (reversedStack.empty()) copyStack(); 
        
        return reversedStack.pop(); 
    }
    
    /** Get the front element. */
    public int peek() {
        if (reversedStack.empty()) copyStack(); 
        
        return reversedStack.peek(); 
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return addStack.empty() && reversedStack.empty(); 
    }
    
    private void copyStack() {
        while (!addStack.empty()) {
            reversedStack.push(addStack.pop()); 
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
