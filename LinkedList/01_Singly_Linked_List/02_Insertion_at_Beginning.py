class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Manages all Linked List Operation
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

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


node = LinkedList()
node.insert_at_start(15)
print(node.head.data)
