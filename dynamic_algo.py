from action import Action
import csv


class Dynalgo:

	
    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price

    def dynamic_algo_execute(self):
        data = self.get_datas(self.file)            # tableau des actions avec prix et benefices non triés  
        self.dynamic_algo(data, self.max_price)

    def dynamic_algo(self, data, max_price):    
        matrice = [[0 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # Initialisation de la matrice à 0/x et 0/y
        # liste action en x et poids/valeurs en y
        for i in range(1, len(data) + 1):               # parcours des y actions
            for w in range(1, max_price + 1):           # parcours des prix par n°action
                if int(data[i - 1].price) <= w:         # prix action précédente
                    matrice[i][w] = max(int(data[i - 1].benefit) + matrice[i - 1][w - int(data[i - 1].price)], matrice[i - 1][w])
                    # max(a,b) retourne le plus grand
                else:
                    matrice[i][w] = matrice[i - 1][w]

        w = max_price
        n = len(data)               # nombre d'objets (actions)
        actions_selection = []

        while w >= 0 and n >= 0:    # recupération des données finales
            e = data[n - 1]
            if matrice[n][w] == matrice[n - 1][w - int(e.price)] + int(e.benefit):
                actions_selection.append(e)
                w -= int(e.price)        
            n -= 1

        self.display_algo_data(actions_selection)
        return matrice[-1][-1], actions_selection

    # ------- Getting datas into array 'data'-------
    def get_datas(self, file):        
        data = []
        with open(self.file, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                action = Action(line[0], line[1], line[2])                
                data.append(action)        
        return data                                  # tableau des actions avec benefices non triés

    def display_algo_data(self, tab):
        somme1 = 0
        somme2 = 0
        for elt in tab:        
            somme1 += int(elt.price)
            somme2 += int(elt.benefit)
            elt.benefit = int(elt.benefit)/100
        print('Actions panel:', tab)
        print('Prix total:', somme1)
        print('Benefice total:', somme2/100)