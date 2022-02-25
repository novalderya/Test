# coding=utf-8
#Programme pour realiser des test sur les flux standard

import sys

if __name__=="__main__":

    sys.stdout.write("un test\n")
    sys.stdout.write("un test\n")

    fichier = open('Programmation systeme//sortie.txt', 'w')   
    sys.stdout = fichier
    print("Quelque chose...")

    sys.stdout = sys.__stdout__
    print("Ceci est un test")







