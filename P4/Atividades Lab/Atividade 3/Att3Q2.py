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

  def é_identica_a(self, lista2):
    a = self.head
    b = lista2.head

    while a and b:
      if a.data != b.data:
        return False
      a = a.next
      b = b.next
    return a == None and b == None
    
  

lista1 = DoubleLinkedList()
lista2 = DoubleLinkedList()
lista3 = DoubleLinkedList()

lista1.add(9)
lista1.add(5)
lista1.add(1)
lista1.add(3)

lista2.add(9)
lista2.add(5)
lista2.add(1)
lista2.add(3)

lista3.add(1)
lista3.add(2)
lista3.add(3)
lista3.add(4)

lista1.display()
lista2.display()

if lista1.é_identica_a(lista2) == True:
  print("São identicas")
else:
  print("Não são identicas")

print("")
lista1.display()
lista3.display()

if lista1.é_identica_a(lista3) == True:
  print("São identicas")
else:
  print("Não são identicas")