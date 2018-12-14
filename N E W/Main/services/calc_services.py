from models.calc_model import Calculator

class Calculator_services(object):
    def __init__(self):
        self.keywords = []

    def find_price(self, choice, days):
        try:
            price_dict = {"suv": 100000, "mini": 50000, "sedan": 50000, "sport": 200000,"mpv": 75000}
            price = 0
            for key, value in price_dict.items():
                if choice == key:
                    price = value
            
            total_cost = price * int(days)
        except Exception:
            total_cost = 0

        return total_cost
