from action import Action
import csv


class Optidynalgo:

	
    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price

    def dynamic_algo_execute(self, file):
        from utils import get_datas
        data = get_datas(file)            # tableau des actions avec prix et benefices non triés  
        dynamic_algo(data, self.max_price)
        #print('data:', data)
    
def dynamic_algo(data, max_price):
    from utils import display_algo_data
    tab = []
    matrice = [[0 for x in range(max_price + 1)] for x in range(len(data) + 1)]  # Initialisation de la matrice à 0/x et 0/y
    # liste action en x et poids/valeurs en y
    for i in range(1, len(data) + 1):               # parcours des y actions
        for w in range(1, max_price + 1):           # parcours des prix
            if round(int(data[i - 1].price) / 100) <= w:         # si prix précédent < prix actuel < max_price               
                matrice[i][w] = max(round(int(data[i - 1].benefit)/100) + matrice[i - 1][w - round(int(data[i - 1].price)/100)], round(int(matrice[i - 1][w])/100))
                # max(a,b) retourne le plus grand
                
            else:                
                matrice[i][w] = matrice[i - 1][w]
    
    #print('matrice_prix:', matrice[i][w])
    w = max_price
    n = len(data)               # nombre d'objets (actions)
    actions_selection = []

    while w >= 0 and n >= 0:    # recupération des données finales
        e = data[n - 1]        
        if matrice[n][w] == matrice[n - 1][w - round(int(e.price)/100)] + round(int(e.benefit)/100):
            #print('mat:', matrice[n][w], n, w, e)
            actions_selection.append(e)            
            w -= round(int(e.price)/100)        
        n -= 1
    display_algo_data(actions_selection)    
    return matrice[-1][-1], actions_selection

