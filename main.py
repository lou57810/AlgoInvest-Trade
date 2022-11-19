from action import Action
from algo import Algo
#import binIncrementer

import csv
#import bruteforce



def main ():
    # sol_naive = Solution("action_panel.csv", 500)    
    # sol_naive.naive_solution_execute()

    sol_brut = Algo("action_panel.csv", 500)
    sol_brut.display_fbrut_algo()


    
    



    
    
    
    

    
  
if __name__ == '__main__':
    main()