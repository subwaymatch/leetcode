/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    private int getListLength(ListNode head) {
        if (head == null) return 0; 
        
        int len = 1; 
        ListNode currentNode = head; 
        
        while (currentNode.next != null) {
            len++; 
            currentNode = currentNode.next; 
        }
        
        return len; 
    }
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null; 
        
        int lenA = getListLength(headA); 
        int lenB = getListLength(headB); 
        int diff = Math.abs(lenA - lenB); 
        
        ListNode shorterListNode = (lenA < lenB) ? headA : headB; 
        ListNode longerListNode = (lenA < lenB) ? headB : headA; 
        
        for (int i = 0; i < diff; i++) {
            longerListNode = longerListNode.next; 
        }
        
        for (int i = 0; i < Math.min(lenA, lenB); i++) {
            if (shorterListNode == longerListNode) return shorterListNode; 
            else {
                shorterListNode = shorterListNode.next;
                longerListNode = longerListNode.next; 
            }
        }
        
        return null; 
    }
}
