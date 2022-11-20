from action import Action
from algo import Algo
#import binIncrementer

import csv
#import bruteforce



def main ():

    menu_options = {
        1: 'Option 1 : Solution naive.',
        2: 'Option 2: Solution Brut Force',
        3: 'Exit',
    }

    def print_menu():
        for key in menu_options.keys():
            print(key, '--', menu_options[key])
    print_menu()

    option = int(input('Enter your choice: '))
    if option == 1:
        sol_naive = Algo("action_panel.csv", 500)    
        sol_naive.naive_solution_execute()
    elif option == 2:
        sol_brut = Algo("action_panel.csv", 500)
        sol_brut.fbrut_algo_execute()
    elif option == 3:
        print('Fin du programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 3')


    
    



    
    
    
    

    
  
if __name__ == '__main__':
    main()