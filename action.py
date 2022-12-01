import csv
import os


with open('data_origin.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    # writer.writerow(['Actions #', 'Coût par action (en euros)', 'Bénéfice (après 2 ans'])
    writer.writerow(['A1', '20', '5%'])
    writer.writerow(['A2', '30', '10%'])
    writer.writerow(['A3', '50', '15%'])
    writer.writerow(['A4', '70', '20%'])
    writer.writerow(['A5', '60', '17%'])
    writer.writerow(['A6', '80', '25%'])
    writer.writerow(['A7', '22', '7%'])
    writer.writerow(['A8', '26', '11%'])
    writer.writerow(['A9', '48', '13%'])
    writer.writerow(['A10', '34', '27%'])
    writer.writerow(['A11', '42', '17%'])
    writer.writerow(['A12', '110', '9%'])
    writer.writerow(['A13', '38', '23%'])
    writer.writerow(['A14', '14', '1%'])
    writer.writerow(['A15', '18', '3%'])
    writer.writerow(['A16', '08', '8%'])
    writer.writerow(['A17', '04', '12%'])
    writer.writerow(['A18', '10', '14%'])
    writer.writerow(['A19', '24', '21%'])
    writer.writerow(['A20', '114', '18%'])


class Action:


    def __init__(self, name, price, benefit):        
        self.name = name
        self.price = price
        self.benefit = benefit

    def __str__(self):
        return str(self.name) + ' ' + str(self.price) + ' ' + str(self.benefit)

    def __repr__(self):
        return str(self.name) + ' ' + str(self.price) + ' ' + str(self.benefit)

    def calcul_and_write_benefit(self, file):
        temp = []
        action_panel = []
        with open('data_origin.csv', 'a') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                temp.append(line)
            
        for elt in temp:
            ratio = (elt[2].split('%'))[0]
            benef = int(elt[1]) * int(ratio) / 100
            elt[2] = benef        
            action_panel.append([elt[0], elt[1], elt[2]])

        for elt in action_panel:
            write_to_csv('action_panel.csv', elt)


    
# ----------- Writing to new useable csv file ------------
def write_to_csv(file, fields):    
    if os.path.isfile(file):
        pass
    else:
        with open(file, 'a', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, delimiter=',')
            # writing the data rows
            csvwriter.writerow(fields)

 







		

