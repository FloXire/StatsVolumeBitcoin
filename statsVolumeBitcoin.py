import json
import math
import matplotlib.pyplot as plt
import numpy as np
from operationsLoiNormale import *

class Volume:

    def __init__(self):
        file = open("data.JSON", 'r')
        dataVol = json.load(file)
        self.dataVol = dataVol[::-1] # on inverse la liste pour avoir les dates les plus anciennes d'abord
        self.dataSort = sorted(self.dataVol, key = lambda x:x[1]) # tri croissant en fonction du volume
        self.nbVal = len(self.dataSort)

        self.x = [self.dataVol[i][0] for i in range(self.nbVal)]
        self.y = [self.dataVol[j][1] for j in range(self.nbVal)]

        self.moyenne = self.moyenne()
        self.mediane = self.mediane()
        self.quartiles = self.quartiles()
        self.etendue = self.etendue()
        self.min = self.min()
        self.max = self.max()
        self.variance = self.variance()
        self.ecartType = math.sqrt(self.variance)

    def moyenne(self):
        moy = 0
        for i in range(self.nbVal):
            moy += self.dataSort[i][1]

        return int(moy*100/self.nbVal)/100 # troncature à deux décimales

    def mediane(self):
        ind = (self.nbVal+1)/2
        # si nombre pair de valeur, alors la médiane est la moyenne des deux valeurs centrales
        if ind == int(ind):
            med = (self.dataSort[int(ind)-1][1] + self.dataSort[int(ind)][1])/2
        # si nombre impair de valeur, alors la médiane est la valeur centrale
        else:
            med = self.dataSort[int(ind)]

        return med

    def quartiles(self):
        # premier quartile
        indInit = self.nbVal/4
        if indInit == int(indInit):
            premierQ = self.dataSort[int(indInit)][1]
        else:
            premierQ = self.dataSort[int(indInit)+1][1]

        # troisieme quartile
        indInit = 3*indInit
        if indInit == int(indInit):
            troisiemeQ = self.dataSort[int(indInit)][1]
        else:
            troisiemeQ = self.dataSort[int(indInit)+1][1]

        return (premierQ, troisiemeQ)

    def etendue(self):
        return self.dataSort[-1][1] - self.dataSort[0][1]

    def min(self):
        return self.dataSort[0][1]

    def max(self):
        return self.dataSort[-1][1]

    def variance(self):
        var = 0
        for i in range(self.nbVal):
            var += (self.dataVol[i][1]-self.moyenne)**2

        return var/self.nbVal

    def infoDistrib(self):

        """Retourne les effectifs observes dans chaque catégorie et les valeurs de ces catégories"""

        n, bins, patches = plt.hist(self.y)
        plt.close('all')
        # retour sous forme de liste pour pouvoir travailler sur ces listes (concaténation de liste notamment)
        return (n.tolist(), bins.tolist())

    def chi2(self):

        """Test d'ajustement à une loi normale"""

        def calcDist(obs, att):
            # calcule la distance entre effectifs attendus et effectifs observés
            sommeDist = 0
            for i in range(len(att)):
                sommeDist += ((obs[i]-att[i])**2)/att[i]
            return sommeDist

        effectifObs, categories = self.infoDistrib()
        nbCategories = len(effectifObs)

        effectifsTh = [0]*nbCategories
        for i in range(nbCategories):
            effectifsTh[i] = calcProba(categories[i+1], categories[i], self.moyenne, self.ecartType) * self.nbVal

        # Ajout des deux valeurs observées extrêmes, égales à 0
        effectifObs = [0]+effectifObs+[0]
        # Ajout de la valeur théorique pour la catégorie allant de -inf à categories[0], on considère qu'on a 100% des valeurs dans l'intervalle [mu-10*sigma ; mu+10*sigma]
        effectifsTh.insert(0, calcProba(categories[0], self.moyenne-10*self.ecartType, self.moyenne, self.ecartType) * self.nbVal)
        # Ajout de la valeur théorique pour la catégorie allant de categories[-1] à +inf, il s'agit en fait du nombre total de valeur auquel on soustrait la somme des effectifs précédemment calculés
        effectifsTh.append(self.nbVal - sum(effectifsTh))

        T = calcDist(effectifObs, effectifsTh)
        degLbte = self.nbVal - 3 # -3 car -2 (mu et sigma) et -1

        print(
        """
        Résultats du test d'adéquation du X²
        Distance totale entre les effectifs attendus et les effectifs observés si la distribution suit une loi normale : {}
        Nombre de degrés de liberté : {}
        """.format(T, degLbte)
        )

        return (T, degLbte)

    def showDailyGraph(self):

        plt.close('all')
        fig, ax = plt.subplots()
        fig.autofmt_xdate()

        plt.title('Volume journalier entre le 28/11/2018 et le 28/12/2018')
        plt.xlabel('Date (jour/mois)')
        plt.ylabel('Volume')

        ax.plot(self.y, 'rx')
        plt.xticks(range(self.nbVal), self.x)

        print(self.y)

        plt.show()
        return

    def showHist(self):
        plt.title(r'Histogramme du volume : $\mu={}$, $\sigma={}$'.format("{:.3E}".format(int(self.moyenne)), "{:.3E}".format(int(self.ecartType))))
        n, bins, patches = plt.hist(self.y, facecolor='#ff7400', alpha=0.8)

        x = np.linspace(self.moyenne - 3*self.ecartType, self.moyenne + 3*self.ecartType, 100)
        y = densiteLoiNormale(x, self.moyenne, self.ecartType)

        # remise à l'échelle de la loi normale ayant les même paramètres (moyenne et écart type) que la distribution pour pouvoir les comparer à vue d'oeil
        for i in range(len(x)):
            y[i] *= self.moyenne*3.2

        plt.plot(x, y, 'r--', alpha=0.8)
        plt.show()

        return

    def getInfo(self):

        print(
        """
        Moyenne : {}
        Mediane : {}
        Quartile 1: {}
        Quartile 3 : {}
        Etendue : {}
        Minimum : {}
        Maximum : {}
        Variance : {}
        Ecart-type : {}
        """.format(self.moyenne, self.mediane, self.quartiles[0], self.quartiles[1], self.etendue, self.min, self.max, self.variance, int(self.ecartType))
        )

        return {"Moyenne" : self.moyenne,
                "Mediane" : self.mediane,
                "Quartile 1": self.quartiles[0],
                "Quartile 3" : self.quartiles[1],
                "Etendue" : self.etendue,
                "Minimum" : self.min,
                "Maximum" : self.max,
                "Variance" : self.variance,
                "Ecart-type" : int(self.ecartType)}
