/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((node1, node2) -> node1.val - node2.val); 
        
        for (ListNode node : lists) {
            if (node != null) {
                pq.add(node); 
            }
        }
        
        if (pq.isEmpty()) return null; 
        
        ListNode root = pq.poll();
        if (root.next != null) pq.add(root.next); 
        ListNode currNode = root; 
        
        while (!pq.isEmpty()) {
            // System.out.println(pq.peek().val);
            ListNode nextNode = pq.poll(); 
            
            currNode.next = nextNode; 
            currNode = nextNode; 
            
            if (nextNode.next != null) pq.add(nextNode.next); 
        }
        
        return root;
    }
}
