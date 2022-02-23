# coding=utf-8
# Online Python - IDE, Editor, Compiler, Interpreter


def afficher(*parametres,sep=' ', fin='\n' ):
    """Fonction réalisant la même fonction que print"""
    str_sortie=''
    for i in parametres :
        #On fait la concatenation de l'entree avec un séparateur"
        str_sortie+=str(i) + sep
    #On rajoute la fin
    str_sortie+=fin
    print(str_sortie)

afficher("Ceci est un test",2)        
