from utils import get_datas, display_algo_data
from datetime import datetime

class Algo:

    def __init__(self, file, max_price):
        self.file = file
        self.max_price = max_price
        

    def execute(self):        
        data = get_datas(self.file)                  # Appel de la fct transformant .csv en tableau actions
        start = datetime.now()
        self.algo_generic()
        end = datetime.now()
        dt = td = (end - start).total_seconds()
        print(f'Timing: {td:.05f}s')

    def algo_generic(self):
        pass
        