# coding=utf-8
# Programme contenant les programmes nécessaires au pendu

from random import randrange
    
def demande_lettre_utilisateur(lettre_dite):
    """Fonction demandant a l'utilisateur de taper une lettre et si l'utilisateur ne tape
    pas une lettre la fonction redemande """
    lettre=''
    #On continue si ce n'est pas une lettre entree , si la lettre a deja ete dite et si on tape plus d'une lettre ou pas de lettre
    while lettre in lettre_dite or  len(lettre)!=1 or not lettre.isalpha() :

        lettre=input("Quel lettre voulez vous utiliser ?")
        if len(lettre)!=1  :
            print("Il  faut utiliser une seule lettre")
        elif lettre in lettre_dite :
            print("Vous avez deja utilisé cette lettre auparavant")
        elif not lettre.isalpha() :
            print("Il faut taper une lettre")
        #On ajoute la lettre au lettre dite
    lettre_dite.append(lettre)
    return lettre

def mot_choisi_aleatoirement(liste_mot):
    """Fonction permettant de choisir un mot aleatoire dans la liste de mot possible"""
    index_aleatoire=randrange(len(liste_mot))
    return (liste_mot[index_aleatoire])
  
def resultat_essai(lettre_demande,mot_actuel):
    """Fonction permettant d'afficher si on decouvert une lettre dans le mot ou non"""
    #On ajoute un compteur pour savoir le nombre de fois que la lettre est présente dans le mot
    cpt_lettre=0
    if lettre_demande in mot_actuel :
        for i in range(len(mot_actuel)) :
            if mot_actuel[i]==lettre_demande :
                cpt_lettre+=1
        print("Bravo il y a {} {} dans le mot a deviner".format(cpt_lettre,lettre_demande))
    else :
        print("Il n'y a pas de {} dans le mot ".format(lettre_demande))
  
   
def affichage_mot_decouvert(mot_actuel,lettre_dite):
    """Fonction permettant de réaliser l'affichage du mot avec les lettres découvertes et 
    avec des étoiles sur les mots non découverts et qui renvoie le nombre de lettre du mot découvert"""
    cpt_lettre_decouverte=0
    mot_decouvert=""
    for i in range(len(mot_actuel)):
        #On ajoute la lettre si on l'a deja dite sinon on met une etoile
        if mot_actuel[i] in lettre_dite:
            mot_decouvert+=mot_actuel[i]
            cpt_lettre_decouverte+=1
        else : 
            mot_decouvert+='*'
    print(mot_decouvert)        
    return cpt_lettre_decouverte    

#Test sur les fonctions developpe          
if __name__=="__main__":
    demande_lettre_utilisateur(['a','b'])