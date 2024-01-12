class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def append_list(self, data):
        for i in data:
            new_node = Node(i)
            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
    
    def insert(self, data, index):
        new_node = Node(data)
        if index == 0: #Being inserted at beggining
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if current_node.next is None: #Being inserted at end
            current_node.next = self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
    
    def delete(self, data):
        if self.head is None: #List is empty
            return
        current_value = self.head
        while current_value.next:
            if current_value.next.data == data:
                current_value.next = current_value.next.next
                if current_value.next is None: #After deletion, check the tail
                    self.tail = current_value
                return
            
    def to_list(self):
        list = []
        current_node = self.head
        while current_node:
            list.append(current_node.data)
            current_node = current_node.next
        return list

    def size(self):
        counter = 0
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def str(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

list1 = LinkedList()

print(list1.size())
list1.append("3")
list1.append("3")
list1.append("g")
list1.append_list([3, 2, 3, 6, 7])
list1.insert("k", 3)
print(list1.size())
print(list1.str())
print(list1.to_list())

