from action import Action
from algo import Algo
import csv

class Greedy(Algo):

    def __init__(self, file, max_price):
        super().__init__(file, max_price)
                            
    def algo_generic(self):        
        data = super().get_datas(self.file)          # tableau des actions avec prix et benefices non tri�s)
        print('data:', data)
        sorted_benefit = super().sort_by_benefit(data)        
        actions_selection = self.naive_solution(sorted_benefit, self.max_price)        
        super().display_algo_data(actions_selection)    

    def naive_solution(self, sorted_benefit, max_price):
        cumul_price = 0
        action_selection = []
        while sorted_benefit:                   # Tant que l'on boucle sur la liste tri�e
            action = sorted_benefit.pop()       # retranche de la liste
            # if int(action.price) + cumul_price <= max_price * 100:
            if int(action.price) + cumul_price <= max_price:
                action_selection.append(action)
                cumul_price += int(action.price)
        return action_selection

    