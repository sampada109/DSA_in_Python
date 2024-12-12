class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Manages all Linked List Operation
class LinkedList: 
  def __init__(self):
    self.head = None
    self.tail = None
 
  #insertion at starting
  def insert_at_start(self, data):
    #create a new node
    newNode = Node(data)
    #if linked lsit is empty
    if(self.head == None):
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    
  #traversing
  def traverse(self):
    if self.head == None:
        print("Linked List is Empty")
    temp = self.head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')  



node = LinkedList()
node.insert_at_start(15)
node.traverse()
node.insert_at_start(22)
node.traverse()
node.insert_at_start(3)
node.traverse()
print(f'HEAD - {node.head.data}')
print(f'TAIL - {node.tail.data}')
