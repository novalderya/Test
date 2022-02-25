# coding=utf-8
#Programme réalisant des test sur les expressions réguliéres

import re

def test_num_telephone(str) :
    """Fonction permettant de vérifier si la chaine correspond a un numéro"""
    #On va tester dans un premier temps si l'utilisateur a taper 10 chiffres 
    return (re.search(r"^0[0-9]([-. ]?[0-9]{2}){4}$",str) is not None)

if __name__=="__main__":
    print(re.search(r"abc","abcef"))
    print(re.search(r"abc","absdfld"))
    print(re.search(r"abc*","abdffd"))
    print(re.search(r"abc*","fabccc") is not None)
    print(re.sub(r"1(test)2(3)", r" est un \2 ","ceci1test234"))
    numero=""
    while not test_num_telephone(numero):

        numero=input("Entrez votre numero de telephone :")
    print(numero)





