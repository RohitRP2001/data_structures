class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(item,"enqueued")
          # Add item to the end of the list

    def dequeue(self):
        if self.is_empty():
            print("empty queue")
            return
        print(self.items.pop(0),"dequeued")  # Remove item from the front of the list

    def peek(self):
        if self.is_empty():
            print("empty queue")
            return
        print("Q first elemnt",self.items[0])

    def size(self):
        return len(self.items)
    
    def display(self):
        print("displaying queue",self.items)

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.peek()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.dequeue()  # Output: 1
    q.peek()    # Output: 2
    print(q.size())     # Output: 2
