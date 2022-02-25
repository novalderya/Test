# coding=utf-8
#Programme permettant la réalisation d'une classe de dictionnaire ordonne

from operator import attrgetter
from typing import Dict


class DictionnaireOrdonne() :
    """Classe permettant de réaliser un dictionnaire que l'on peut trier avec une valeur
    """
    #Ajout de la possibilite de creer avec en entree des valeurs ou un autre dictionnaire
    def __init__(self,base={},**dictionnaire):
        self.cles=[]
        self.valeur=[]
        for i,elt in dictionnaire.items() :
            self.cles.append(i)
            self.valeur.append(elt)
        if type(base) in (dict, DictionnaireOrdonne) :
            for cle in base :
                #Methode plus rapide pour assigner les valeurs 
                self[cle]=base[cle]


    def __setitem__(self,cle,valeur):
        """Fonction permettant de définir une variable du dictionnaire par dico[cle]=valeur"""
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
        #rajout d'une exception pour traiter le cas ou la cle donner n'existe pas 
        else : 
            raise KeyError("La clé demandé n'existe pas dans ce dictionnaire")


    def __delitem__(self,cle):
        """Fonction permettant de detruire une cle donne"""
        if cle in self.cles :
            index=self.cles.index(cle)
            del self.cles[index]
            del self.valeur[index]
             #rajout d'une exception pour traiter le cas ou la cle donner n'existe pas 
        else : 
            raise KeyError("La clé demande n'existe pas dans ce dictionnaire")

    def __contains__(self, cle):
        """Fonction permettant de savoir si la cle est presente dans la liste de cle defini"""
        return cle in self.cles 

        

    def __len__(self) :
        """Fonction renvoyant la longueur du dictionnaire"""
        return len(self.cles)

    def __repr__(self) :
        """Fonction permettant de redefinir l'affichage de l'objet avec print"""
        chaine= "{"
        for i in range (len(self.cles)-1) :
            chaine+="'{}': {},".format(self.cles[i],self.valeur[i])
        chaine+="'{}': {}".format(self.cles[-1],self.valeur[-1])
        chaine+="}"
        return chaine

    #Ajout de str que je n'avais pas défini 
    def __str__(self):
        """Fonction appelée quand on souhaite afficher le dictionnaire grâce
        à la fonction 'print' ou le convertir en chaîne grâce au constructeur
        'str'. On redirige sur __repr__"""
        
        return repr(self)
    
    def sort(self):
        """Fonction permettant de trier le dictionnaire par rapport a la liste des valeurs"""
        liste_cle_triee=sorted(self.cles)
        valeur=[]
        for cle in liste_cle_triee:
            index=self.cles.index(cle)
            valeur.append(self.valeur[index])
        self.cles=liste_cle_triee
        self.valeur=valeur
    #Ma version 
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

    # #version propose par la correction 
    # def reverse(self):
    #     """Inversion du dictionnaire"""
    #     # On crée deux listes vides qui contiendront le nouvel ordre des clés
    #     # et valeurs
    #     cles = []
    #     valeurs = []
    #     for cle, valeur in self.items():
    #         # On ajoute les clés et valeurs au début de la liste
    #         cles.insert(0, cle)
    #         valeurs.insert(0, valeur)
    #     # On met ensuite à jour nos listes
    #     self._cles = cles
    #     self._valeurs = valeurs

    def __iter__(self) : 
        """Fonction permettant l'acces lorsque on utilise for i in dictionnaire"""
        return(iter(self.cles))

    def keys(self):
        """Fonction retournant les cles du dictionnaire"""
        return((self.cles))

    def values(self):
        """Fonction retournant les valeurs du dictionnaire"""
        return(self.valeur)

    #Ma version
    def items(self): 
        """Fonction retournant une liste de tuple contenant les valeurs et les cles"""
        list=[]
        for i in range(len(self.cles)):
            list.append((self.cles[i],self.valeur[i]))
        return(list)
    # #Autre version possible , correction 
    # def items(self):
    #     """Renvoie un générateur contenant les couples (cle, valeur)"""
    #     for i, cle in enumerate(self._cles):
    #         valeur = self._valeurs[i]
    #         yield (cle, valeur)
    

    def __add__(self,dictionnaire):
        """Fonction permettant d'ajouter deux dictionnaires entre eux"""
        #Rajout d'une verification de type avant l'addition et on indique le problème rencontré
        if type(dictionnaire) is not type(self):
            raise TypeError( \
                "Impossible de concaténer {0} et {1}".format( \
                type(self), type(dictionnaire)))
        else:
            nouveau=DictionnaireOrdonne()
            # for cle in self.cles :
            #     nouveau.cles.append(cle)
            # for valeur in self.valeur :
            #     nouveau.valeur.append(valeur)
            
            #Moins de ligne de code pour la même opérations
            for cle in self.cles :
                nouveau[cle]=self[cle]

            for i in range (len(dictionnaire)) :
                #On regarde si la cle du deuxieme dictionnaire n'est pas dans le premier
                if dictionnaire.cles[i] not in self.cles :
                    nouveau.cles.append(dictionnaire.cles[i])
                    nouveau.valeur.append(dictionnaire.valeur[i])
                #Si la cle est présente on va addittionner la valeur des deux dictionnaires
                else :
                    nouveau.valeur[i]+=dictionnaire.valeur[i]
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

    test_creation_liste= DictionnaireOrdonne(carrote = 26, haricot = 23)
    print(test_creation_liste)
    test_creation_dictionnaire= DictionnaireOrdonne(test_creation_liste)
    print(test_creation_dictionnaire)




