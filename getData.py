import requests
from bs4 import BeautifulSoup
import json

dateDebut = "20181128"
datefin = "20181228"
url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={}&end={}".format(dateDebut, datefin)
content = requests.get(url).content

soup = BeautifulSoup(content,'html.parser')
table = soup.find('table', {'class': 'table'})
data = [[td.text.strip() for td in tr.findChildren('td')] for tr in table.findChildren('tr')]

data = data[1:] # Le premier élement est un tableau vide

dateEtvOl = [[data[i][0], data[i][5]] for i in range(len(data))]

def formatDate(date):
    mois = date[:3]
    if mois == 'Dec':
        mois = '12'
    elif mois == 'Nov':
        mois = '11'
    elif mois == 'Oct':
        mois = '10'
    elif mois == 'Sep':
        mois = '09'
    elif mois == 'Aug':
        mois = '08'
    elif mois == 'Jul':
        mois = '07'
    elif mois == 'Jun':
        mois = '06'
    elif mois == 'May':
        mois = '05'
    elif mois == 'Apr':
        mois = '04'
    elif mois == 'Mar':
        mois = '03'
    elif mois == 'Feb':
        mois = '02'
    elif mois == 'Jan':
        mois = '01'
    return date[4:6]+'/'+mois

def formatVolume(volume):
    return int(volume.replace(',', ''))

dateEtvOl = [[formatDate(dateEtvOl[j][0]), formatVolume(dateEtvOl[j][1])] for j in range(len(dateEtvOl))]

file = open("data.JSON", 'w')
json.dump(dateEtvOl, file)
file.close()
