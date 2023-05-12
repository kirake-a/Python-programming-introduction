"""System module."""
from Nodo import Node

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
