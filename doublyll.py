class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append to the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Prepend to the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Search for a node
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    # Delete a node
    def delete(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:  # Deleting head
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return True
            temp = temp.next
        return False

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

# Sample usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()            # Output: 5 <-> 10 <-> 20

print("Searching 10:", dll.search(10) is not None)  # True
print("Searching 99:", dll.search(99) is not None)  # False

dll.delete(10)
dll.display()            # Output: 5 <-> 20
