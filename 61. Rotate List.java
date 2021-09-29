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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null){
            return null;
        }
        if (head.next == null){
            return head;
        }
        int len = 1;
        ListNode old_tail = head;
        // find the tail
        while (old_tail.next != null){
            old_tail = old_tail.next;
            len++;
        }
        //close the list to a ring
        old_tail.next = head;
        
        ListNode new_tail = head;
        for (int i = 0; i < len- k % len -1; i++){
            new_tail = new_tail.next;
        }
        ListNode newhead = new_tail.next;
        new_tail.next = null;
        return newhead;
    }
}
