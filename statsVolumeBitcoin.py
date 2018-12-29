import json
import math

class Volume:

    def __init__(self):
        file = open("data.JSON", 'r')
        dataVol = json.load(file)
        self.dataVol = dataVol[::-1] # on inverse la liste pour avoir les dates les plus anciennes d'abord
        self.dataSort = sorted(self.dataVol, key = lambda x:x[1]) # tri croissant en fonction du volume
        self.nbVal = len(self.dataSort)

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
print(vol.getInfo())
