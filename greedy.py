from algo import Algo


class Greedy(Algo):

    def __init__(self, file_in, file_out, max_price):
        super().__init__(file_in, file_out, max_price)

    def algo_generic(self):
        # tableau des actions avec prix et benefices non tri�s)
        data = self.get_datas(self.file_in)
        # print('data:', data)
        sorted_benefit = self.sort_by_benefit(data)
        actions_selection = self.naive_solution(sorted_benefit, self.max_price)
        self.display_algo_data(actions_selection)

    def naive_solution(self, sorted_benefit, max_price):
        cumul_price = 0  # Au d�part le prix de la liste est nul.
        action_selection = []
        while sorted_benefit:  # Tant que l'on boucle sur la liste tri�e
            # retranche de la liste l'�l�ment
            # � la plus grande valeur (au sommet de la pile)
            action = sorted_benefit.pop()
            if float(action.price) + cumul_price <= max_price:
                action_selection.append(action)
                cumul_price += float(action.price)
        return action_selection
