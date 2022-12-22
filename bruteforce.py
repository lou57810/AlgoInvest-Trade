from algo import Algo


class Binary(Algo):

    def __init__(self, file_in, file_out, max_price):
        super().__init__(file_in, file_out, max_price)
        self.sumPrice = 0
        self.sumBenefit = 0

    def algo_generic(self):
        data = self.get_datas(self.file_in)
        self.bin_increment(data, 2**len(data))
        self.display_algo_data(self.best_panel)

    # ------------------ Brut Force Solution1 (binaire): ----------------
    def select_best_binary_value(self, val, panel_actions):  # val = bin(i)
        temp = []

        k = len(val[0]) - 1
        somme_temp_prices = 0
        somme_temp_benefits = 0
        # ex:   val, val[0] ['11011001100101110'] 11011001100101110
        for j in val[0]:
            # j = valeur binaire (1/0) k index n� bit
            if j == '1':            # poids binaire = 1
                temp.append(panel_actions[k])

                somme_temp_prices += float(panel_actions[k].price)
                somme_temp_benefits +=\
                    round(float(panel_actions[k].benefit), 2)
            k -= 1

        # Echange meilleure combinaison actions
        if somme_temp_benefits > self.sumBenefit and somme_temp_prices <= 500:
            self.sumPrice = somme_temp_prices
            self.sumBenefit = somme_temp_benefits
            self.best_panel = temp

    # Incr�ment binaire, et appel fct display_val
    def bin_increment(self, data, max_value):
        panel_actions = data                # .csv en tableau actions

        for i in range(max_value):
            val = bin(i)            # ex:  0b 1110110110010101
            val = val[2:].split()   # ex:  ['10111001110011000']
            self.select_best_binary_value(val, panel_actions)
