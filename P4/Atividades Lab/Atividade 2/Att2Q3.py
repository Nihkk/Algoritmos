class Node:

  def __init__(self, dado_inicial):
    self.dado = dado_inicial
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None

  def add(self, dado):

    new_node = Node(dado)
    
    if self.head == None:
      self.head = new_node
      return
          
    current_node = self.head

    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node
    return

  def lenght(self):
    if self.head == None:
      return 0
    
    current_node = self.head
    total = 0

    while current_node:
      total += 1
      current_node = current_node.next
    return total
    
  def ordem_crescente(self):
    contador = 0
    current_node = self.head

    while current_node:
      if current_node.dado < current_node.next.dado:
        current_node = current_node.next
      else:
        contador += 1
        current_node = current_node.next
        
    if contador == 0:
      return 1
    else:
      return 2
        
lista = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)

resposta = lista.ordem_crescente()

if resposta == 1:
  print("Está em ordem crescente")
else:
  print("Não está em ordem crescente")