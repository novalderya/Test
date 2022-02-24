# coding=utf-8
#Programme utiliser pour faire des test sur les classes 
#Toutes les fonctions auront des print qui affiche la fonction qui est utilisé afin de comprendre quelle fonction est appele
from math import ceil

#Classe mere du programme
class Humain():
    """classe permettant de definir un etre humain"""

    def __init__(self,_classe,prenom,vie=10,stamina=10,attaque=3):
        self.prenom=prenom
        self.vie=vie
        self.stamina=stamina
        self.attaque=attaque
        self._classe=_classe
        print("Init classe humain")
    
    def _get_classe(self):
        return self._classe
    #Test sur classe car elle ne doit pas etre modifie de l'exterieur car elle est fixe au personnage a sa définition
    classe=property(_get_classe)

    def attaque_perso(self,Perso) :
        """Fonction permettant a un personnage d'attaquer un autre ce qui lui coutent de la stamina"""
        if type(Perso)==Guerrier :
            Perso.vie-=self.attaque - Perso.armure
        else :
            Perso.vie-=self.attaque

        self.stamina-=2
        print("attaque classe humain")


    def repos(self):
        """Fonction permettant de regagner de la stamina"""
        self.stamina+=2
        print("repos classe humain")

    def __repr__(self):
        """Fonction gérant l'affichage avec print"""
        print("affichage classe humain")
        return "{} le {} posséde {} de vie , {} de stamina , {} d'attaque.".format(self.prenom,self._classe,self.vie,self.stamina,self.attaque)
        


class  Paysan(Humain):
    """Classe permettant de definir un paysan"""  
    def __init__(self, prenom, vie=10, stamina=10, attaque=3):
        Humain.__init__(self,"paysan",prenom, vie, stamina, attaque)
        print("Init classe  paysan")

class Sorcier(Humain) :
    """classe permettant de definit un sorcier qui herite donc d'un etre humain et qui possede du mana """
    
    def __init__(self,prenom,vie=7,stamina=7,attaque=2,mana=15):
        #initialisation comme un humain avec du mana en plus
        Humain.__init__(self,"sorcier",prenom,vie,stamina,attaque)
        self.mana=mana
        print("Init classe Sorcier")
    
    def repos(self):
        Humain.repos(self)
        self.mana+=3
        print("repos classe sorcier")

    def __repr__(self):
        """Fonction gérant l'affichage avec print"""
        print("affichage classe sorcier")
        return "{} le {} posséde {} de vie , {} de stamina , {} d'attaque , {} de mana.".format(self.prenom,self._classe,self.vie,self.stamina,self.attaque,self.mana)

        

class Guerrier(Humain):
    """classe permettant de definir un guerrier qui possede de l'armure """
    #initialisation comme un humain mais avec de l'armure en plus
    def __init__(self,prenom,vie=14,stamina=14,attaque=4,armure=2) :
        Humain.__init__(self,"guerrier",prenom,vie,stamina,attaque)
        self.armure=armure
        print("Init classe guerrier")

    def coup_puissant(self,Perso):
        """Methode d'attaque specifique au guerrier"""
        if type(Perso)==Guerrier :
            Perso.vie-=self.attaque - ceil(Perso.armure/2)
        else :
            Perso.vie-=self.attaque

        self.stamina-=2
        print("Coup classe guerrier")

    def __repr__(self):
        """Fonction gérant l'affichage avec print"""
        print("affichage classe sorcier")
        return "{} le {} posséde {} de vie , {} de stamina , {} d'attaque , {} d'armure.".format(self.prenom,self._classe,self.vie,self.stamina,self.attaque,self.armure)

    def repos(self):
        self.stamina+=3
        print("Repos classe guerrier")


#test dde double heritage de classe
class double_heritage(Sorcier,Guerrier): 
    """Classe permettant de faire des test sur l'héritage multiple en héritant de sorcier et guerrier"""
    def __init__(self, prenom, vie=7, stamina=7, attaque=2, mana=10):
        Sorcier.__init__(self,prenom, vie, stamina, attaque, mana)
        print("Initialisation classe double heritage")

#Test heritage d'heritage
class SorcierFeu(Sorcier):
    def __init__(self, prenom, vie=6, stamina=6, attaque=2, mana=18):
        Sorcier.__init__(self,prenom, vie, stamina, attaque, mana)
        self.type="feu"
        print("Initialisation sorcier de feu")

    def __repr__(self):
        print("affichage classe sorcier de feu")
        return "{} le {} de {} posséde {} de vie , {} de stamina , {} d'attaque , {} de mana.".format(self.prenom,self._classe,self.type,self.vie,self.stamina,self.attaque,self.mana)

      

if __name__=="__main__" :
    #-----------------------------Test initialisation -------------------------

    print("Test initialisation")
    Jacques=Paysan("Jacques")
    Hubert=Guerrier("Hubert")
    Robert=Sorcier("Robert")
    
    #---------------------------------Test affichage-------------------------------

    print("Test affichage")
    print(Jacques)
    print(Hubert)
    print(Robert)

    #--------------------------------Test repos-------------------------------------
    
    print("Test repos")
    Jacques.repos()
    Hubert.repos()
    Robert.repos()
    Robert.attaque_perso(Jacques)

    #--------------------------------Test double heritage---------------------------

    print("Test double heritage")
    Alban=double_heritage("Alban")
    Alban.repos()
    Alban.coup_puissant(Robert)
    print(Alban)

    #-----------------------------test heritage de heritage------------------------------
    print("Test heritage de heritage")
    Gerard=SorcierFeu("Gerard")
    Gerard.repos()
    print(Gerard)
    Gerard.attaque
    


