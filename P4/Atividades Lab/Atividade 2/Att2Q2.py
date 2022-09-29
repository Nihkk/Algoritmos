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

  def profundidade(self, alvo):
    aux = alvo
    contador = 0
    current_node = self.head

    while current_node:
      if current_node.dado != aux:
        contador += 1
        current_node = current_node.next
      else:
        return contador
        break
        
    

lista = LinkedList()

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(6)
lista.add(8)

alvo = 8

profundidade = lista.profundidade(alvo)

print("A profundidade deste nó é igual a:", profundidade)