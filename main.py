from statsVolumeBitcoin import Volume

if __name__ == "__main__":

    donnees = Volume()
    donnees.getInfo()
    donnees.showDailyGraph()
    donnees.showHist()
    donnees.chi2()
