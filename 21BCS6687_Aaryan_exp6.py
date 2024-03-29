class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None

def traversal(node):
    if node is None:
        return
    
    print(node.data, end = ' ')

    traversal(node.left)
    traversal(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

traversal(root)