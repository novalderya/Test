# coding=utf-8
# Online Python - IDE, Editor, Compiler, Interpreter
#Programme principal du jeu pendu

#Importation de librairie
from donnees import *
from fonctions import *
import pickle
import os

#définition de variables utiles
nombre_d_erreur=0
cpt_lettre_decouverte=0
cpt_tampon=cpt_lettre_decouverte
#On recupere le mot a deviner
mot_actuel=mot_choisi_aleatoirement(Mot_possible)
#On recupere nom d'utilisateur
nom_utilisateur=input("Taper votre nom d'utilisateur : ")

#On affiche le mot a decouvrir avec des etoiles pour permettre de montrer la longueur du mot
print("Voici le mot a deviner : ")
affichage_mot_decouvert(mot_actuel,lettre_dite)
#On continue a jouer tant que l'on a pas fait le nombre d'erreur max autorise ou si on a decouvert le mot
while nombre_d_erreur<nombre_d_essai_max and cpt_lettre_decouverte!=len(mot_actuel) :
    #On demande la lettre a l'utilisateur
    lettre_demande=demande_lettre_utilisateur(lettre_dite)
    #On affiche si il a decouvert ou non une lettre dans le mot
    resultat_essai(lettre_demande,mot_actuel)
    #On compte le nombre de lettre decouverte et on aficche le mot 
    cpt_lettre_decouverte=affichage_mot_decouvert(mot_actuel,lettre_dite)
    #On regarde si on n'a pas découvert de lettre on increment le compteur d'erreur
    if cpt_lettre_decouverte==cpt_tampon :
        nombre_d_erreur+=1
    else : 
        cpt_tampon=cpt_lettre_decouverte
    #On affiche donc le nombre d'erreur possible pour deviner le mot
    if    (nombre_d_essai_max - nombre_d_erreur)!=0 or cpt_lettre_decouverte==len(mot_actuel) :
        print("Il vous reste {} chances pour deviner le mot ".format(nombre_d_essai_max - nombre_d_erreur))

#Affichage de si on a gagner ou pas et avec le nombre d'erreur restante si on a gagne       
if (nombre_d_erreur>=nombre_d_essai_max):
    print("Vous avez perdu , le mot a deviner était : {}".format(mot_actuel))
elif (cpt_lettre_decouverte==len(mot_actuel)):
    print ("Bravo vous avez gagne , vous avez deviner le mot il vous restait {} essais".format(nombre_d_essai_max - nombre_d_erreur))
#On regarde si le fichier existe si il existe on regarde s'il est vide ou non afin de savoir s'il y a deja des resultats
if os.path.exists(nom_fichier)  :
    test_fichier_vide=os.path.getsize(nom_fichier) == 0
else : 
    test_fichier_vide=True
#Si le fichier est vide ou qu'il n'est pas cree on va creer le dictionnaire 
if test_fichier_vide :
    
        score={nom_utilisateur:nombre_d_essai_max - nombre_d_erreur}
#Si le fichier contient deja un dictionnaire on va recuperer le score et le modifier en fct des cas possible
else :
    with open(nom_fichier, 'rb') as fichier: 
        mon_depickler = pickle.Unpickler(fichier)
        score = mon_depickler.load()
        #Si l'utilisteur existe deja on lui ajoute son score actuel avec ses anciens scores
        if nom_utilisateur in score.keys() :
            score[nom_utilisateur]+=nombre_d_essai_max - nombre_d_erreur
        #S'il n'existe pas on va le créer
        else : 
            score[nom_utilisateur]=nombre_d_essai_max - nombre_d_erreur



#On envoie le score dans le fichier et on l'affiche au joueur
with open(nom_fichier, 'wb') as fichier: 
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)
    print("Score actuel :")
    print(score)

    
    
    
    
    
    
    