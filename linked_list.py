class Cell:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Cell(None)
  
  def insert(self,value):
    front = self.head
    rear  = front.next
    
    while rear and value > rear.value:
      front = rear
      rear = rear.next
    cell = Cell(value)
    cell.next = rear
    front.next = cell
    
  def show(self):
    tmp = self.head.next
    while tmp:
      print(tmp.value)
      tmp = tmp.next

link = LinkedList()
link.insert(5)
link.insert(1)
link.insert(3)

link.show()