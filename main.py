from action import Action
from greedy_algo import Greedy
from binary_algo import Binary
from recursif_algo import Recursiv
from dynamic_algo import Dynalgo
from utils import Utils

import time
import csv



def main ():
    
    menu_options = {
        1: '1: Solution naive (algo greedy).',
        2: '2: Solution Brut Force (algo binaire).',
        3: '3: Solution recursive',
        4: '4: Solution dynamique',
        5: '5: TestBinaireSienna1',
        6: '6: TestDynamicSienna1',
        7: '7: TestBinaireSienna2',
        8: '8: TestDynamicSienna2',
        9: '9: Exit',
    }

    file1 = Utils()
    file2 = Utils()
    file1.multiply_datas("CsvData/dataset1_Python+P7.csv", "CsvData/dataset1.csv")
    file2.multiply_datas("CsvData/dataset2_Python+P7.csv", "CsvData/dataset2.csv")

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
        #sol_brut = Dynalgo("CsvData/action_panel.csv", 500)   
        #sol_brut.dynamic_algo_execute()
        sol_brut = Dynalgo("CsvData/action_panel.csv", 50000)   
        sol_brut.dynamic_algo_execute()
    elif option == 5:        
        sol_brut = Binary("CsvData/dataset11.csv", 500)   
        sol_brut.fbrut_algo_execute()
    elif option == 6:        
        sol_brut = Dynalgo("CsvData/dataset11.csv", 500)   
        sol_brut.dynamic_algo_execute()
    elif option == 7:        
        sol_brut = Binary("CsvData/dataset2_Python+P7.csv", 500)   
        sol_brut.fbrut_algo_execute()
    elif option == 8:        
        sol_brut = Dynalgo("CsvData/dataset2_Python+P7.csv", 500)   
        sol_brut.dynamic_algo_execute()
    elif option == 9:
        print('Fin du programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 3')


    
    



    
    
    
    

    
  
if __name__ == '__main__':
    main()