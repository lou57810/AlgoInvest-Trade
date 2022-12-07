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
                    price = int(round(float(item[1]) * 100))
                    benefit = int(round(float(item[2]) * 100))                    
                    new_action_panel.append([name, price, benefit])
                for item in new_action_panel:
                    self.write_to_csv(file_out, item)

    # ----------- Writing to new useable csv file ------------
    def write_to_csv(self, file, fields):       
        with open(file, 'a', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, delimiter=',')
            # writing the data rows                
            csvwriter.writerow(fields)

def get_datas(file):        
    data = []
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if int(line[1]) > 0:
                action = Action(line[0], line[1], line[2])
                data.append(action)    
    return data

def display_algo_data(tab):
    somme1 = 0
    somme2 = 0
    for elt in tab:        
        somme1 += int(elt.price)
        somme2 += int(elt.benefit)
        elt.benefit = int(elt.benefit)/100
        elt.price = int(elt.price)/100
    print('Actions panel:', tab)
    print('Prix total:', somme1 / 100)
    print("Benefice total:", somme2 / 100)

def calc_profit(ratio):
    benefit = (price * ratio)/10000
    return benefit
