# coding=utf-8
# Online Python - IDE, Editor, Compiler, Interpreter

#definition de la liste
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
 ]

list_inverse=[(nbr,elt) for elt,nbr in inventaire]     #Inversion de la liste
list_inverse.sort(reverse=True)                        #Tri de la liste
inventaire_trie=[(nbr,elt) for elt,nbr in list_inverse]#Reinversion de la liste
print(inventaire_trie)
