# coding=utf-8
#Programme pour faire des test sur les classes

class tableau_noir: 

    """Classe permettant de simuler un tableau noir sur lequel on peut ecrire effacer  """

    def __init__(self) :
        """Fonction permettant l'initialisation d'un tableau il commence vide"""
        self.contenu=""
        self._test_private="apple"
        self._test_private2="computer"

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

    def _get_test_private(self) :
        print("accesseur _test_private")
        return self._test_private

    def _get_test_private2(self) :
        print("accesseur _test_private2")
        return self._test_private2

    def _set_test_private2(self,message):
        print("mutateur _test_private2")
        self._test_private2=message

    test_private=property(_get_test_private)
    test_private2=property(_get_test_private2,_set_test_private2)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""

         
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

if __name__== "__main__" :
    tableau=tableau_noir()
    tableau.ecrire("Test ecriture tableau")
    tableau.ecrire("Test nouvelle ligne")
    tableau.lire()
    tableau.effacer()
    tableau.lire()
    tableau.ecrire("Ecrire apres effacer")
    tableau.lire()
    print(tableau)
    tableau.test
    tableau._get_test_private()
    tableau.test_private
    tableau._set_test_private2("test")
    #tableau.test_private="strawberry"

