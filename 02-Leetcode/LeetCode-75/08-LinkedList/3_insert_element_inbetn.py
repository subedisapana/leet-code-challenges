"""
1. Insert 20 at index 2
2. Create a new_node, if insertion is in index 0 (at the beginning)
new_node.next = self.head
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0: # index
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Given data
    data = [1, 2, 3, 4, 5]
    
    # Insert data into the linked list
    for index, value in enumerate(data):
        linked_list.insert_at_position(index, value)

    # Insert 40 at index 2
    linked_list.insert_at_position(2, 40)

    # Print the linked list
    linked_list.print_list()
