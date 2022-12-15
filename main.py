# -*- coding: utf-8 -*-
from action import Action
from greedy import Greedy
from bruteforce import Binary
from recursif import Recursiv
from optimized import OptiAlgo



import os
import time
import csv


def main ():

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

    calcul_profit("CsvData/data0.csv", "CsvData/datatest.csv")
    calcul_profit("CsvData/dataset1_Python+P7.csv", "CsvData/dataset1.csv")
    calcul_profit("CsvData/dataset2_Python+P7.csv", "CsvData/dataset2.csv")
    
    menu_options = {        
        1: '1: Solution naive (algo greedy).',
        2: '2: Solution Brut Force (algo binaire).',
        3: '3: Solution Brut Force recursive',
        4: '4: Solution optimisee (dynamique)',
        5: '5: Solution Brut Force Sienna1 binaire(panier restreint 20 actions)',
        6: '6: Test optimisee (dynamique) Sienna1',
        7: '7: Test Brut Force Sienna2 binaire(panier restreint 20 actions)',
        8: '8: Test optimisee (dynamique) Sienna2',
        9: '9: Test recursif Sienna2',
        0: '0: Exit',
    }

    def print_menu():
        for key in menu_options.keys():
            print(key, '--', menu_options[key])

    print_menu()
    option = int(input('Enter your choice: '))
    
    if option == 1:        
        sol_naive = Greedy("CsvData/datatest.csv", 500)
        sol_naive.execute()
    elif option == 2:         
        sol_brut_bin = Binary("CsvData/datatest.csv", 500)
        sol_brut_bin.execute()
    elif option == 3:
        sol_brut_recursif = Recursiv("CsvData/datatest.csv", 500)
        sol_brut_recursif.execute()
    elif option == 4:                
        sol_brut_dyn = OptiAlgo("CsvData/datatest.csv", 500)
        sol_brut_dyn.execute()
    elif option == 5:        
        sol_brut = Binary("CsvData/dataset11.csv", 500)   
        sol_brut.execute()
    elif option == 6:
        sol_brut = OptiAlgo("CsvData/dataset1.csv", 500)   
        sol_brut.execute()
    elif option == 7:        
        sol_brut = Binary("CsvData/dataset12.csv", 500)   
        sol_brut.execute()
    elif option == 8:        
        sol_brut = OptiAlgo("CsvData/dataset2.csv", 500)   
        sol_brut.execute()
    elif option == 9:        
        sol_brut = Recursiv("CsvData/dataset12.csv", 500)   
        sol_brut.execute()
    elif option == 0:
        print('Fin du programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 10')
   
  
if __name__ == '__main__':
    main()