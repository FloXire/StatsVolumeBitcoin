import json
import math
import matplotlib.pyplot as plt
import numpy as np

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

        """Retourne les effectifs observes"""

        n, bins, patches = plt.hist(self.y)
        plt.close('all')
        return (n, bins)

    def chi2(self):

        """Test d'ajustement à une loi normale"""

        effectifObs, categories = self.infoDistrib()

        return

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
        y = ""

        # remise à l'échelle de la loi normale ayant les même paramètres (moyenne et écart type) que la distribution
        for i in range(100):
            y[i] *= self.moyenne*3.5

        plt.plot(x, y, 'r--', alpha=0.8)

        plt.show()

        return

    def getInfo(self):
        return {"Moyenne" : self.moyenne,
                "Mediane" : self.mediane,
                "Quartile 1": self.quartiles[0],
                "Quartile 3" : self.quartiles[1],
                "Etendue" : self.etendue,
                "Minimum" : self.min,
                "Maximum" : self.max,
                "Variance" : self.variance,
                "Ecart-type" : int(self.ecartType)}

vol = Volume()
vol.showHist()
