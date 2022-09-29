class DoubleNode:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoubleLinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, data):
    new_node = DoubleNode(data)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def display(self):
    content = self.head

    if content is None:
      print("Lista vazia!")

    while content:
      print(content.data)
      content = content.next
    print("------------")

  def altura(self, numero):
    current_node = self.head
    a = numero
    contador = 0

    while current_node:
      if current_node.data == a:
        while current_node:
          current_node = current_node.next
          contador += 1
      else:
        current_node = current_node.next

    return contador - 1

lista1 = DoubleLinkedList()

lista1.add(9)
lista1.add(5)
lista1.add(1)
lista1.add(7)
lista1.add(3)
lista1.add(8)
lista1.add(4)

num = 4

print("A altura do elemento (", num,") na lista é:", lista1.altura(num))
