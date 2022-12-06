class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None
        self.grau = None
        self.check = None
        
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node

    def add(self, data):
        new_node = Node(data)
        atual = self.root
        i = 1

        while(i == 1):
            if new_node.data < atual.data:
                if not atual.left:
                    atual.left = new_node
                    new_node.prev = atual
                    return
                else:
                    atual = atual.left
            else:
                if not atual.right:
                    atual.right = new_node
                    new_node.prev = atual
                    return
                else:
                    atual = atual.right
            
    def contarFilhos(self):
        atual = self.root

        if atual:
            while(atual.prev != None or atual.check != True):
                if atual.left and atual.grau == None:
                    atual.grau = 1
                    if atual.right:
                        atual.grau = 2
                        print("O nó " + str(atual.data) + " tem como filhos os nós " + str(atual.left) + " e " + str(atual.right))
                        temp = atual
                        atual = atual.left
                        atual.prev = temp
                    else:
                        print("O nó " + str(atual.data) + " tem como filho o nó " + str(atual.left))
                        atual.check = True
                        temp = atual
                        atual = atual.left
                        atual.prev = temp

                elif atual.right and atual.grau == None:
                    atual.grau = 1
                    print("O nó " + str(atual.data) + " tem como filho o nó " + str(atual.right))
                    atual.check = True
                    atual.prev = atual
                    atual = atual.right

                elif atual.right and atual.check != True:
                    atual.check = True
                    temp = atual
                    atual = atual.right
                    atual.prev = temp
                
                elif atual.grau == None:
                    atual.grau = 0
                    print("O nó " + str(atual.data) + " não possui filhos")
                    atual = atual.prev

                elif atual.check == True:
                    atual = atual.prev
            
        else:
            print("A árvore está vazia!")
            return

tree = BinaryTree(10)
tree.add(12)
tree.add(8)
tree.add(9)
tree.add(7)
tree.add(11)
tree.add(13)
tree.contarFilhos()