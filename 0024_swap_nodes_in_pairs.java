/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode currentNode = new ListNode(0); 
        ListNode originalHead = currentNode; 
        
        currentNode.next = head;
        
        while (currentNode.next != null && currentNode.next.next != null) {
            ListNode leftSwap = currentNode.next; 
            ListNode rightSwap = currentNode.next.next; 

            ListNode followingNode = rightSwap.next; 

            currentNode.next = rightSwap; 
            rightSwap.next = leftSwap; 
            leftSwap.next = followingNode; 
            
            currentNode = leftSwap; 
        }
        
        return originalHead.next; 
    }
}
