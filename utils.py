from action import Action
import csv
import os
import math
from decimal import *


class Utils:

    
    def __init__(self):
        pass

    def round_up(self, nombre, decimals = 0):
        multiplier = 10 ** decimals
        return math.ceil(nombre * multiplier) / multiplier
        

    # ------- Getting datas into array 'data'-------
    def multiply_datas(self, file_in, file_out):        
        temp = []
        new_action_panel = []
        #file_out = 'CsvData/new_action_panel.csv'
        if os.path.isfile(file_out):
            pass
        else:
            temp = []
            with open(file_in, 'r') as file:
                next(file)          #skip first row(name,price,profit##*##??)
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    temp.append(line)
                for item in temp:
                    name = item[0]                    
                    price = self.round_up(float(item[1])) * 100
                    price = int(price)
                    benefit = self.round_up(float(item[2])) * 100
                    benefit = int(benefit)
                    new_action_panel.append([name, price, benefit])
                for item in new_action_panel:
                    self.write_to_csv(file_out, item)
                    
                    
                    
            
                
            

    # ----------- Writing to new useable csv file ------------
    def write_to_csv(self, file, fields):
        #print('fields:', fields)
        with open(file, 'a', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, delimiter=',')
            # writing the data rows                
            csvwriter.writerow(fields)
            
    '''
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
    '''
        
