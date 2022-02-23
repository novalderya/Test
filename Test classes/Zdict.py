# coding=utf-8

class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        
        return self._dictionnaire[index]

    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        self._dictionnaire[index] = valeur

    def __repr__(self):
        """Methode permettant de changer l'affichage lorsqu'on tape que le nom de l'objet defini"""
        chaine_carc="{"
        for i,elt in self._dictionnaire.items(): 
            chaine_carc+="({},{})".format(i,elt)
        chaine_carc+="}"
        return chaine_carc

    def __str__(self): 
        """Methode permettant de changer la conversion en str"""
        chaine_carc="{"
        for i,elt in self._dictionnaire.items(): 
            chaine_carc+="({},{})".format(i,elt)
        chaine_carc+="}"
        return chaine_carc

    def __getattr__(self,nom) :
        """Methode etant appelle lorsque l'on appelle un attribut qui n'existe pas """
        print("Il n'existe pas d'attribut possedant ce nom {} pour cette classe".format(nom)) 

    def __delitem__(self,index):
        """Fonction permettant de detruire un index precis"""
        del self._dictionnaire[index]

if __name__=="__main__" :
    dictionnair=ZDict()
    dictionnair[1]="test"
    print(dictionnair[1])
    dictionnair.__setitem__(7,"test 2")
    print(dictionnair)
    chaine=str(dictionnair)
    print(chaine)
    dictionnair.test
    del dictionnair[1]
    print(dictionnair)