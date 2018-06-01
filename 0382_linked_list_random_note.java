/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    ListNode head; 
    
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.head = head; 
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        if (head.next == null) return head.val; 
        
        ListNode currentNode = head; 
        int length = 1; 
        int currentVal = currentNode.val; 
        
        while (currentNode.next != null) {
            currentNode = currentNode.next; 
            length++; 
            
            if (Math.random() < ((double) 1 / (double) length)) {
                currentVal = currentNode.val; 
            }
        }
        
        return currentVal; 
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
