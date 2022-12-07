from action import Action
from utils import get_datas, display_algo_data
from algo import Algo
import csv

class Greedy(Algo):

    def __init__(self, file, max_price):
        super().__init__(file, max_price)

    #def naive_solution_execute(self, file):                        
    def algo_generic(self):        
        data = get_datas(self.file)          # tableau des actions avec prix et benefices non triés
        sorted_benefit = self.sort_by_benefit(data)        
        actions_selection = self.naive_solution(sorted_benefit, self.max_price)        
        display_algo_data(actions_selection)

    def sort_by_benefit(self, data):
            sorted_benefit = sorted(data, key=lambda action: action.benefit)        
            return sorted_benefit

    def naive_solution(self, sorted_benefit, max_price):
            cumul_price = 0
            action_selection = []
            while sorted_benefit:                   # Tant que l'on boucle sur la liste triée
                action = sorted_benefit.pop()       # retranche de la liste
                if int(action.price) + cumul_price <= max_price * 100:
                    action_selection.append(action)
                    cumul_price += int(action.price)
            return action_selection

    