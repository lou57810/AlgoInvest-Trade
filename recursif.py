from algo import Algo


class Recursiv(Algo):

    def __init__(self, file_in, file_out, max_price):
        super().__init__(file_in, file_out, max_price)
        self.selected_actions = []

    def algo_generic(self):
        # tableau des actions avec prix et benefices non tri�s
        data = self.get_datas(self.file_in)
        recursif_algo(self.max_price, data, self.selected_actions)
        self.display_algo_data(tab[-1])


tab = []


def recursif_algo(max_price, data, selected_actions):
    if data:
        action1, list_actions1 = \
            recursif_algo(max_price, data[1:], selected_actions)
        action = data[0]

        if float(action.price) <= max_price:
            action2, list_actions2 = \
                recursif_algo(max_price - float(action.price),
                              data[1:], selected_actions + [action])

            if int(action1) < int(action2):
                return int(action2), list_actions2
        tab.append(list_actions1)
        return int(action1), list_actions1

    else:
        return sum([float(i.benefit) for i in selected_actions]),\
               selected_actions
