from greedy import Greedy
from bruteforce import Binary
from recursif import Recursiv
from optimized import OptiAlgo


def main():

    menu_options = {
        1: '1: Solution test naive      (algo greedy).',
        2: '2: Solution test Brut Force (algo binaire).',
        3: '3: Solution test Brut Force (algo recursif)',
        4: '4: Solution test optimisee  (algo dynamique)',
        5: '5: Solution optimisee (algo dynamique) Sienna1',
        6: '6: Solution optimisee (algo dynamique) Sienna2',
        7: '7: Test Brut Force binaire Sienna1 (20 actions)',
        8: '8: Test Brut Force Sienna2 binaire(panier restreint 20 actions)',
        9: '9: Test recursif Sienna2(panier restreint 20 actions)',
        0: '0: Exit',
    }

    def print_menu():
        for key in menu_options.keys():
            print(key, '--', menu_options[key])

    print_menu()
    option = int(input('Enter your choice: '))

    if option == 1:
        sol_naive = Greedy("CsvData/data0.csv",
                           "CsvData/datatest.csv", 500)
        sol_naive.execute()
    elif option == 2:
        sol_brut_bin = Binary("CsvData/data0.csv",
                              "CsvData/datatest.csv", 500)
        sol_brut_bin.execute()
    elif option == 3:
        sol_brut_recursif = Recursiv("CsvData/data0.csv",
                                     "CsvData/datatest.csv", 500)
        sol_brut_recursif.execute()
    elif option == 4:
        sol_brut_dyn = OptiAlgo("CsvData/data0.csv",
                                "CsvData/datatest.csv", 500)
        sol_brut_dyn.execute()
    elif option == 5:
        sol_brut = OptiAlgo("CsvData/dataset1_Python+P7.csv",
                            "CsvData/dataset1.csv", 500)
        sol_brut.execute()
    elif option == 6:
        sol_brut = OptiAlgo("CsvData/dataset2_Python+P7.csv",
                            "CsvData/dataset2.csv", 500)
        sol_brut.execute()
    elif option == 7:
        sol_brut = Binary("CsvData/dataset1_Python+P7_20.csv",
        "CsvData/dataset11.csv", 500)
        sol_brut.execute()
    elif option == 8:
        sol_brut = Binary("CsvData/dataset2_Python+P7_25.csv",
        "CsvData/dataset12.csv", 500)
        sol_brut.execute()
    elif option == 9:
        sol_brut = Recursiv("CsvData/dataset2_Python+P7_25.csv",
        "CsvData/dataset12.csv", 500)
        sol_brut.execute()
    elif option == 0:
        print('Sortie programme.')
        exit()
    else:
        print('Invalid option. Please, enter a number between 1 & 10')


if __name__ == '__main__':

    main()
