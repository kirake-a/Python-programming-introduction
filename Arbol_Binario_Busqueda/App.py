"""System module."""

from Arbol_Binario_Busqueda.Arbol import ABB

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