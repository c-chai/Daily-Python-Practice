# Create a program which the class Stack 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(f'Current stack: {my_stack.items}')