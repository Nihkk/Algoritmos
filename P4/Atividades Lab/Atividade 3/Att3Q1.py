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
    
  def achar_menor(self):
    current_node = self.head

    menor = current_node.data

    while current_node:
      if current_node.data < menor:
        menor = current_node.data
      current_node = current_node.next

    return menor

lista = DoubleLinkedList()

lista.add(9)
lista.add(5)
lista.add(1)
lista.add(3)

print("------------")

lista.display()
menor = lista.achar_menor()

print("O menor valor da lista é:", menor)