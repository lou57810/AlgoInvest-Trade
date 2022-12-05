from action import Action
import csv


class Binary:

    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price
        self.sumPrice = 0
        self.sumBenefit = 0

    def fbrut_algo_execute(self):
        data = self.get_datas(self.file)
        self.bin_increment(2**len(data))
        # Complexité: O(2**20)1048576

	# ------------------ Brut Force Solution1 (binaire): ----------------    
    def select_best_binary_value(self, val, panel_actions):  # val = bin(i)
        temp = []        
        
        k = len(val[0]) - 1
        somme_temp_prices = 0
        somme_temp_benefits = 0        
        
        for j in val[0]:            
            # j = valeur binaire (1/0) k index n° bit                
            if j == '1':            # poids binaire = 1                    
                temp.append(panel_actions[k])                                    
                somme_temp_prices += int(panel_actions[k].price) / 100    # int * 100
                somme_temp_benefits += int(panel_actions[k].benefit) / 100                
            k -= 1
                
        # Echange meilleure combinaison actions            
        if somme_temp_benefits > self.sumBenefit and somme_temp_prices <= 500:            
            self.sumPrice = somme_temp_prices
            self.sumBenefit = somme_temp_benefits                
            self.best_panel = temp
        
    # Incrément binaire, et appel fct display_val
    def bin_increment(self, max_value):        
        panel_actions = self.get_datas(self.file)
        
        for i in range(max_value):            
            val = bin(i)            
            val = val[2:].split()
            
            self.select_best_binary_value(val, panel_actions)        
        self.display_algo_data(self.best_panel)

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
            
        print('Actions panel:', tab)
        print('Prix total:', somme1 / 100)
        print("Benefice total:", somme2 / 100)