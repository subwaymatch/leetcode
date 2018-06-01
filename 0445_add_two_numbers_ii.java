/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private static int getListLength(ListNode head) {
        if (head == null) return 0; 
        
        int length = 1; 
        
        while (head.next != null) {
            length++; 
            head = head.next; 
        }
        
        return length; 
    }
    
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int l1Len = getListLength(l1); 
        int l2Len = getListLength(l2); 
        
        System.out.println("l1.length=" + l1Len + ", l2.length=" + l2Len); 
        
        ListNode longerListNode = (l1Len > l2Len) ? l1 : l2; 
        ListNode shorterListNode = (longerListNode == l1) ? l2 : l1;  
        
        int lenDiff = Math.abs(l1Len - l2Len); 
        int shorterLen = Math.min(l1Len, l2Len); 
        int longerLen = Math.max(l1Len, l2Len); 
        
        int[] digitAddedArr = new int[longerLen + 1]; 
        
        for (int i = 1; i <= lenDiff; i++) {
            digitAddedArr[i] = longerListNode.val; 
            longerListNode = longerListNode.next; 
        }
        
        for (int i = lenDiff + 1; i <= longerLen; i++) {
            digitAddedArr[i] = longerListNode.val + shorterListNode.val; 
            
            longerListNode = longerListNode.next; 
            shorterListNode = shorterListNode.next; 
        }
        
        for (int i = digitAddedArr.length - 1; i > 0; i--) {
            if (digitAddedArr[i] >= 10) {
                digitAddedArr[i - 1] += 1; 
                digitAddedArr[i] -= 10; 
            }
        }
        
        int beginIndex = -1; 
        
        for (int i = 0; i < digitAddedArr.length; i++) {
            if (digitAddedArr[i] != 0) {
                beginIndex = i; 
                break; 
            }
        }
        
        if (beginIndex == -1) return new ListNode(0); 
        
        ListNode head = new ListNode(digitAddedArr[beginIndex]); 
        ListNode currentNode = head; 
        
        for (int i = beginIndex + 1; i < digitAddedArr.length; i++) {
            currentNode.next = new ListNode(digitAddedArr[i]); 
            currentNode = currentNode.next; 
        }
                
        return head;  
    }
}
