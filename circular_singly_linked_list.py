class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Maintain circular structure

    # Prepend to the beginning
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:  # Find the last node
                temp = temp.next
            temp.next = new_node  # Update last node to point to new head
            new_node.next = self.head
            self.head = new_node  # Update head reference

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")  # Indicate circular nature

    # Delete a node
    
    def delete(self, key):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        prev = None

        # Case 1: Deleting the head node
        if temp.data == key:
            if temp.next == self.head:  # Only one node in the list
                self.head = None
                return
            while temp.next != self.head:  # Find last node
                temp = temp.next
            temp.next = self.head.next  # Point last node to new head
            self.head = self.head.next  # Update head
            return

        # Case 2: Deleting any other node
        prev = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print(key, "not found in the list")

# Sample Usage
csll = CircularSinglyLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.prepend(5)

csll.display()  # Output: 5 -> 10 -> 20 -> 30 -> (head)

csll.delete(20)
csll.display()  # Output: 5 -> 10 -> 30 -> (head)

csll.delete(5)
csll.display()  # Output: 10 -> 30 -> (head)


"""
🛠️ Explanation of Key Operations
Append (append)

If the list is empty, the new node points to itself.

Otherwise, traverse to the last node and update its next to point to the new node, ensuring circular linkage.

Prepend (prepend)

If the list is empty, behave like append.

Otherwise, find the last node and update its next to the new node, then update self.head to the new node.

Delete (delete)

If the key is found in the head, update the last node to point to the new head.

If found in the middle or end, adjust prev.next to skip the node.

Display (display)

Traverse the list until you reach back to the head, ensuring circular traversal.

🚀 Why Use a Circular Singly Linked List?
✔ Useful for circular buffers, round-robin scheduling, and playlist management.
✔ No None in next, making traversal continuous.
✔ Efficient insertions and deletions compared to regular SLL.
"""
