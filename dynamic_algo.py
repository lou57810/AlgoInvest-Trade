from action import Action
import csv
from algo import Algo
from utils import get_datas, display_algo_data


class Dynalgo(Algo):

	
    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price

    #def dynamic_algo_execute(self, file):
    def algo_generic(self):
        data = get_datas(self.file)            # tableau des actions avec prix et benefices non triés  
        self.dynamic_algo(data, self.max_price)

    def dynamic_algo(self, data, max_price):
        from utils import display_algo_data
        matrice = [[0 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # Initialisation de la matrice à 0/x et 0/y
        # liste action en x et poids/valeurs en y
        for i in range(1, len(data) + 1):               # parcours des y actions
            for w in range(1, max_price + 1):           # parcours des prix par n°action            
            
                if int(int(data[i - 1].price) / 100) <= w:         # prix action précédente                
                    matrice[i][w] = max(int(int(data[i - 1].benefit) / 100) + matrice[i - 1][w - int(int(data[i - 1].price) / 100)], matrice[i - 1][w])
                    # max(a,b) retourne le plus grand
                else:
                    matrice[i][w] = matrice[i - 1][w]               
    
        w = max_price
        n = len(data)               # nombre d'objets (actions)
        actions_selection = []

        while w >= 0 and n >= 0:    # recupération des données finales
            e = data[n - 1]        
            if matrice[n][w] == matrice[n - 1][w - int(int(e.price) / 100)] + int(int(e.benefit) / 100):
                actions_selection.append(e)
                w -= int(int(e.price) / 100)        
            n -= 1
        display_algo_data(actions_selection)    
        return matrice[-1][-1], actions_selection
