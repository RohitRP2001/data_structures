class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #newly created node's next will be None

class SinglyLinkedList:

    def __init__(self):
        self.head = None  #initially head is None

    def is_empty(self):
        return self.head is None
    
    def prepend(self,data): #insert at the begenning of the list

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(new_node.data,"prepended to the list")
    
    def append(self,data):
        new_node = Node(data)
        #if list is empty
        if self.is_empty():
            self.head = new_node
            print(data," appended to list")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(data," appended to list")
        return
    
    def search(self,data):
        if self.is_empty():
            print("list empty")
            return 
        current = self.head
        while current:
            if current.data == data:
                print(data," is present in the list")
                return
            current = current.next
        print(data," is not present in the list")
    
    def insert_after(self, prev_data, new_data):
        """
        Inserts a new node with new_data after the first node containing prev_data.

        Args:
            prev_data: The data of the node after which the new node will be inserted.
            new_data: The data to be stored in the new node.
        """
        if self.is_empty():
            print("List is empty. Cannot insert.")
            return

        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print(f"Node with data '{prev_data}' not found.")


   
    def display(self):
        if self.is_empty():
            print("list empty")
            return 
        current = self.head
        sll = []
        while current:
            print(current.data, end=" ->")
            current = current.next
        print()
    def delete(self,data):
        """
        steps

        1. check if list is empty
        2. check if head node is the one to del if yes, change the head node's address
        3. traverse thru entire list and if found update the pointers
        """
        if self.is_empty():
            print("empty list")
            return
        if self.head.data == data:
            self.head = self.head.next 
            print(data, " deleted from list")
            return
        
        current = self.head
        while current: 
            if current.next.data == data:
                current.next = current.next.next
                print(data, " deleted from list")
                return
            current = current.next    
        

if __name__ == "__main__":

    my_singly_ll = SinglyLinkedList()

    my_singly_ll.prepend(10)
    my_singly_ll.display()
    my_singly_ll.prepend(20)
    my_singly_ll.insert_after(10,11)
    my_singly_ll.prepend(30)
    my_singly_ll.append(5)
    
    my_singly_ll.display()
    my_singly_ll.search(20)
    my_singly_ll.delete(20)
    my_singly_ll.display()
    my_singly_ll.search(5)
    

    
