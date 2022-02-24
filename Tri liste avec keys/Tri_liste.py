# coding=utf-8

from operator import attrgetter, itemgetter


class Etudiant :


    def __init__(self,nom,age,moyenne) :
        self.nom=nom
        self.moyenne=moyenne
        self.age=age

    def __repr__(self) -> str:
        return "<Nom : {}, âge : {}, moyenne : {}>".format(self.nom,self.age,self.moyenne)


if __name__=="__main__" :
    print("Test tri sur liste :")
    etudiants = [
        ("Clément", 14, 16),
        ("Charles", 12, 15),
        ("Oriane", 14, 18),
        ("Thomas", 11, 12),
        ("Damien", 16, 15),
    ]
    #Tri de la liste par rapport a leur premiere colonne
    print(sorted(etudiants))
    #Tri de la liste par rapport a leur troisieme colonne
    print(sorted(etudiants, key = lambda colonnes : colonnes[2]))
    #Tri de la liste avec itemgetter
    print(sorted(etudiants,key = itemgetter(2)))

    print("Test tri sur classe :")
    etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
    ]
    print(etudiants)
    #On trie les étudiants par rapport a leur moyenne
    print(sorted(etudiants, key=lambda etudiant:etudiant.moyenne ))
    #On trie les étudiants par rapport a leur moyenne inversé
    print(sorted(etudiants, key=lambda etudiant:etudiant.moyenne , reverse=True))
    print("test attregetter")
    print(sorted(etudiants,key=attrgetter("age","moyenne")))

