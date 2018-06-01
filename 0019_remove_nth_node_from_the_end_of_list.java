/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode virtualHead = new ListNode(0); 
        virtualHead.next = head; 
        
        System.out.println("head.val=" + head.val); 
        System.out.println("n=" + n); 
        
        ListNode nodeBeforeDeletion = virtualHead; 
        ListNode currentNode = virtualHead; 
        
        for (int i = 0; i < n; i++) {
            currentNode = currentNode.next; 
        }
        
        while (currentNode.next != null) {
            currentNode = currentNode.next; 
            nodeBeforeDeletion = nodeBeforeDeletion.next; 
        }
        
        nodeBeforeDeletion.next = nodeBeforeDeletion.next.next; 
        
        System.out.println("nodeBeforeDeletion.val=" + nodeBeforeDeletion.val); 
        System.out.println("currentNode.val=" + currentNode.val); 
        
        return virtualHead.next; 
    }
}
