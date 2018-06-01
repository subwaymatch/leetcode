/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    private void connectNodes(ListNode currentNode, ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return; 
        }
        
        else if (l1 != null && l2 == null) {
            currentNode.next = l1; 
            l1 = l1.next; 
        }
        
        else if (l1 == null && l2 != null) {
            currentNode.next = l2; 
            l2 = l2.next; 
        }
        
        else {
            if (l1.val < l2.val) {
                currentNode.next = l1; 
                l1 = l1.next; 
            } else {
                currentNode.next = l2; 
                l2 = l2.next; 
            }
        }
        
        connectNodes(currentNode.next, l1, l2); 
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0); 
        
        connectNodes(head, l1, l2);         
        
        return head.next; 
    }
}
