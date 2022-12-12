from action import Action
from greedy_algo import Greedy
from bruteforce import Binary
from recursif_algo import Recursiv
from dynamic_algo import Dynalgo
from optimized import Optidynalgo


import os
import time
import csv


def main ():

 # ------- Getting datas into array 'data'-------
    def calcul_profit(file_in, file_out):        
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
                    price = float(item[1])                    
                    ratio = int(round(float(item[2]) * 100))
                    benefit = round((price * ratio) / 10000, 6)
                    if price > 0 and benefit > 0:
                        new_action_panel.append([name, price, benefit])                    
                for item in new_action_panel:
                    write_to_csv(file_out, item)

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
        3: '3: Solution recursive(panier restreint 13 actions)',
        4: '4: Solution dynamique',
        5: '5: TestBinaireSienna1(panier restreint 25 actions)',
        6: '6: TestDynamicSienna1',
        7: '7: TestBinaireSienna2(panier restreint 20 actions)',
        8: '8: TestDynamicSienna2',
        9: '9: Exit',
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
        sol_brut_recursif = Recursiv("CsvData/recursif_panel.csv", 500)        
        sol_brut_recursif.execute()
    elif option == 4:
        file = "CsvData/datatest.csv"
        sol_brut_dyn = Dynalgo(file, 500)   
        sol_brut_dyn.execute()
    elif option == 5:
        file = "CsvData/dataset11.csv"
        sol_brut = Binary("CsvData/dataset11.csv", 500)   
        sol_brut.execute()
    elif option == 6:        
        file = "CsvData/dataset1.csv"
        sol_brut = Optidynalgo(file, 500)   
        sol_brut.execute()
    elif option == 7:        
        sol_brut = Binary("CsvData/dataset12.csv", 500)   
        sol_brut.fbrut_algo_execute()
    elif option == 8:        
        sol_brut = Optidynalgo("CsvData/dataset2.csv", 500)   
        sol_brut.execute()
    elif option == 9:
        print('Fin du programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 9')
        
   
  
if __name__ == '__main__':
    main()