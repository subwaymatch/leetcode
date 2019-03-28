class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null; 
        else if (lists.length == 1) return lists[0];
        else if (lists.length == 2) return mergeTwoLists(lists[0], lists[1]); 
        else {
            ListNode[] a = Arrays.copyOfRange(lists, 0, (lists.length + 1) / 2);
            ListNode[] b = Arrays.copyOfRange(lists, (lists.length + 1) / 2, lists.length); 

            return mergeTwoLists(mergeKLists(a), mergeKLists(b));   
        }
    }
    
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode currNode = dummy; 
        
        ListNode n1ptr = list1; 
        ListNode n2ptr = list2; 
        
        while (n1ptr != null || n2ptr != null) {
            if (n2ptr == null || (n1ptr != null && n1ptr.val < n2ptr.val)) {
                currNode.next = n1ptr; 
                currNode = n1ptr; 
                n1ptr = n1ptr.next;
            }
            else {
                currNode.next = n2ptr;
                currNode = n2ptr;
                n2ptr = n2ptr.next; 
            }
        }
        
        return dummy.next; 
    }
}
