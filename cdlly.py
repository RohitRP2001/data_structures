class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            # First node points to itself in both directions
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev  # Last node
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def prepend(self, data):
        self.append(data)
        self.head = self.head.prev  # Move head to the new node

    def delete(self, data):
        if not self.head:
            return

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:  # Only one node
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break  # Element not found

    def display(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("... (back to head)")

    def search(self, data):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == data:
                print(data, "found")
                return 
            current = current.next
            if current == self.head:
                break
        print(data, "not found")
        return False


# Example usage
cll = CircularDoublyLinkedList()
cll.append(10)
cll.append(20)
cll.prepend(5)
cll.display()  # 5 <-> 10 <-> 20
cll.delete(10)
cll.display()  # 5 <-> 20
cll.search(5)