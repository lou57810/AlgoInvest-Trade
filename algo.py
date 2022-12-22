from action import Action
from datetime import datetime
import os
import csv


class Algo:

    def __init__(self, file_in, file_out, max_price):
        self.file_in = file_in
        self.file_out = file_out
        self.max_price = max_price
        self.nb_line_in = 0
        self.nb_line_out = 0

    def execute(self):
        # Appel de la fct transformant .csv en tableau actions
        # data = self.get_datas(self.file_in)
        start = datetime.now()
        self.algo_generic()
        end = datetime.now()
        td = (end - start).total_seconds()
        print(f'Timing: {td:.07f}s')

    def algo_generic(self):
        pass

    def get_datas(self, file_in):
        data = []
        self.file_out = self.calcul_profit(file_in)
        with open(self.file_out, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                action = Action(line[0], line[1], line[2])
                data.append(action)
        return data

    def sort_by_benefit(self, data):
        sorted_benefit = sorted(data, key=lambda action: float(action.benefit))
        return sorted_benefit

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
    def calcul_profit(self, file_in):
        # print('file_in:', file_in)
        temp = []
        new_action_panel = []
        if os.path.isfile(self.file_out):
            pass
        else:
            temp = []
            with open(file_in, 'r') as file:
                # skip first row(En-t�tes: name,price,profit)
                next(file)
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    temp.append(line)
                    self.nb_line_in += 1

                for item in temp:
                    name = item[0]
                    price = float(item[1])
                    ratio = int(round(float(item[2]) * 100))
                    benefit = round((price * ratio) / 10000, 6)
                    # supprime les valeurs incorrectes
                    if price > 0 and benefit > 0:
                        new_action_panel.append([name, price, benefit])
                    elif price <= 0 or benefit <= 0:
                        self.nb_line_out += 1

                for item in new_action_panel:
                    self.write_to_csv(self.file_out, item)
        print('nblignes_in:', self.nb_line_in,
              'nblignes_out:', self.nb_line_out)
        return self.file_out

    # ----------- Writing to new useable csv file ------------
    def write_to_csv(self, file, fields):
        with open(file, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(fields)
