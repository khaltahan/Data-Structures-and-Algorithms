'''
The Stack class acts as a LIFO (Last In First Out) data structure.
It will have the following methods:
- push : Adds an element to the top of the stack.
- pop : Removes and returns the topmost element from the stack.
- isEmpty : Checks whether the stack is empty.
- isFull : Checks whether the stack is full.
- top : Displays the topmost element of the stack.
Optional: We will also add a method to give the stack more space
'''

class Stack:

    def __init__ (self, stack_length = 10):
        self.arr = [None for _ in range(stack_length)]
        self.next_element = 0
        self.element_length = 0
    
    def push (self, data):
        self.arr[self.next_element] = data
        self.next_element += 1
        self.element_length += 1
        if self.isFull():
            self.resizeStack()

    def pop (self):
        self.next_element -= 1
        element = self.arr[self.next_element]
        self.arr[self.next_element] = None
        self.element_length -= 1
        return element
    
    def isEmpty(self):
        return True if self.element_length == 0 else False
    
    def isFull(self):
        return True if self.element_length == len(self.arr) else False
    
    def resizeStack (self):
        old_arr = self.arr

        self.arr = [None for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

foo = Stack()
foo.push("Test!")
print(foo.arr)
print("Pass" if foo.arr[0] == "Test!" else "Fail")
print(foo.pop())
print(foo.arr)
print(foo.isEmpty())
print(foo.isFull())
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
foo.push("Test!")
print(foo.isEmpty())
print(foo.isFull())
print(foo.arr)