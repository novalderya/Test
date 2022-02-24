# coding=utf-8

class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self,valeur):
        """Fonction permettant l'addition de deux duree ou d'une duree et d'un entier"""
        #on va regarder si on ajoute un entier
        Duree_Tampon=Duree()
        #On va considerez l'entier comme etant des secondes entre par l'utilisateur et on definit une duree a partir de ca
        if type(valeur)==int :
            valeur=Duree(valeur//60,valeur%60)

        #On additionne les deux valeurs des secondes et si on depasse 60 secondes on fait un modulo 60 et on retient une minute
        Duree_Tampon.sec =self.sec+valeur.sec
        if Duree_Tampon.sec>=60 :
            Duree_Tampon.sec%=60
            Duree_Tampon.min =self.min+valeur.min +1 
        else : 
            Duree_Tampon.min = self.min+ valeur.min
        if Duree_Tampon.min >=60:
            Duree_Tampon.min%=60
        print("fonction add")
        return Duree_Tampon

    
    def __radd__(self,valeur):
        """Fonction permettant de faire l'addition d'un entier et d'une duree dans le sens suivant
        int + entier """
        return self+valeur


    def __iadd__(self,valeur):
        """Fonction permettant de réaliser l'opération += sur deux durees ou une duree et un entier"""
        #on va regarder si on ajoute un entier
        Duree_Tampon=Duree()
        #On va considerez l'entier comme etant des secondes entre par l'utilisateur et on definit une duree a partir de ca
        if type(valeur)==int :
            valeur=Duree(valeur//60,valeur%60)

        #On additionne les deux valeurs des secondes et si on depasse 60 secondes on fait un modulo 60 et on retient une minute
        Duree_Tampon.sec =self.sec+valeur.sec
        if Duree_Tampon.sec>=60 :
            Duree_Tampon.sec%=60
            Duree_Tampon.min =self.min+valeur.min +1 
        else : 
            Duree_Tampon.min = self.min+ valeur.min
        if Duree_Tampon.min >=60:
            Duree_Tampon.min%=60
        print("fonction iadd")
        return Duree_Tampon
    
    def __lt__(self,valeur):
        """Fonction permettant de faire la comparaison < entre deux dureee"""
        #On compare dans un premier temps les minutes et si elles sont égales on va comparer les secondes
        if self.min<valeur.min :
            return True 
        elif self.min>valeur.min :
            return False
        else :
            if self.sec <valeur.sec :
                return True 
            else :
                return False


if __name__== "__main__" :
    duree=Duree(3,5)
    print(duree)
    duree2=Duree(3,56)
    print(duree+duree2)
    duree3=Duree(3,53)
    print(duree+duree3)
    print(duree+600)
    print(600+duree)
    duree+=2444
    print(duree)
    print(duree3<duree2)