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
    public boolean isPalindrome(ListNode head) {
        if (head == null) return true;
        ListNode slow = head;
        ListNode fast = head;
        
        // slow now is the end of first half
        // fast.next != null ensures slow stops at the middle point in odd lists
        // fast.next.next != null ensures slow stops at the end of left half in even                lists
        while (fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        
        //reverse
        ListNode prev = null;
        // this ensures that the middle node is ignored for comparison
        slow = slow.next;
        while (slow != null){
            ListNode hold = slow.next;
            slow.next = prev;
            prev = slow;
            slow = hold;
        }
        
        //compare
        ListNode temp = head;
        boolean isP = true;
        while (prev != null){
            if (temp.val != prev.val){
                isP = false;
                break;
            }
            prev = prev.next;
            temp = temp.next;
        }
        return isP;
    }
        

}
