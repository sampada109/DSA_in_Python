# INSERTION AT END OF LINKED LIST

# NODE CLASS THAT CREATES A NEW NODE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

# LINKEDLIST CLASS THAT MANAGES ALL OPERATIONS
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # TRAVERSAL
    def traverse(self):
        # IF LL IS EMPTY
        if self.head == None:
            print('Linked List is Empty')
            return
        # WHEN ONE OR MORE NODE EXISTS
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print(' ')
        print(f'HEAD - {node.head.data}, TAIL - {node.tail.data}')


    # INSERTION AT END
    def insert_at_end(self, data):
        # CREATE A NODE
        newNode = Node(data)
        # IF LL IS EMPTY
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        # INSERT AT END
        self.tail.next = newNode
        self.tail = newNode


if __name__ == "__main__":
    
    node = LinkedList()
    node.insert_at_end(4)
    node.traverse()
    node.insert_at_end(10)
    node.traverse()
    node.insert_at_end(8)
    node.traverse()
    node.insert_at_end(55)
    node.traverse()
    node.insert_at_end(2)
    node.traverse()
