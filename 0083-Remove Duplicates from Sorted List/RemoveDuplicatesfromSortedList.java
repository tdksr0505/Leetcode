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
        if(head == null) return head;
        ListNode preNode = head;
        ListNode currentNode = head.next;
        for(; currentNode!=null ;){
            if(preNode.val != currentNode.val){
                preNode.next = currentNode;
                preNode = currentNode;
            }
            currentNode = currentNode.next;
        }
        preNode.next = null;
        return head;
    }
}