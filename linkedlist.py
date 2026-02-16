# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes
node1.next = node2
node2.next = node3

# Traverse
current = node1
print("Linked List:")
while current:
    print(current.data)
    current = current.next
