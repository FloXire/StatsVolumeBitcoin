# Statistiques : le volume du bitcoin
_Analyse statistique du volume du bitcoin entre le 28/11/2018 et le 28/12/2018_

La branche master contient le code permettant d'extrapoler à d'autres intervalles de temps. \
La branche OneYearOfData est un test pour voir si oui ou non, lorsque l'on retire les 10% des valeurs les plus fortes, la distribution suit une loi normale au sens du test du X² (ce n'est pas le cas avec ces 10% de valeurs).

Les données ont été récoltées sur coinmarketcap, site référençant notamment le volume d’échange total journalier du bitcoin sur l’ensemble des plateformes d’échange mondial.

Lien utilisé pour extraire les données :
https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20181128&end=20181228

Voici les résultat bruts obtenus après l’analyse :

Volume journalier observé du 2018-11-28 au 2018-12-28 : 
[['28/11', 7280280000], ['29/11', 6503347767], ['30/11', 6048016717], ['01/12', 5375314093], ['02/12', 5262697895], ['03/12', 5089570994], ['04/12', 5028069239], ['05/12', 5302481574], ['06/12', 5878333109], ['07/12', 6835615448], ['08/12', 5305024497], ['09/12', 4947372847], ['10/12', 5020968740], ['11/12', 4696765188], ['12/12', 4139364829], ['13/12', 4343372456], ['14/12', 4372763663], ['15/12', 3551763561], ['16/12', 3744248994], ['17/12', 5409247918], ['18/12', 5911325473], ['19/12', 6810689119], ['20/12', 8927129279], ['21/12', 7206015706], ['22/12', 5605823233], ['23/12', 6151275490], ['24/12', 7240968501], ['25/12', 6158207293], ['26/12', 5326547918], ['27/12', 5130222366], ['28/12', 5631554348]]

        Moyenne : 5620463814.67
        Mediane : 5392281005.5
        Quartile 1: 5028069239
        Quartile 3 : 6503347767
        Etendue : 5375365718
        Minimum : 3551763561
        Maximum : 8927129279
        Variance : 1.2789186677716534e+18
        Ecart-type : 1130892863

Résultats du test d'adéquation du X² : \
Distance totale entre les effectifs attendus et les effectifs observés si la distribution suit une loi normale : 12.949518779230953. \
Nombre de degrés de liberté : 28.
