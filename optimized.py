from action import Action
from algo import Algo
import csv


class Optidynalgo(Algo):

	
    def __init__(self, file, max_price):
        super().__init__(file, max_price)
        self.file = file
        self.max_price = max_price

    def algo_generic(self):        
        data = super().get_datas(self.file)            # tableau des actions avec prix et benefices non triés
        self.dynamic_algo(data, self.max_price)        
    
    def dynamic_algo(self, data, max_price):        
        
        matrice = [[1 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # Initialisation de la matrice à 0/x et 0/y
        # liste action en x et poids/valeurs en y
        for i in range(1, len(data) + 1):               # parcours des y actions            
            for w in range(1, max_price + 1):           # parcours des prix     # w=  1-->501            
                if float(data[i - 1].price) <= w:         # si prix précédent < prix actuel < max_price                    
                    matrice[i][w] = max(data[i - 1].benefit + matrice[i - 1][int(w - data[i - 1].price)], matrice[i - 1][w])                    
                else:                
                    matrice[i][w] = matrice[i - 1][w]
    
        
        w = max_price
        n = len(data)               # nombre d'objets (actions)
        actions_selection = []

        while w >= 0 and n >= 0:    # recupération des données finales
            e = data[n - 1]            
            if matrice[n][w] == matrice[n - 1][int(w - float(e.price))] + float(e.benefit):
                actions_selection.append(e)            
                w -= round(float(float(e.price)))
            n -= 1
        #print('action_selection:', actions_selection)
        super().display_algo_data(actions_selection)    
        #return matrice[-1][-1], actions_selection

