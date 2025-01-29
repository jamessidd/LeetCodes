    if(head == null || head.next == null){
        return head;
    }

    ListNode slow = head;
    ListNode fast = head;
    ListNode dummy = head;

    while(fast.next != null&& fast.next.next!= null){
        slow = slow.next;
        fast = fast.next;
    }

    while(dummy.next != slow){
        dummy = dummy.next;
    }
    dummy.next = dummy.next.next;
    return head;
}