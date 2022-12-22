from algo import Algo


class OptiAlgo(Algo):

    def __init__(self, file_in, file_out, max_price):
        super().__init__(file_in, file_out, max_price)
        self.max_price = max_price

    def algo_generic(self):
        # tableau des actions avec prix et benefices sans tri
        data = self.get_datas(self.file_in)
        self.dynamic_algo(data, self.max_price)

    def dynamic_algo(self, data, max_price):
        # Initialisation de la matrice � 0x et 0y
        matrice = \
            [[1 for x in range(max_price + 1)]
             for x in range(len(data) + 1)]

        # liste action en x et poids/valeurs en y
        for i in range(1, len(data) + 1):  # parcours des y actions
            # parcours des prix     # w=  1-->501
            for w in range(1, max_price + 1):
                if float(data[i - 1].price) <= w:
                    matrice[i][w] = \
                        max(float(data[i - 1].benefit) +
                            matrice[i - 1][int(w - float(data[i - 1].price))],
                            matrice[i - 1][w])

                else:
                    matrice[i][w] = matrice[i - 1][w]

        w = max_price
        n = len(data)  # nombre d'objets (actions)
        actions_selection = []
        # recup�ration des donnees finales
        while w >= 0 and n >= 0:
            e = data[n - 1]
            if matrice[n][w] == \
                    matrice[n - 1][int(w - float(e.price))] + float(e.benefit):
                actions_selection.append(e)
                w -= round(float(float(e.price)))

            n -= 1
        self.display_algo_data(actions_selection)
