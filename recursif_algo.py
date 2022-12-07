from action import Action
import csv
from algo import Algo
from utils import get_datas , display_algo_data

class Recursiv(Algo):


    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price
        self.tab = []
        self.selected_actions = []
        self.start = 0

    #def recursif_algo_execute(self, file):                # Complexité: O()
    def algo_generic(self):
        data = get_datas(self.file)          # tableau des actions avec prix et benefices non triés
        recursif_algo(data, self.max_price, self.selected_actions)
        display_algo_data(tab[-1])

tab = []

def recursif_algo(data, max_price, selected_actions):      # 10 mn / 12 actions
    
    if data:
        action1 = recursif_algo(data[1:], max_price, selected_actions)        
        list_actions1 = recursif_algo(data[1:], max_price, selected_actions) 
        action = data[0]
        
        if int(int(action.price) / 100) <= max_price:
            action2 = recursif_algo(data[1:], max_price, selected_actions)
            
            list_actions2 = recursif_algo(data[1:], max_price - int(int(action.price)/100), selected_actions + [action])
            if action1 < action2:
                return action2, list_action2
                
        return action1, list_actions1        
    else:
        #benefit = sum([int(i.benefit) for i in selected_actions])
        tab.append(selected_actions)
        get_tab(selected_actions)
        
        return sum([int(int(i.benefit)/100) for i in selected_actions]), selected_actions

#tab = []

def get_tab(sa):    
    tab.append(sa)


