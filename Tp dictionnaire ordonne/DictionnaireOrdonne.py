# coding=utf-8
#Programme permettant la réalisation d'une classe de dictionnaire ordonne

from operator import attrgetter
from typing import Dict


class DictionnaireOrdonne() :
    """Classe permettant de réaliser un dictionnaire que l'on peut trier avec une valeur
    """

    def __init__(self,dictionnaire={}):
        self.cles=[]
        self.valeur=[]



    def __setitem__(self,cle,valeur):
        """Fonction permettant de definit une variable du dictionnaire par dico[cle]=valeur"""
        if cle in self.cles :
            index=self.cles.index(cle)
            self.valeur[index]=valeur
        else :
            self.cles.append(cle)
            self.valeur.append(valeur)

    def __getitem__(self,cle) :
        """Fonction permettant d'obtenir la valeur contenu avec le mot cle donc dico[cle] et none si la cle n'existe pas """
        #Dans cette fonction si la cle rentre n'existe pas on renvoie none
        if cle in self.cles :
            index=self.cles.index(cle)
            return self.valeur[index]
        return None

    def __delitem__(self,cle):
        """Fonction permettant de detruire une cle donne"""
        if cle in self.cles :
            index=self.cles.index(cle)
            del self.cles[index]
            del self.valeur[index]

    def __contains__(self, cle):
        """Fonction permettant de savoir si la cle est presente dans la liste de cle defini"""
        return cle in self.cles 

        

    def __len__(self) :
        return len(self.cles)

    def __repr__(self) :
        """Fonction permettant de redefinir l'affichage de l'objet avec print"""
        chaine= "{"
        for i in range (len(self.cles)-1) :
            chaine+="'{}': {},".format(self.cles[i],self.valeur[i])
        chaine+="'{}': {}".format(self.cles[-1],self.valeur[-1])
        chaine+="}"
        return chaine
    
    def sort(self):
        """Fonction permettant de trier le dictionnaire par rapport a la liste des valeurs"""
        liste_cle_triee=sorted(self.cles)
        valeur=[]
        for cle in liste_cle_triee:
            index=self.cles.index(cle)
            valeur.append(self.valeur[index])
        self.cles=liste_cle_triee
        self.valeur=valeur

    def reverse(self):
        """Fonction permettant d'inverser le dictionnaire"""
        cles=[]
        valeurs=[]
        length=len(self.cles)
        for i in range (length):
            cles.append(self.cles[length-i-1])
            valeurs.append(self.valeur[length-i-1])
        self.cles=cles
        self.valeur=valeurs


    def __iter__(self) : 
        """Fonction permettant l'acces lorsque on utilise for i in dictionnaire"""
        return(iter(self.cles))

    def keys(self):
        """Fonction retournant les cles du dictionnaire"""
        return((self.cles))

    def values(self):
        """Fonction retournant les valeurs du dictionnaire"""
        return(self.valeur)

    def items(self): 
        """Fonction retournant une liste de tuple contenant les valeurs et les cles"""
        list=[]
        for i in range(len(self.cles)):
            list.append((self.cles[i],self.valeur[i]))
        return(list)

    def __add__(self,dictionnaire):
        nouveau=DictionnaireOrdonne()
        for cle in self.cles :
            nouveau.cles.append(cle)
        for valeur in self.valeur :
            nouveau.valeur.append(valeur)

        for i in range (len(dictionnaire)) :
            if dictionnaire.cles[i] not in self.cles :
                nouveau.cles.append(dictionnaire.cles[i])
                nouveau.valeur.append(dictionnaire.valeur[i])
        return nouveau

    

if __name__=="__main__" :
    fruits=DictionnaireOrdonne()
    fruits["pomme"] = 52
    fruits["poire"] = 34
    fruits["prune"] = 128
    fruits["melon"] = 15
    fruits["melon"] = 23
    print(fruits)
    print(fruits["pomme"])
    del fruits["poire"]
    print(fruits)
    print("pomme" in fruits)
    print(len(fruits))
    for cle in fruits :
        print(cle)
    print(fruits.keys())
    print(fruits.values())
    print(fruits.items())
    for nom, qtt in fruits.items():
        print("{0} ({1})".format(nom, qtt))

    legumes = DictionnaireOrdonne()
    legumes["carotte"] = 26
    legumes["haricot"]  = 48
    fruits=fruits+legumes
    print(fruits)
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)



