class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)  # Fixed the syntax error here
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        # Implementation for inserting at a specific index
        pass  # Placeholder for the actual implementation

    def insertAtEnd(self, data):
        # Implementation for inserting at the end
        pass  # Placeholder for the actual implementation

    def remove_node(self, data):
        # Implementation for removing a node
        pass  # Placeholder for the actual implementation

    def sizeOfLL(self):
        # Implementation for getting the size of the linked list
        pass  # Placeholder for the actual implementation

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicates the end of the linked list
    def remove_node(self, data):
         current  while current:
            if current.data == data_to_remove:
                # Found the node to remove
                if prev:
                    prev.next = current.next  # Update the previous node's next pointer
                else:
                    # If the target node is the head, update the head
                    self.head = current.next
                return  # Exit the loop
            prev = current
            current = current.next

        print(f"Node with data {data_to_remove} not found in the linked list.")
    _
# Example usage:
my_list = LinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.printLL()  # Output should be: 30 -> 20 -> 10 -> None
my_list.remove_node(10)
my_list.printLL()