class Stack:
    def __init__(self, max_size):
        self.stack = [None] * max_size  # Initialize stack with a fixed size
        self.max_size = max_size
        self.top = -1  # Initialize top pointer to -1 (empty stack)

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push", item)
        else:
            self.top += 1
            self.stack[self.top] = item
            print(item, "\tpushed")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack")
            return None
        else:
            popped_item = self.stack[self.top]
            self.stack[self.top] = None  # Optional: Clear the popped slot
            self.top -= 1
            print(popped_item, "popped")
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty, cannot peek")
            return None
        else:
            return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("displaying stack  []")
        else:
            print("displaying stack ", self.stack[self.top::-1])

print('Hi')
if __name__ == "__main__":
    print("Welcome to main")
    my_stack = Stack(5)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(6)
    my_stack.push(7)
    my_stack.display()
    my_stack.pop()
    my_stack.display()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.display()
    print("Top element:", my_stack.peek())

print("bye")