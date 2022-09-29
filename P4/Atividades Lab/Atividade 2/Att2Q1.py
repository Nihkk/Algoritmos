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

  def mostrar_pares(self):
    contador = 0
    current_node = self.head

    while current_node:
      if current_node.dado % 2 == 0:
        contador += 1
      current_node = current_node.next
    return contador
    

lista = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(6)

pares = lista.mostrar_pares()

print("A quantidade de pares na lista é:", pares)