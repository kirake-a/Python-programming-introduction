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


