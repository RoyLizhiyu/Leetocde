/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode merged = new ListNode();
        ListNode result = merged;
        
        while (l1 != null && l2 != null){
            
            if (l1.val > l2.val){
                merged.next = l2;
                l2 = l2.next;
            }
            else{
                merged.next = l1;
                l1 = l1.next;
            }
            merged = merged.next;
        }
        
        if (l1 == null){
            merged.next = l2;
        }
        else{
            merged.next = l1;
        }
        
        
        return result.next;
        
    }
}
