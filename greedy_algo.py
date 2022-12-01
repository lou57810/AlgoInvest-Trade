from action import Action
import csv

class Greedy:

    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price
        

    def naive_solution_execute(self):        
            data = self.get_datas(self.file)            # tableau des actions avec prix et benefices non triés        
            sorted_benefit = self.sort_by_benefit(data)        
            actions_selection = self.naive_solution(sorted_benefit, self.max_price)        
            self.display_algo_data(actions_selection)

    def sort_by_benefit(self, data):
            sorted_benefit = sorted(data, key=lambda action: action.benefit)        
            return sorted_benefit

    def naive_solution(self, sorted_benefit, max_price):
            cumul_price = 0
            action_selection = []
            while sorted_benefit:                   # Tant que l'on boucle sur la liste triée
                action = sorted_benefit.pop()       # retranche de la liste
                if int(action.price) + cumul_price <= max_price:
                    action_selection.append(action)
                    cumul_price += int(action.price)
            return action_selection

    # ------- Getting datas into array 'data'-------
    def get_datas(self, file):        
        data = []
        with open(self.file, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                action = Action(line[0], line[1], line[2])                
                data.append(action)
        
        return data

    def display_algo_data(self, tab):
        somme1 = 0
        somme2 = 0
        for elt in tab:        
            somme1 += int(elt.price)
            somme2 += int(elt.benefit)
            elt.benefit = int(elt.benefit)/100
        print('Actions panel:', tab)
        print('Prix total:', somme1)
        print("Benefice total:", somme2 / 100)