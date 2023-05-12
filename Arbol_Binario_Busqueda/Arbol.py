"""System module."""
from Arbol_Binario_Busqueda.Nodo import Node

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

        if self.root is None:
            self.root = Node(label, None)
        else:
            self.insert_aux(self.root, label)

    def insert_aux(self, current:Node, label) -> None:
        """Auxiliar en la insersion de nuevas claves al arbol,
        Ingresa las claves nuevas tomando en cuenta las caracteristicas
        de un ABB"""
        if label < current.get_data():
            if current.get_left() is None:
                current = current.get_left()
                current = Node(label, None)
            else:
                self.insert_aux(current.get_left(), label)
        else:
            if current.get_right() is None:
                current = current.get_right()
                current = Node(label, None)
            else:
                self.insert_aux(current.get_right(), label)

    def is_leaf_node(self, node:Node):
        """Verifica si el nodo recibido es un nodo hoja"""
        if node.get_left == None and node.get_right() == None:
            return True
        return False


    def in_order(self, root_aux):
        """Recorrido del arbol en orden"""
        if root_aux is not None:
            self.in_order(root_aux.get_left())
            print(root_aux.get_data(), end=", ")
            self.in_order(root_aux.get_right())

tree = ABB()
ARRAY_DATA = [8, 3, 10, 1, 6, 14, 4, 7, 13]

tree.insert_node(8)
tree.insert_node(3)
tree.insert_node(10)
tree.insert_node(1)
tree.insert_node(6)
tree.insert_node(14)
tree.insert_node(4)
tree.insert_node(7)
tree.insert_node(13)
print(tree.root)

#tree.in_order(tree)
