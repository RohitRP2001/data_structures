class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class IterativeBST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(self, key):
        current = self.root
        while current:
            if current.key == key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, key):
        parent = None
        current = self.root

        # Find the node and its parent
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # Key not found

        # Case 1: Node with two children
        if current.left and current.right:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.key = successor.key
            current = successor
            parent = successor_parent

        # Now node has at most one child
        child = current.left if current.left else current.right

        if parent is None:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

    def inorder(self):
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.key)
            current = current.right

        return result

# Example usage
bst = IterativeBST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder())
print("Search 60:", bst.search(60))  # True
print("Search 25:", bst.search(25))  # False

bst.delete(20)
bst.delete(30)
bst.delete(50)

print("Inorder traversal after deletes:", bst.inorder())
