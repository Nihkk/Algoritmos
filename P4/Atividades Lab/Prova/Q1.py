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
            
    def contarGraus(self):
        atual = self.root

        if atual:
            while(atual.prev != None or atual.check != True):
                if atual.left and atual.grau == None:
                    atual.grau = 1
                    if atual.right:
                        atual.grau = 2
                        if atual.prev:
                            atual.grau = 3
                            print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                            temp = atual
                            atual = atual.left
                            atual.prev = temp
                        else:
                            print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                            temp = atual
                            atual = atual.left
                            atual.prev = temp
                    elif atual.prev:
                        atual.grau = 2
                        print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                        atual.check = True
                        temp = atual
                        atual = atual.left
                        atual.prev = temp
                    else:
                        print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                        atual.check = True
                        temp = atual
                        atual = atual.left
                        atual.prev = temp

                elif atual.right and atual.grau == None:
                    atual.grau = 1
                    if atual.prev:
                        atual.grau = 2
                        print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                        atual.check = True
                        atual.prev = atual
                        atual = atual.right
                    else:
                        print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                        atual.check = True
                        atual.prev = atual
                        atual = atual.right


                elif atual.right and atual.check != True:
                    atual.check = True
                    temp = atual
                    atual = atual.right
                    atual.prev = temp
                
                elif atual.prev and atual.grau == None:
                    atual.grau = 1
                    print("O nó " + str(atual.data) + " tem grau: " + str(atual.grau))
                    atual = atual.prev

                elif atual.prev and atual.check == True:
                    atual = atual.prev
            
        else:
            print("A árvore está vazia!")
            return

tree = BinaryTree(10)
tree.add(11)
tree.add(8)
tree.add(9)
tree.add(7)
tree.contarGraus()