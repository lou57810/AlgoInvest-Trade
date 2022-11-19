from action import Action
import csv


class Algo:

    
    def __init__(self, file, max_price):
        self.max_price = max_price
        self.file = file
        self.sumPrice = 0
        self.sumBenefit = 0
        self.best_panel = []        

    def naive_solution_execute(self):        
        data = self.get_datas(self.file)        
        sorted_benefit = self.sort_by_benefit(data)        
        action_selection = naive_solution(sorted_benefit, self.max_price)
        display_action_selection(action_selection)

    def display_fbrut_algo(self):
        self.bin_increment(1048576)        

    # ------- Getting datas into array 'data'-------
    def get_datas(self, file):
        data = []
        with open(self.file, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                action = Action(line[0], line[1], line[2])
                print("Actions:", action)
                data.append(action)                
        return data    

    def sort_by_benefit(self, data):
        sorted_benefit = sorted(data, key=lambda action: action.benefit)
        return sorted_benefit

    # Brut Force fcts:

    
    def display_val(self, val, panel_actions):
        temp = []
        
        k = 0
        somme_temp_prices = 0
        somme_temp_benefits = 0
        sumPrice = 0
        sumBenefit = 0
        
        for elt in val:
            #index_len = len(elt)            
            for j in elt:                
                # j = valeur binaire (1/0) k index n° bit
                if j == '1':            # poids binaire = 1                    
                    temp.append(panel_actions[k])                    
                    somme_temp_prices += int(panel_actions[k].price)
                    somme_temp_benefits += float(panel_actions[k].benefit)
                
                k += 1
        # Echange meilleure combinaison actions            
            if somme_temp_prices < 500:
                if somme_temp_prices > self.sumPrice:
                    self.sumPrice = somme_temp_prices                
                            
                if somme_temp_benefits > self.sumBenefit:
                    self.sumBenefit = somme_temp_benefits                
                    self.best_panel = temp
        # Remise à zéros
            somme_temp_prices = 0
            somme_temp_benefits = 0
            temp = []                               
        print('sommeTotalPrix:', self.sumPrice)
        print('sommeTotalBenef:', self.sumBenefit)
        print('best_panel:', self.best_panel)
            
        
    
    def bin_increment(self, max_value):        
        panel_actions = self.get_datas(self.file)
        
        for i in range(max_value):        
            val = bin(i)
            val = val[2:].split()
            self.display_val(val, panel_actions)
            i += 1

    def somme_benefices(self, temp):   # tab = temp
        somme_benef = 0        
        for elt in temp:
            print("tempElt", elt)
            
        



def naive_solution(sorted_benefit, max_price):
    cumul_price = 0
    action_selection = []
    while sorted_benefit:
        action = sorted_benefit.pop()
        if int(action.price) + cumul_price <= max_price:
            action_selection.append(action)
            cumul_price += int(action.price)
    return action_selection

def display_action_selection(action_selection):
    total_p = 0
    total_b = 0
    for action in action_selection:
        total_p = total_p + int(action.price)
        total_b = total_b + float(action.benefit)
        
        print(action)
    print("Prix total:", total_p)
    print("Benefice total:", total_b)





