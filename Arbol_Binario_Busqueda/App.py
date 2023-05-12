"""System module."""

from Arbol import ABB

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