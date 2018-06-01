/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode virtualHeadNode = new ListNode(0); 
        virtualHeadNode.next = head; 
        
        ListNode currentNode = virtualHeadNode; 
        
        while (currentNode.next != null) {
            if (currentNode.next.val == val) {
                currentNode.next = currentNode.next.next; 
            }
            
            else {
                currentNode = currentNode.next; 
            }
        }
        
        return virtualHeadNode.next; 
    }
}
