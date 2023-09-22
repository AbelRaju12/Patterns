class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverselist(head):
    prev, curr = None, head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

def mergeTwoLists(list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current =current.next
        
        if list1 != None:
            current.next = list1
        else:
            current.next = list2
        return head.next
        