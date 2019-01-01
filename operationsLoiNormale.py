"""Module contenant des opérations liées à la loi normale"""

import numpy as np

def densiteLoiNormale(x, mu, sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*(np.e**((-1/2)*(((x-mu)/sigma)**2)))

def probaNormCentreeReduite(x):

    """Calcul de la fonction F(x) de la loi normale centrée réduite"""

    # on utilise le fait que F(x) = 1-F(-x)

    if x == 0:
        return 0.5

    u = abs(x)
    # nombre de rectangles, on en veut à peu près un tous les 0.0001 en abscisse
    n = int(u/0.0001)
    # largeur d'un rectangle (pas exactement égal à 0.0001 car on a un nombre entier de rectangles)
    du = u/n

    integrale = 0
    for i in range(n):
        """
        On moyenne l'erreur pour ne pas avoir d'intégrales > 1 ou < 0.
        En effet si on prend à chaque incrémentation une hauteur du rectangle qui vaut i*du alors on ne prend que des rectangles qui surestiment légèrement l'aire.
        En alternant une fois sur deux rectangle qui surestime et rectangle qui sous estime l'aire, alors cette erreur s'annuleself.
        """
        if i%2 == 0:
            ord = i*du
        else:
            ord = (i+1)*du

        integrale += densiteLoiNormale(ord,0,1)

    # on multiplie le tout par du ce qui équivaut à multiplier chaque terme de la somme par du
    integrale *= du
    # on part de 0, l'intégrale vaut alors 0.5, on doit donc ajouter 0.5 à l'intégrale obtenue
    integrale += 0.5

    if x<0:
        integrale = 1-integrale

    return integrale

def centreEtReduit(x, mu, sigma):
    return (x-mu)/sigma

def calcProba(a, b, mu, sigma):

    """Renvoie la probabilité d'être entre a et b"""

    borneSup = probaNormCentreeReduite(centreEtReduit(a, mu, sigma))
    borneInf = probaNormCentreeReduite(centreEtReduit(b, mu, sigma))
    return borneSup-borneInf
