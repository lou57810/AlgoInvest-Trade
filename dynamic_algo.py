from action import Action
import csv
from algo import Algo



class Dynalgo(Algo):
    

    def __init__(self, file, max_price):
        super().__init__(file, max_price)
	
    def algo_generic(self):
        data = super().get_datas(self.file)            # tableau des actions avec prix et benefices non tri�s  
        self.dynamic_algo(data, self.max_price)

    def dynamic_algo(self, data, max_price):        
        matrice = [[0 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # Initialisation de la matrice � 0/x et 0/y
        # liste action en x et poids/valeurs en y
        for i in range(1, len(data) + 1):               # parcours des y actions
            for w in range(1, max_price + 1):           # parcours des prix par n�action            
                if int(data[i - 1].price) <= w:         # prix action pr�c�dente                
                    matrice[i][w] = max(data[i - 1].benefit + matrice[i - 1][int(w - data[i - 1].price)], matrice[i - 1][w])
                    print('mat:', data[i - 1].benefit)
                    # max(a,b) retourne le plus grand
                else:
                    matrice[i][w] = matrice[i - 1][w]               
    
        w = max_price
        n = len(data)               # nombre d'objets (actions)
        actions_selection = []

        while w >= 0 and n >= 0:    # recup�ration des donn�es finales
            e = data[n - 1]            
            if matrice[n][w] == matrice[n - 1][w - int(e.price)] + float(e.benefit):
                actions_selection.append(e)
                w -= int(e.price)        
            n -= 1
        super().display_algo_data(actions_selection)    
        return matrice[-1][-1], actions_selection
