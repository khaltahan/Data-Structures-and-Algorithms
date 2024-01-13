def even_after_odd(head):
    if head is None:
        return None
    
    even_head = None
    even_tail = None
    
    odd_head = None
    odd_tail = None
    
    current_node = head
    while current_node:
        if current_node.data % 2 == 0:
            if not even_head:
                even_head = current_node
                even_tail = current_node
            else:
                even_tail.next = current_node
                even_tail = current_node
        else:
            if not odd_head:
                odd_head = current_node
                odd_tail = current_node
            else:
                odd_tail.next = current_node
                odd_tail = current_node
        current_node = current_node.next
    if even_head is None:
        return odd_head
    if odd_head is None:
        return even_head
    
    odd_tail.next = even_head
    
    return odd_head