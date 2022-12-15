from action import Action
from datetime import datetime
import os
import csv

class Algo:

    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price
        

    def execute(self):        
        data = self.get_datas(self.file)                  # Appel de la fct transformant .csv en tableau actions
        start = datetime.now()
        self.algo_generic()
        end = datetime.now()
        dt = td = (end - start).total_seconds()
        print(f'Timing: {td:.07f}s')

    def algo_generic(self):
        pass

    def get_datas(self, file):        
        data = []        
        with open(file, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:                
                if float(line[1]) > 0 and float(line[2]) > 0:
                    action = Action(line[0], float(line[1]), float(line[2]))
                    data.append(action)    
        return data

    def sort_by_benefit(self, data):
        sorted_benefit = sorted(data, key=lambda action: action.benefit)        
        return sorted_benefit
    '''
    def display_algo_data2(self, tab):
        somme1 = 0
        somme2 = 0
        for elt in tab:        
            somme1 += float(elt.price)        
            somme2 += float(elt.benefit)        
            elt.benefit = round(float(elt.benefit), 6)        
        print('Actions panel:', tab)
        print('Prix total:', round(somme1 / 100, 2))
        print("Benefice total:", round(somme2 / 100, 2))
    '''

    def display_algo_data(self, tab):
        somme1 = 0
        somme2 = 0
        for elt in tab:        
            somme1 += float(elt.price)        
            somme2 += float(elt.benefit)        
            elt.benefit = round(float(elt.benefit), 6)        
        print('Actions panel:', tab)
        print('Prix total:', round(somme1, 2))
        print("Benefice total:", round(somme2, 2))

    # ------- Getting datas into array 'data'-------
    def calcul_profit(file_in, file_out):
        nb_line_in = 0
        nb_line_out = 0
        temp = []
        new_action_panel = []        
        if os.path.isfile(file_out):
            pass
        else:
            temp = []
            
            with open(file_in, 'r') as file:
                next(file)          #skip first row(name,price,profit##*##??)
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    temp.append(line)
                    nb_line_in += 1
                for item in temp:
                    name = item[0]                    
                    price = float(item[1])                    
                    ratio = int(round(float(item[2]) * 100))
                    benefit = round((price * ratio) / 10000, 6)
                    if price > 0 and benefit > 0:                       # supprime les valeurs incorrectes
                        new_action_panel.append([name, price, benefit])
                    else:
                        nb_line_out += 1

                for item in new_action_panel:
                    write_to_csv(file_out, item)
            #print(file_in, 'nombre actions:', nb_line_in, 'nombre data bad:', nb_line_out, 'nombre data restant:', nb_line_in - nb_line_out)

    # ----------- Writing to new useable csv file ------------
    def write_to_csv(file, fields):       
        with open(file, 'a', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, delimiter=',')
            # writing the data rows                
            csvwriter.writerow(fields)

