# Write a class that implements a queue data structure using lists

class Queue:
    def __init__(self):
        self.items = [] # Initialize an empty list to store queue items 

    def enqueue(self, item):
        self.items.append(item) # Add an item to the end of the queue

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None # Remove and return the front item of the queue
    
    def peek(self):
        return self.items[0] if not self.is_empty() else None # Return the front item from the queue without removing it
    
    def is_empty(self):
        return len(self.items) == 0 # Check if queue is empty
    
    def size(self):
        return len(self.items) # Return number of items in the queue
    
# Use example 
my_queue = Queue()
my_queue.enqueue('a')
my_queue.enqueue('b')
my_queue.enqueue('c')

print("Current queue:", my_queue.items)
print("Dequeued item:", my_queue.dequeue())
print("Current queue after dequeue:", my_queue.items)
print("Front item:", my_queue.peek())
print("Is the queue empty?", my_queue.is_empty())
print("Queue size:", my_queue.size())