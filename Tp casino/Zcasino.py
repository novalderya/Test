# coding=utf-8
# Online Python - IDE, Editor, Compiler, Interpreter

#Importation des librairies utiles
from random import randrange
from math import ceil

#Définition de variables utiles
Running=1    #Booléen vérifiant si on continue a jouer ou pas
somme_possede=1000 # Somme possede au depart

while Running :
    #On affiche la somme possede au joueur pour qu'il mise
    print("Vous possedez {} $".format(somme_possede))
    mise=0
    #On demande la mise jusqu'a ce que l'utilisateur tape une valeur attendue par le programme
    while (mise<=0 or mise>somme_possede):

        mise=input("Quelle mise souhaitez vous mettre :")
        #On regarde si on peut convertir en entier , s'il est dans l'intervalle attendu
        try : 
            mise=int(mise)
        except ValueError :
            print("On attend un nombre pour la mise")
            mise=0
        if mise<0 : 
            print("La mise ne doit pas etre négative ")
        if mise>somme_possede :
            print("La mise ne doit pas etre supérieur a l'argent possédé")
    
    nombre_choisi=-1
    #On demande le nombre choisi par l'utilisateur donc on verifie que l'entree correspond a ce que l'on veut 
    while (nombre_choisi<0 or nombre_choisi>49)  :
        print("Choissisez votre nombre entre 0 et 49")  
      
        nombre_choisi=input()  
        #On regarde si le nombre choisi est bien un int si il est dans l'intervalle attendu
        try : 
            nombre_choisi=int(nombre_choisi)
        except ValueError :
            print("On attend un nombre pour la mise")
            nombre_choisi=-1
        if nombre_choisi<0:
            print("Le nombre doit être supérieure à 0")
        if nombre_choisi>49:
            print("Le nombre doit être inférieure à 49")
          
    #On tire un nombre aléatoire     
    nombre_obtenu_roulette=randrange(50)
    print("Le nombre obtenu à la roulette est {}".format(nombre_obtenu_roulette))
    #On regarde si on a le nombre exact ou la meme couleur ou si on a perdu et on affiche un message correspondant
    if nombre_obtenu_roulette==nombre_choisi :
        mise_gagne=ceil(mise*3)
        somme_possede+=mise_gagne
        print("Bravo vous avez obtenu le nombre exact !, vous gagnez {} $".format(mise_gagne))
    else : 
        if (nombre_choisi%2==nombre_obtenu_roulette%2):
            mise_gagne=ceil(mise/2)
            somme_possede-=mise_gagne
            print("Vous avez obtenu la même couleur vous avez gagné {} $".format(mise_gagne))
  
        else: 
            somme_possede-=mise
            print("Vous n'avez pas obtenu la même couleur , vous perdez votre mise ")
    #On demande si le joueur souhaite continuer a jouer et s'il n'a plus d'argent il est force a arrêter
    print("Vous posséder {} $".format(somme_possede))
    if (somme_possede==0):
        print("Vous ne pouvez plus jouer vous n'avez plus d'argent")
        Running=0
    else :
        #Si l'utilisateur tape autre chose que 0 il continue a jouer        
        test_sortie=input("Souhaitez vous continuer à jouer ? taper 1 pour continuer , 0 sinon")  
        if test_sortie==0 : 
            Running =0
            #On affiche la somme qu'il possede en partant
            print("Vous partez du casino avec {} $".format(somme_possede))


        
        
        
        
