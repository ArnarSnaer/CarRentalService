from models.calc_model import Calculator

class Calculator_services(object):
    def __init__(self):
        self.keywords = []

    def find_price(self, choice, days):
        try:
            price_dict = {"suv": 100000, "mini": 50000, "sedan": 50000, "sport": 200000,"mpv": 75000}
            base_price = 0
            for key, value in price_dict.items():
                if choice == key:
                    base_price = value
            
            total_cost_without_ins = base_price * int(days)
            total_cost_with_ins = total_cost_without_ins + 12000
        except Exception:
            base_price = 0

        return total_cost_without_ins, total_cost_with_ins, base_price
