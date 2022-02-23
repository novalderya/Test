# coding=utf-8
# Online Python - IDE, Editor, Compiler, Interpreter


def afficher_flottant(flottant):
    """Fonction permettant d'afficher un flottant avec trois chiffres avec une virgule"""
    #On regarde si on travaille bien avec un flottant
    if type(flottant) is  float :
        
        flt_str=str(flottant)  # On le transforme en str
        flt_list=flt_str.split(".") # On le separe de facon a avoir la partie entiere et partie a virgule
        flt_value=",".join([flt_list[0],flt_list[1][0:3]]) #On joint les deux parties avec une virgule
        return flt_value
    #On le retourne juste si ce n'est pas un flottant pour éviter les problèmes
    else :
        return flottant
#Test de la fonction        
print(afficher_flottant(2.8))
print(afficher_flottant(6))
print(afficher_flottant(2.88677))
print(afficher_flottant(2.800))