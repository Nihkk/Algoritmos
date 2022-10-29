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

  def display(self):
    content = self.head

    if content is None:
      print("Lista vazia!")

    while content:
      print(content.dado)
      content = content.next
    print("------------")

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
    next_node = current_node.next

    while current_node and next_node:
      if current_node.dado > next_node.dado:
        contador += 1
      current_node = next_node
      next_node = next_node.next
      
        
    if contador == 0:
      return True
    else:
      return False
        
lista = LinkedList()
lista2 = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)

lista2.add(3)
lista2.add(2)
lista2.add(1)

resposta = lista.ordem_crescente()
resposta2 = lista2.ordem_crescente()

print("")
lista.display()
if resposta == True:
  print("Está em ordem crescente")
else:
  print("Não está em ordem crescente")

print("")
lista2.display()
if resposta2 == True:
  print("Está em ordem crescente")
else:
  print("Não está em ordem crescente")