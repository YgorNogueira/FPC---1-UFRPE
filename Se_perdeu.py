class Node():
    def __init__(self, data):
        self._data = data
        self._father = None
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return str(self._data)

    def getData(self):
        return self._data

    def getFather(self):
        return self._father

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setData(self, value):
        self._data = value

    def setFather(self, value):
        self._father = value
    
    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value

class Tree(Node):

    def __init__(self):
        self._root = None
        self._view = ''
        self._maior = 0
        self._x = 0

    def __repr__(self):
        return 'raiz:', self._root

    def getRoot(self):
        return self._root
    
    def search(self, value):
        node = self._root
        while node != None and value != node.getData():
            if value < node.getData():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node
    
    def minimum(self, node):
        while node.getLeft() != None:
            node = node.getLeft()
        return node

    def maximum(self, node):
        while node.getRight() != None:
            node = node.getRight()
        return node

    def successor(self, node):
        if node.getRight() != None:
            return self.minimum(node.getRight())
        y = node.getFather()
        while y != None and node == y.getRight():
            node = y
            y = node.getFather()
        return y
    
    def add(self, value):
        node = Node(value)
        y = None
        x = self._root
        while x != None:
            y = x
            if node.getData() < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y == None:
            self._root = node
        elif node.getData() < y.getData():
            y.setLeft(node)
        else:
            y.setRight(node)
        
    def delete(self, value):
        z = self.search(value)
        if z != None:
            if z.getLeft() == None or z.getRight() == None:
                y = z
            else:
                y = self.successor(z)
            if y.getLeft() != None:
                x = y.getLeft()
            else:
                x = y.getRight()
            if x != None:
                x.setFather(y.getFather())
            if y.getFather() == None:
                self._root = x
            else:
                if y == y.getFather().getLeft():
                    y.getFather().setLeft(x)
                else:
                    y.getFather().setRight(x)
            if y != z:
                z.setData(y.getData())
            return y

    #views
    def inOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else:
            return '0 '

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.getLeft())
            self._view += str(node) + ' '
            self.inOrder(node.getRight()) 

    def inPreOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inPreOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else:
            return '0 '

    def inPreOrder(self, node):
        if node != None:
            self._view += str(node) + ' '
            self.inPreOrder(node.getLeft())           
            self.inPreOrder(node.getRight()) 

    def inPostOrderPrint(self):
        if self._root is not None:
            raiz = self._root
            self.inPostOrder(raiz)
            out = self._view
            self._view = ''
            return out
        else: 
            return '0 '

    def inPostOrder(self, node):
        if node != None:            
            self.inPostOrder(node.getLeft())           
            self.inPostOrder(node.getRight()) 
            self._view += str(node) + ' '

    def greaterLess(self, value):
        node = self._root
        self._x = value
        self.inorderTreeWalk2(node)
        out = self._maior
        self._maior = 0
        self._x = 0 
        return out

    def inorderTreeWalk2(self, node):
        if node != None:
            self.inorderTreeWalk2(node.getLeft())
            if node.getData() > self._maior and node.getData() < self._x:
                self._maior = node.getData()
            self.inorderTreeWalk2(node.getRight())


#--------------------------------------------------------------------

def run(caso):
   loop = int(input())
   print('Caso %i:' %(caso))
   tree = Tree()
   for i in range(loop):
        comando = input().split()
        if comando[0] == 'A':
            tree.add(int(comando[1]))
            
        elif comando[0] == 'B':           
            tree.delete(int(comando[1]))
            
        elif comando[0] == 'C':
            print(tree.greaterLess(int(comando[1])))
            
        elif comando[0] == 'PRE':
            print(tree.inPreOrderPrint()[:-1])
            
        elif comando[0] == 'IN':
            print(tree.inOrderPrint()[:-1])
            
        elif comando[0] == 'POST':
            print(tree.inPostOrderPrint()[:-1])
            

#--------------------------------------------------------------------
caso = 1
while True:
    try:        
        run(caso)
        caso += 1
    except:
        break