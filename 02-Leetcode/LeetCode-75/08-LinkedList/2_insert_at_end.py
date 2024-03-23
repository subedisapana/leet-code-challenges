"""
1. Create a node name new_end: to create use node class with element as 200 (data) and link/reference to null
2. Insert element at the last
3. Before even inserting, wee need to check whether its empty or not, 
If empty, whatever node we are adding, this is the first node of the linkedinlist

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)

print("Linked list:")
llist.display()
