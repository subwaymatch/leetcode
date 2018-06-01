/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head; 
        
        ListNode virtualHead = new ListNode(0); 
        virtualHead.next = head; 
        
        ListNode currentNode = virtualHead; 
        Map<Integer, Boolean> valMap = new HashMap<Integer, Boolean>(); 
        
        while (currentNode.next != null) {
            if (!valMap.containsKey(currentNode.next.val)) {
                System.out.println(currentNode.next.val + " not found"); 
                valMap.put(currentNode.next.val, true); 
                currentNode = currentNode.next; 
            }
            else {
                System.out.println(currentNode.next.val + " found"); 
                currentNode.next = currentNode.next.next; 
            }
        }
        
        System.out.println(head.val); 
        
        return virtualHead.next; 
    }
}
