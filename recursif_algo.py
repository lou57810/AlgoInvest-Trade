from action import Action
import csv

class Recursiv:

	def __init__(self, file, max_price):
		self.file = file
		self.max_price = max_price
        self.tab = []
        self.start = 0

	def recursif_algo(self, data, max_price, selected_actions):      # 10 mn / 12 actions    
    
        if data:
            action1 = recursif_algo(data[1:], max_price, selected_actions)        
            list_actions1 = recursif_algo(data[1:], max_price, selected_actions) 
            action = data[0]
        
            if int(action.price) <= max_price:
                action2 = recursif_algo(data[1:], max_price, selected_actions)
            
                list_actions2 = recursif_algo(data[1:], max_price - int(action.price), selected_actions + [action])
                if action1 < action2:
                    return action2, list_action2
                
            return action1, list_actions1        
        else:
            #benefit = sum([int(i.benefit) for i in selected_actions])
            self.get_tab(selected_actions)
            return sum([int(i.benefit) for i in selected_actions]), selected_actions


    def get_tab(sa):    
        tab.append(sa)

    def display_tab(tab):    
        self.display_algo_data(tab[-1])

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