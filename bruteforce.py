import csv


def lit_csv():
    file = open("dataBrut.csv", "r")
    test = csv.reader(file)
    for row in test:
        print(row[1])


# lit_csv()

def lit_elt(file):
    with open(file, 'r') as f:
        ligne = f.readline()
        premierElement = ligne.split(',')[0]
        print(premierElement)


# lit_elt('dataBrut.csv')
"""
with open('dataBrut.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Actions #', 'Coût par action (en euros)', 'Bénéfice (après 2 ans'])
    writer.writerow(['Action-1', 	'20', 	'5%'])
    writer.writerow(['Action-2', 	'30', 	'10%'])
    writer.writerow(['Action-3', 	'50',	'15%'])
    writer.writerow(['Action-4', 	'70', 	'20%'])
    writer.writerow(['Action-5', 	'60', 	'17%'])
    writer.writerow(['Action-6', 	'80', 	'25%'])
    writer.writerow(['Action-7', 	'22', 	'7%'])
    writer.writerow(['Action-8', 	'26', 	'11%'])
    writer.writerow(['Action-9', 	'48', 	'13%'])
    writer.writerow(['Action-10', 	'34', 	'27%'])
    writer.writerow(['Action-11',   '42', 	'17%'])
    writer.writerow(['Action-12', 	'110', 	 '9%'])
    writer.writerow(['Action-13', 	'38', 	'23%'])
    writer.writerow(['Action-14', 	'14', 	'1%'])
    writer.writerow(['Action-15', 	'18', 	'3%'])
    writer.writerow(['Action-16', 	'08', 	'8%'])
    writer.writerow(['Action-17', 	'04', 	'12%'])
    writer.writerow(['Action-18',   '10', 	'14%'])
    writer.writerow(['Action-19', 	'24',  	'21%'])
    writer.writerow(['Action-20', 	'114', 	'18%'])
"""
with open('dataBrutAlpha.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Actions #', 'Coût par action (en euros)', 'Bénéfice (après 2 ans'])
    writer.writerow(['A', 	'20', 	'5%'])
    writer.writerow(['B', 	'30', 	'10%'])
    writer.writerow(['C', 	'50',	'15%'])
    writer.writerow(['D', 	'70', 	'20%'])
    writer.writerow(['E', 	'60', 	'17%'])
    writer.writerow(['F', 	'80', 	'25%'])
    writer.writerow(['G', 	'22', 	'7%'])
    writer.writerow(['H', 	'26', 	'11%'])
    writer.writerow(['I', 	'48', 	'13%'])
    writer.writerow(['J', 	'34', 	'27%'])
    writer.writerow(['K',   '42', 	'17%'])
    writer.writerow(['L', 	'110', 	 '9%'])
    writer.writerow(['M', 	'38', 	'23%'])
    writer.writerow(['N', 	'14', 	'1%'])
    writer.writerow(['O', 	'18', 	'3%'])
    writer.writerow(['P', 	'08', 	'8%'])
    writer.writerow(['Q', 	'04', 	'12%'])
    writer.writerow(['R',   '10', 	'14%'])
    writer.writerow(['S', 	'24',  	'21%'])
    writer.writerow(['T', 	'114', 	'18%'])

file = open('dataBrutAlpha.csv')
read = csv.reader(file)

for row in read:
    print('row:', row)
    print('\n')
tab = []
with open('dataBrutAlpha.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        tab.append(line)
        print(line)

print("row0:", row[0])
print("line1_0:", tab[1][0])
print("Tab:", tab)





def valid_fct():
    pass

# def calcul_benefice():
