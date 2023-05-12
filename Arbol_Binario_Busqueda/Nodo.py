"""System module."""

class Node:
    """Nodo para un arbol binario de busqueda"""
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.data

    def get_data(self):
        """Retorna el valor contenido en el nodo"""
        return self.data
  
    def set_data(self, data) -> None:
        """Cambia el valor contenido en el nodo"""
        self.data = data

    def get_left(self):
        """Retorna el nodo izquierdo"""
        return self.left

    def set_left(self, left):
        """Establece el nodo izquierdo"""
        self.left = left

    def get_right(self):
        """Retorna al nodo derecho"""
        return self.right

    def set_right(self, right) -> None:
        """Establece el nodo derecho"""
        self.right = right

    def get_parent(self):
        """Retorna al nodo padre del nodo actual"""
        return self.parent
    
    def set_parent(self, parent):
        """Establece al padre del nodo actual"""
        self.parent = parent

class ABB:
    """Arbol binario de busqueda"""
    def __init__(self):
        self.root: Node = None
    
    def is_empty(self):
        """Verifica si el arbol esta vacio"""
        if self.root is None:
            return True
        return False

    def insert_node(self, label) -> None:
        """Inserta un nuevo nodo al ABB"""

        if self.is_empty():
            self.root = Node(label, None)
        else:
            self.insert_aux(self.root, label)

    def insert_aux(self, current:Node, label) -> None:
        """Auxiliar en la insersion de nuevas claves al arbol,
        Ingresa las claves nuevas tomando en cuenta las caracteristicas
        de un ABB"""
        if label < current.get_data():
            if current.get_left() is None:
                parent = current
                new_node = Node(label, None)
                current.set_left(new_node)

                left = current
                left.set_parent(parent)
            else:
                self.insert_aux(current.get_left(), label)
        else:
            if current.get_right() is None:
                parent = current
                new_node = Node(label, None)
                current.set_right(new_node)

                right = current
                right.set_parent(parent)
            else:
                self.insert_aux(current.get_right(), label)

    def is_leaf_node(self, node:Node):
        """Verifica si el nodo recibido es un nodo hoja"""
        if node.get_left == None and node.get_right() == None:
            return True
        return False

    def pre_order(self, root_aux: Node):
        """Recorrido del arbol en orden"""
        if root_aux is not None:
            print(root_aux.__repr__(), end=", ") # R
            self.in_order(root_aux.get_left()) #
            self.in_order(root_aux.get_right()) #

    def in_order(self, root_aux: Node):
        """Recorrido del arbol en orden"""
        if root_aux is not None:
            self.in_order(root_aux.get_left()) #
            print(root_aux.__repr__(), end=", ") # R
            self.in_order(root_aux.get_right()) #
    
    def post_order(self, root_aux: Node):
        """Recorrido del arbol en orden"""
        if root_aux is not None:
            self.in_order(root_aux.get_left()) #
            self.in_order(root_aux.get_right()) # 
            print(root_aux.__repr__(), end=", ") # R

tree = ABB()
ARRAY_DATA = [8, 3, 10, 1, 6, 14, 4, 7, 13]
ARRAY_DATA_2 = [9, 2, 5, 3, 15]

for element in ARRAY_DATA:
    tree.insert_node(element)

for num in ARRAY_DATA_2:
    tree.insert_node(num)

#print(tree.root.__repr__())
print("preorden", end='  ')
tree.pre_order(tree.root)
print()
print("inorden", end='  ')
tree.in_order(tree.root)
print()
print("postorden", end='  ')
tree.post_order(tree.root)
