# coding=utf-8
#Programme utiliser pour faire des test sur les signaux

import signal
import sys

def fermer_programme(signal, frame):
    """Fonction appelée quand vient l'heure de fermer notre programme"""
    print("C'est l'heure de la fermeture !")
    sys.exit(0)

if __name__=="__main__" :
    # Connexion du signal à notre fonction
    signal.signal(signal.SIGINT, fermer_programme)

    # Notre programme...
    print("Le programme va boucler...")
    while True:
        continue







