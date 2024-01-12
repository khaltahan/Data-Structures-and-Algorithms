class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)
    

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None: #No node exists
            self.head = new_node
            self.tail = new_node
            return
        
        if data <= self.head.data: #Before head
            new_node.next = self.head
            self.head = new_node
            return
        
        if data >= self.tail.data: #After tail head
            self.tail.next = new_node
            self.tail = new_node
            return
        
        current_node = self.head
        while current_node.next and data >= current_node.next.data:
            current_node = current_node.next
            
        new_node.next = current_node.next
        current_node.next = new_node
        
# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.data == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.data == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.data == 4) else "Fail")


def sort(array):
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for data in array:
        linked_list.append(data)
    
    node = linked_list.head
    while node:
        sorted_array.append(node.data)
        node = node.next
    
    return sorted_array

print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")
