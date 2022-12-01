from action import Action
from greedy_algo import Greedy
from binary_algo import Binary
from dynamic_algo import Dynalgo

import time
#import binIncrementer

import csv
#import bruteforce



def main ():    
    
    menu_options = {
        1: 'Option 1 : Solution naive (algo glouton).',
        2: 'Option 2: Solution Brut Force (algo binaire).',
        3: 'Option 3: Solution recursive',
        4: 'Option 4: Solution dynamique',
        5: 'Option 5: Exit',
    }

    def print_menu():
        for key in menu_options.keys():
            print(key, '--', menu_options[key])
    print_menu()

    option = int(input('Enter your choice: '))
    if option == 1:
        sol_naive = Greedy("CsvData/action_panel.csv", 500)    
        sol_naive.naive_solution_execute()
    elif option == 2:
        sol_brut = Binary("CsvData/action_panel.csv", 500)
        sol_brut.fbrut_algo_execute()
    elif option == 3:
        sol_brut = Recursiv("CsvData/recursif_panel.csv", 500)   
        sol_brut.recursif_algo_execute()
    elif option == 4:        
        sol_brut = Dynalgo("CsvData/action_panel.csv", 500)   
        sol_brut.dynamic_algo_execute()
    elif option == 5:
        print('Fin du programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 3')


    
    



    
    
    
    

    
  
if __name__ == '__main__':
    main()