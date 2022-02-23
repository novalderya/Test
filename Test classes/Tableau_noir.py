# coding=utf-8
#Programme pour faire des test sur les classes

class tableau_noir: 

    """Classe permettant de simuler un tableau noir sur lequel on peut ecrire effacer  """

    def __init__(self) :
        """Fonction permettant l'initialisation d'un tableau il commence vide"""
        self.contenu=""

    def ecrire(self,message):
        """Fonction permettant d'ecrire sur le tableau"""
        if self.contenu!="":
            self.contenu+='\n'
        self.contenu+=message

    def lire(self):
        """Fonction permettant d'afficher ce qui est écrit sur le tableau"""
        print(self.contenu)

    def effacer(self) :
        self.contenu=""

if __name__== "__main__" :
    tableau=tableau_noir()
    tableau.ecrire("Test ecriture tableau")
    tableau.ecrire("Test nouvelle ligne")
    tableau.lire()
    tableau.effacer()
    tableau.lire()
    tableau.ecrire("Ecrire apres effacer")
    tableau.lire()

